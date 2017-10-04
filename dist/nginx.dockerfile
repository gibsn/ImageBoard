FROM nginx

EXPOSE 80 443

COPY dist/nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /usr/local/etc/certs/
COPY server.crt /usr/local/etc/certs/
COPY server.key /usr/local/etc/certs/
