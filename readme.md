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

## Script
El script sera basico para ver que funciona corremente.
~~~
print ("hola mundo")
~~~

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
        command: python
~~~
Y levantamos el docker.
