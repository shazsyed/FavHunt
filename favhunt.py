import json
import requests
import codecs
import mmh3
import argparse
import urllib3

from concurrent import futures
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_hash(domain):
    response = requests.get(domain, verify=False, timeout=10)
    favicon = codecs.encode(response.content, "base64")
    hash = str(mmh3.hash(favicon))

    return domain, hash

def main():
    parser = argparse.ArgumentParser(description="Find favicon hashes to fingerprint services")
    parser.add_argument("-l", help="List of domains", required=True, dest="list")
    parser.add_argument("-o", help="JSON output filename", required=False, dest="output")
    parser.add_argument("-f", help="Path to fingerprints json file (default: fingerprints.json)", required=False, default="fingerprints.json", dest="fingerprints")
    parser.add_argument("-t", help="Threads (default: 20)", type=int, required=False, default=20, dest="threads")
    parser.add_argument("-j", "--json", help="Stdout output in JSON", action="store_true")
    parser.add_argument("-s", "--silent", help="Only shows results with matched fingerprints", action="store_true")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true", required=False)
    args = parser.parse_args()

    urls = []
    threads = []
    output = {}

    if Path(args.list).exists():
        with open(args.list, 'r') as file:
            data = file.read().splitlines()
    else:
        print("Invalid list")
        return

    for domain in data:
        if domain.strip()[-1] == '/':
            urls.append(f'{domain.strip()}favicon.ico')
        else:
            urls.append(f'{domain.strip()}/favicon.ico')

    with open(args.fingerprints, 'r') as file:
        fingerprints = json.load(file)

    with futures.ThreadPoolExecutor(args.threads) as executor:
        for url in urls:
            threads.append(executor.submit(get_hash, domain=url))
        for future in futures.as_completed(threads):
            try:
                domain, hash = future.result()
                matched_fingerprint = "None"
                
                if hash in fingerprints.keys():
                    matched_fingerprint = fingerprints[hash]
                output[domain] = {"hash": hash, "matched_fingerprint": matched_fingerprint}

                if (args.silent and not matched_fingerprint == "None") or (not args.silent):
                    if args.json:
                        print('{"domain": "%s", "fingerprint": "%s", "hash": "%s"}' %(domain, matched_fingerprint, hash))
                    else:
                        print(f'[{matched_fingerprint}][{hash}] {domain}')

            except Exception as e:
                if args.verbose:
                    print(f'[{type(e).__name__}] {domain}')

        if args.output:
            with open(args.output, 'w') as file:
                json.dump(output, file)

if __name__ == '__main__':
    main()