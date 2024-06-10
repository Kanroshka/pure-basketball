#!/bin/bash

if ! command -v docker &> /dev/null; then
    exit 1
fi

if [[ "$#" -ne 1 ]]; then
    echo "False"
    exit 1
fi

yml_file=$1

if [ ! -f $yml_file ]; then
    echo "False $yml_file"
    exit 1
fi

docker_image=$(cat $yml_file | yaml2json | jq -r '.image')
container_name=$(cat $yml_file | yaml2json | jq -r '.name')
port=$(cat $yml_file | yaml2json | jq -r '.port')
docker_args=$(cat $yml_file | yaml2json | jq -r '.docker_args')

docker run -d -p $port:80 --name $container_name $docker_image $docker_args

if [ "$(docker ps -q -f name=$container_name)" ]; then
    echo "True"
else
    echo "False"
    exit 1
fi

docker inspect $container_name
