# Devops

DEVOPS 

TP1  


OBJECTIFS 

Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude
(passées en variable d'environnement) en utilisant openweather API dans le langage de
programmation de votre choix (bash, python, go, nodejs, etc)


GitHub repository : https://github.com/HadiJamalAhmad/Devops/edit/master

Docker Hub : https://hub.docker.com/repository/docker/hadi78/tp1

Openweather API
OpenWeatherMap est un service en ligne, appartenant à OpenWeather Ltd, qui fournit des données météorologiques mondiales via API, y compris des données météorologiques actuelles, des prévisions, des prévisions actuelles et des données météorologiques historiques pour n'importe quel emplacement géographique.

API call : https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

Méthodologie :
J'ai crée un wrapper en python, j'utilise request pour les appel API, os.environ pour récupérer les variables d'environnement.


Code python :

import requests
import os
import json
api_key = os.environ['API_KEY']
lat = os.environ['LAT']
lon = os.environ['LONG']
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)


Docker

Utilisation d'un environnement python pour le wrapper. L'environnement python est crée grace à Docker.

Dockerfile

FROM alpine:3.4

WORKDIR /app

RUN apk update && apk add \
curl  \
vim





Build

docker build . -t tp1:001
[+] Building 5.9s (7/7) FINISHED
 => [internal] load build definition from Dockerfile                    0.0s
 => => transferring dockerfile: 37B                                     0.0s 
 => [internal] load .dockerignore                                       0.0s 
 => => transferring context: 2B                                         0.0s 
 => [internal] load metadata for docker.io/library/alpine:3.4           5.8s 
 => [1/3] FROM docker.io/library/alpine:3.4@sha256:b733d4a32c4da6a00a8  0.0s
 => CACHED [2/3] WORKDIR /app                                           0.0s 
 => CACHED [3/3] RUN apk update && apk add curl  vim                    0.0s 
 => exporting to image                                                  0.0s 
 => => exporting layers                                                 0.0s 
 => => writing image sha256:66e17ee3d23aea8827cf037a271f1f3f90eb07a42b  0.0s 
 => => naming to docker.io/library/docker101:001                        0.0s 


TAG

docker tag docker101:0.0.1 hadi78/tp1:0.0.1

PUSH 


hadi@LAPTOP-ADEE62RQ:/mnt/c/Users/hadij/Downloads/Devops/tp1$ docker push hadi78/tp1:0.0.1
The push refers to repository [docker.io/hadi78/tp1]
847142acf4df: Mounted from hadi78/dockerapi
fc9e5b2da2bd: Mounted from hadi78/dockerapi
23f7bd114e4a: Mounted from hadi78/dockerapi
0.0.1: digest: sha256:cb9afa03204b31b43093e71db43d3586dadc1087601fc5b8d053a4b7009c92d9 size: 946


PULL
hadi@LAPTOP-ADEE62RQ:/mnt/c/Users/hadij/Downloads/Devops/tp1$ docker pull hadi78/tp1:0.0.1
0.0.1: Pulling from hadi78/tp1
Digest: sha256:cb9afa03204b31b43093e71db43d3586dadc1087601fc5b8d053a4b7009c92d9
Status: Image is up to date for hadi78/tp1:0.0.1
docker.io/hadi78/tp1:0.0.1



TRIVY 

hadi@LAPTOP-ADEE62RQ:/mnt/c/Users/hadij/Downloads/Devops/tp1$ docker run aquasec/trivy image python:3.4-alpine
2022-06-06T17:07:41.617Z        INFO    Need to update DB
2022-06-06T17:07:41.617Z        INFO    DB Repository: ghcr.io/aquasecurity/trivy-db
2022-06-06T17:07:41.617Z        INFO    Downloading DB...
6.43 MiB / 32.33 MiB [------------>_________________________________________________] 19.89% ? p/s ?13.07 MiB / 32.33 MiB [------------------------>____________________________________] 40.43% ? p/s ?19.30 MiB / 32.33 MiB [------------------------------------>________________________] 59.71% ? p/s ?25.16 MiB / 32.33 MiB [------------------------------------->__________] 77.83% 31.23 MiB p/s ETA 0s30.10 MiB / 32.33 MiB [-------------------------------------------->___] 93.11% 31.23 MiB p/s ETA 0s32.33 MiB / 32.33 MiB [---------------------------------------------->] 100.00% 31.23 MiB p/s ETA 0s32.33 MiB / 32.33 MiB [---------------------------------------------->] 100.00% 29.98 MiB p/s ETA 0s32.33 MiB / 32.33 MiB [---------------------------------------------->] 100.00% 29.98 MiB p/s ETA 0s32.33 MiB / 32.33 MiB [---------------------------------------------->] 100.00% 29.98 MiB p/s ETA 0s32.33 MiB / 32.33 MiB [-------------------------------------------------] 100.00% 19.57 MiB p/s 1.9s2022-06-06T17:07:47.583Z INFO    Detected OS: alpine
2022-06-06T17:07:47.583Z        INFO    Detecting Alpine vulnerabilities...  
2022-06-06T17:07:47.584Z        INFO    Number of language-specific files: 1
2022-06-06T17:07:47.584Z        INFO    Detecting python-pkg vulnerabilities...
2022-06-06T17:07:47.585Z        WARN    This OS version is no longer supported by the distribution: alpine 3.9.2
2022-06-06T17:07:47.585Z        WARN    The vulnerability detection may be insufficient because security updates are not provided

python:3.4-alpine (alpine 3.9.2)
================================
Total: 37 (UNKNOWN: 0, LOW: 4, MEDIUM: 16, HIGH: 13, CRITICAL: 4)

┌──────────────┬────────────────┬──────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│   Library    │ Vulnerability  │ Severity │ Installed Version │ Fixed Version │                            Title                             │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ expat        │ CVE-2018-20843 │ HIGH     │ 2.2.6-r0          │ 2.2.7-r0      │ expat: large number of colons in input makes parser consume  │
│              │                │          │                   │             
  │ high amount...                                               │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2018-20843                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ expat        │ CVE-2019-15903 │ HIGH     │ 2.2.6-r0          │ 2.2.7-r1      │ expat: heap-based buffer over-read via crafted XML input     │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-15903                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libbz2       │ CVE-2019-12900 │ CRITICAL │ 1.0.6-r6          │ 1.0.6-r7      │ bzip2: out-of-bounds write in function BZ2_decompress        │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-12900                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2019-1543  │ HIGH     │ 1.1.1a-r1         │ 1.1.1b-r1     │ openssl: ChaCha20-Poly1305 with long nonces                  │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1543                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2020-1967  │ HIGH     │ 1.1.1a-r1         │ 1.1.1g-r0     │ openssl: Segmentation fault in SSL_check_chain causes denial │
│              │                │          │                   │             
  │ of service                                                   │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-1967                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2021-23840 │ HIGH     │ 1.1.1a-r1         │ 1.1.1j-r0     │ openssl: integer overflow in CipherUpdate                    │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-23840                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2021-3450  │ HIGH     │ 1.1.1a-r1         │ 1.1.1k-r0     │ openssl: CA certificate check bypass with                    │
│              │                │          │                   │             
  │ X509_V_FLAG_X509_STRICT                                      │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-3450                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2019-1547  │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1d-r0     │ openssl: side-channel weak encryption vulnerability          │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1547                    │
│              ├────────────────┤          │                   │             
  ├──────────────────────────────────────────────────────────────┤
│              │ CVE-2019-1549  │          │                   │             
  │ openssl: information disclosure in fork()                    │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1549                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2019-1551  │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1d-r2     │ openssl: Integer overflow in RSAZ modular exponentiation on  │
│              │                │          │                   │             
  │ x86_64                                                       │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1551                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2020-1971  │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1i-r0     │ openssl: EDIPARTYNAME NULL pointer de-reference              │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-1971                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2021-23841 │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1j-r0     │ openssl: NULL pointer dereference in                         │
│              │                │          │                   │             
  │ X509_issuer_and_serial_hash()                                │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-23841                   │
│              ├────────────────┤          │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2021-3449  │          │                   │ 1.1.1k-r0     │ openssl: NULL pointer dereference in signature_algorithms    │
│              │                │          │                   │             
  │ processing                                                   │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-3449                    │
│              ├────────────────┼──────────┤                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2019-1563  │ LOW      │                   │ 1.1.1d-r0     │ openssl: information disclosure in PKCS7_dataDecode and      │
│              │                │          │                   │             
  │ CMS_decrypt_set1_pkey                                        │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1563                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcrypto1.1 │ CVE-2021-23839 │ LOW      │ 1.1.1a-r1         │ 1.1.1j-r0     │ openssl: incorrect SSLv2 rollback protection                 │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-23839                   │
├──────────────┼────────────────┼──────────┤                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2019-1543  │ HIGH     │                   │ 1.1.1b-r1     │ openssl: ChaCha20-Poly1305 with long nonces                  │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1543                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2020-1967  │ HIGH     │ 1.1.1a-r1         │ 1.1.1g-r0     │ openssl: Segmentation fault in SSL_check_chain causes denial │
│              │                │          │                   │             
  │ of service                                                   │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-1967                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2021-23840 │ HIGH     │ 1.1.1a-r1         │ 1.1.1j-r0     │ openssl: integer overflow in CipherUpdate                    │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-23840                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2021-3450  │ HIGH     │ 1.1.1a-r1         │ 1.1.1k-r0     │ openssl: CA certificate check bypass with                    │
│              │                │          │                   │             
  │ X509_V_FLAG_X509_STRICT                                      │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-3450                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2019-1547  │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1d-r0     │ openssl: side-channel weak encryption vulnerability          │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1547                    │
│              ├────────────────┤          │                   │             
  ├──────────────────────────────────────────────────────────────┤
│              │ CVE-2019-1549  │          │                   │             
  │ openssl: information disclosure in fork()                    │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1549                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2019-1551  │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1d-r2     │ openssl: Integer overflow in RSAZ modular exponentiation on  │
│              │                │          │                   │             
  │ x86_64                                                       │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1551                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2020-1971  │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1i-r0     │ openssl: EDIPARTYNAME NULL pointer de-reference              │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-1971                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2021-23841 │ MEDIUM   │ 1.1.1a-r1         │ 1.1.1j-r0     │ openssl: NULL pointer dereference in                         │
│              │                │          │                   │             
  │ X509_issuer_and_serial_hash()                                │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-23841                   │
│              ├────────────────┤          │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2021-3449  │          │                   │ 1.1.1k-r0     │ openssl: NULL pointer dereference in signature_algorithms    │
│              │                │          │                   │             
  │ processing                                                   │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-3449                    │
│              ├────────────────┼──────────┤                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2019-1563  │ LOW      │                   │ 1.1.1d-r0     │ openssl: information disclosure in PKCS7_dataDecode and      │
│              │                │          │                   │             
  │ CMS_decrypt_set1_pkey                                        │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-1563                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl1.1    │ CVE-2021-23839 │ LOW      │ 1.1.1a-r1         │ 1.1.1j-r0     │ openssl: incorrect SSLv2 rollback protection                 │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2021-23839                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ musl         │ CVE-2019-14697 │ CRITICAL │ 1.1.20-r4         │ 1.1.20-r5     │ musl libc through 1.1.23 has an x87 floating-point stack     │
│              │                │          │                   │             
  │ adjustment im ......                                         │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-14697                   │
│              ├────────────────┼──────────┤                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2020-28928 │ MEDIUM   │                   │ 1.1.20-r6     │ In musl libc through 1.2.1, wcsnrtombs mishandles particular │
│              │                │          │                   │             
  │ combinati ...                                                │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-28928                   │
├──────────────┼────────────────┼──────────┤                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│ musl-utils   │ CVE-2019-14697 │ CRITICAL │                   │ 1.1.20-r5     │ musl libc through 1.1.23 has an x87 floating-point stack     │
│              │                │          │                   │             
  │ adjustment im ......                                         │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-14697                   │
│              ├────────────────┼──────────┤                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2020-28928 │ MEDIUM   │                   │ 1.1.20-r6     │ In musl libc through 1.2.1, wcsnrtombs mishandles particular │
│              │                │          │                   │             
  │ combinati ...                                                │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-28928                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sqlite-libs  │ CVE-2019-8457  │ CRITICAL │ 3.26.0-r3         │ 3.28.0-r0     │ sqlite: heap out-of-bound read in function rtreenode()       │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-8457                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sqlite-libs  │ CVE-2019-19244 │ HIGH     │ 3.26.0-r3         │ 3.28.0-r2     │ sqlite: allows a crash if a sub-select uses both DISTINCT    │
│              │                │          │                   │             
  │ and window...                                                │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-19244                   │
│              ├────────────────┤          │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│              │ CVE-2019-5018  │          │                   │ 3.28.0-r0     │ sqlite: Use-after-free in window function leading to remote  │
│              │                │          │                   │             
  │ code execution                                               │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-5018                    │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sqlite-libs  │ CVE-2020-11655 │ HIGH     │ 3.26.0-r3         │ 3.28.0-r3     │ sqlite: malformed window-function query leads to DoS         │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2020-11655                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sqlite-libs  │ CVE-2019-16168 │ MEDIUM   │ 3.26.0-r3         │ 3.28.0-r1     │ sqlite: Division by zero in whereLoopAddBtreeIndex in        │
│              │                │          │                   │             
  │ sqlite3.c                                                    │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-16168                   │
├──────────────┼────────────────┼──────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sqlite-libs  │ CVE-2019-19242 │ MEDIUM   │ 3.26.0-r3         │ 3.28.0-r2     │ sqlite: SQL injection in sqlite3ExprCodeTarget in expr.c     │
│              │                │          │                   │             
  │ https://avd.aquasec.com/nvd/cve-2019-19242                   │
└──────────────┴────────────────┴──────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
2022-06-06T17:07:47.604Z        INFO    Table result includes only package filenames. Use '--format json' option to get the full path to the package file.

Python (python-pkg)
===================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 1, CRITICAL: 0)

┌────────────────┬────────────────┬──────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│    Library     │ Vulnerability  │ Severity │ Installed Version │ Fixed Version │                            Title                            │
├────────────────┼────────────────┼──────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ pip (METADATA) │ CVE-2019-20916 │ HIGH     │ 19.0.3            │ 19.2          │ python-pip: directory traversal in _download_http_url()     │
│                │                │          │                   │           
    │ function in src/pip/_internal/download.py                   │
│                │                │          │                   │           
    │ https://avd.aquasec.com/nvd/cve-2019-20916                  │
│                ├────────────────┼──────────┤                   ├───────────────┼─────────────────────────────────────────────────────────────┤
│                │ CVE-2021-3572  │ MEDIUM   │                   │ 21.1          │ python-pip: Incorrect handling of unicode separators in git │
│                │                │          │                   │               │ references                                                  │
│                │                │          │                   │               │ https://avd.aquasec.com/nvd/cve-2021-3572                   │
└────────────────┴────────────────┴──────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
hadi@LAPTOP-ADEE62RQ:/mnt/c/Users/hadij/Downloads/Devops/tp1$




