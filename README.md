# FavHunt

Favicon based recon to fingerprint services running on a webserver.

## Installation:
```
$ git clone https://github.com/shazsyed/FavHunt
$ cd FavHunt
$ pip install -r requirements.txt
```
## Usage:
`python3 favhunt.py -l domains.txt` or `cat domains.txt | python favhunt.py` 

```
usage: favhunt.py [-h] -l LIST [-o OUTPUT] [-f FINGERPRINTS] [-t THREADS] [-j] [-s] [-v]

optional arguments:
  -h, --help       show this help message and exit
  -l LIST          List of domains
  -o OUTPUT        JSON output filename
  -f FINGERPRINTS  Path to fingerprints json file (default: fingerprints.json)
  -t THREADS       Threads (default: 20)
  -j, --json       Stdout output in JSON
  -s, --silent     Only shows results with matched fingerprints
  -v, --verbose    Verbose output
  ```
  
  ![](https://i.imgur.com/8gvAckv.png)
  
 #### Using with jq:
  `python3 favhunt.py -l domains.txt -json | jq '.'`

## Credits:
Inspired by [FavFreak](https://github.com/devanshbatham/FavFreak) and thanks for fingerprints <3
