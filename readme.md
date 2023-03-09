## Fichero Python que se va a ejecutar con la imagen
Este es el codigo del script que vamos a ejecutar cuando levantemos el contenedor.
~~~
from pytube import YouTube

#link = input("Enter the link: ")
yt = YouTube("https://www.youtube.com/watch?v=htcVW-nLV7E&list=PL3qLpIJpAr6VoJYGeNNJ-whY_EY02bXt0")

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
~~~

## Creacion de la imagen
Creamos un fichero llamado Dockerfile en el meteremos lo que vamos a usar la nueva imagen
~~~
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
~~~
Con el comando Run instalamos lo que le indicamos en el fichero Requirements.txt
~~~
pytube==12.1.2
PyChromecast
~~~

Antes de todo esto creamos una carpeta donde almacenaremos el script llamada "app".

Despues, utilizamos el comando docker build -t "nombredelaimagen".

Y una vez creada la imagen, creamos el script y el docker-compose.yml

## Docker Compose
Creamos el docker y utilizaremos la imagen que creamos anteriormente .
~~~
version: '3.3'
services:
    python:
        container_name: ytproject
        volumes:
            - ./app:/usr/src/app
        image: youtubeimagen:chromecast
        stdin_open: true
        tty: true
        working_dir: /usr/src/app
        command: ["python","comprobacion.py"]
~~~
Y levantamos el docker.

## Enlace Docker Hub
https://hub.docker.com/repository/docker/adrirxguez/youtubeimage/general

