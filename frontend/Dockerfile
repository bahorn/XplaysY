FROM node:latest as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./app/package.json ./
COPY ./app/package-lock.json ./
RUN npm ci
RUN npm install react-scripts -g --silent
COPY app ./
RUN npm run build

FROM nginx:latest
COPY --from=build /app/build /usr/share/nginx/html
COPY ./nginx/mime.types /etc/nginx/conf/mime.types
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
