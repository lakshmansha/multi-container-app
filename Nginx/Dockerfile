FROM nginx:1.15.8-alpine
#configuration
COPY ./nginx.conf /etc/nginx/nginx.conf
#content, comment out the ones you dont need!
COPY ./*.html /usr/share/nginx/html/
#COPY ./*.css /usr/share/nginx/html/
#COPY ./*.png /usr/share/nginx/html/
#COPY ./*.js /usr/share/nginx/html/

WORKDIR /app

EXPOSE 80

USER root

CMD ["nginx", "-g", "daemon off;"]