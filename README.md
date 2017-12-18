# ImageBoard

Simple imageboard implemented with Python 3 and Django.

## Tools

1) Python3
2) Django
3) Gunicorn
4) Nginx
5) Docker


## Deployment

The provided deploy.sh is intended for a clean Ubuntu Server 16.04.3 LTS.

It will:
1) install all the needed tools
2) generate certificates for nginx
3) build docker images from source
4) generate django secret key
5) generate config for django
6) initialise django
7) launch the whole service as a set of docker containers

It will install:
1) docker
2) docker-compose
3) python (needed to generate django secret key)

It will prompt for:
1) server name
2) mailer password 
3) creation of django superuser

ImageBoard is available at ports 80 and 443 (actually 80 will redirect to 443)
