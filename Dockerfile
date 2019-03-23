FROM alpine:latest

RUN apk update \
        && apk add --update nodejs nodejs-npm yarn zip unzip curl python3 python3-dev libffi libffi-dev bash gcc musl-dev openssl-dev make \
        && pip3 install pip pipenv awscli --upgrade \
        && yarn global add serverless

COPY . /code

RUN npm i --prefix /code

WORKDIR /code
