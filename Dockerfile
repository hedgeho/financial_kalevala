FROM nginx:alpine
COPY ./kalevala_renpy-1.0-dists/kalevala_renpy-1.0-web /usr/share/nginx/html
EXPOSE 80
