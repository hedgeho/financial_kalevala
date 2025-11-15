FROM nginx:alpine
COPY ./-dists/-web /usr/share/nginx/html
EXPOSE 80
