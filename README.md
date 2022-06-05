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



