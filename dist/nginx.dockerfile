FROM nginx

EXPOSE 80 443

COPY dist/nginx.conf /etc/nginx/nginx.conf
