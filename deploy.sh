#!/bin/bash

# installing docker
if [ `uname` == "Linux" ]; then
    sudo apt-get update -q
    sudo apt-get install -y -q \
        apt-transport-https \
        ca-certificates \
        software-properties-common \
        curl

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"

    sudo apt-get update -q
    sudo apt-get install -y -q docker-ce

    sudo docker run hello-world || exit

    which docker-compose || sudo curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo docker-compose --version || exit

    sudo apt install -y -q python || exit
fi

# generating selfsigned ssl certificates
if [ ! -f certs/server.key ] || [ ! -f certs/server.crt ]; then
    mkdir certs
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -subj "/C=US" \
        -keyout certs/server.key -out certs/server.crt || exit
fi

# building docker images from source
sudo docker build ./ -f dist/imageboard.dockerfile -t gibsn/imageboard || exit
sudo docker build ./ -f dist/nginx.dockerfile -t gibsn/nginx || exit

# making imageboard config
secret_key=$(python -c "import string,random; uni=string.ascii_letters+string.digits; print ''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45,50))])")

email="imageboardmailer@mail.ru"
echo "password for $email:"
read password

cat > _cfg.json << EOM
{
    "debug": true,
    "allowed_hosts": ["127.0.0.1"],

    "messages_per_page": 5,

    "secret_key": "$secret_key",
    "token_timeout_days": 1,

    "email_host": "smtp.mail.ru",
    "email_port": 465,
    "email_host_user": "$email",
    "email_host_password": "$password",

    "static_url": "/static/",
    "static_root": "static",

    "media_url": "/media/",
    "media_root": "media"
}
EOM

# launching services
sudo docker-compose -f dist/docker-compose.yml up -d || exit

sudo docker exec -u root -it imageboard python manage.py collectstatic --noinput || exit
sudo docker exec -u root -it imageboard python manage.py makemigrations board users || exit
sudo docker exec -u root -it imageboard python manage.py migrate

sudo docker exec -u root -it imageboard chown imageboard:imageboard media || exit

echo "gonna create a superuser"
sudo docker exec -u root -it imageboard python manage.py createsuperuser || exit

echo "done"
