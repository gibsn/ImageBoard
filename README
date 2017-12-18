Tools

Python3
Django
Gunicorn
Nginx
Docker


Deployment

Use the provided deploy.sh.

It will install:
1) docker
2) docker-compose
3) python (needed to generate django secret key)

It will:
1) install all the needed tools
2) generate certificates for nginx
3) build docker images from source
4) generate django secret key
5) generate config for django
6) initialise django
7) launch the whole service as a set of docker containers

It will prompt for:
1) mailer password
2) creation of django superuser

ImageBoard is available at ports 80 and 443 (actually 80 will redirect to 443)
