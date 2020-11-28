# FavHunt

Favicon based recon to fingerprint services running on a webserver.

#### Usage:
`python3 favhunt.py -l domains.txt`

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

#### Credits:
Inspired by [FavFreak](https://github.com/devanshbatham/FavFreak) and thanks for fingerprints <3
