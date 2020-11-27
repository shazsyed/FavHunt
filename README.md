# FavHunt

Favicon based recon to fingerprint services running on a webserver.

#### Usuage:
`python3 favhunt.py -l domains.txt`

```
usage: favhunt.py [-h] -l LIST [-o OUTPUT] [-f FINGERPRINTS] [-t THREADS] [-v]

optional arguments:
  -h, --help       show this help message and exit
  -l LIST          List of domains
  -o OUTPUT        JSON output filename
  -f FINGERPRINTS  Path to fingerprints json file (default: fingerprints.json)
  -t THREADS       Threads (default: 20)
  -v               Verbose output
  ```

#### Credits:
Inspired by [FavFreak](https://github.com/devanshbatham/FavFreak) and thanks for fingerprints <3
