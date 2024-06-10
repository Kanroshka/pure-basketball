#!/bin/bash

if ! command -v docker &> /dev/null; then
    exit 1
fi

if [[ "$#" -ne 3 ]]; then
    echo "False"
    exit 1
fi

docker_image=$1
container_name=$2
port=$3

docker run -d -p $port:80 --name $container_name $docker_image

# Проверяем, успешно ли запщен контейнер
if [ "$(docker ps -q -f name=$container_name)" ]; then
    echo "True"
else
    echo "False"
    exit 1
fi

docker inspect $container_name
