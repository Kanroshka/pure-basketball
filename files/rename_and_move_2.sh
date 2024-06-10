#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory_name> <file_extension>"
    exit 1
fi

directory_name=$1
file_extension=$2
count=1

if [ ! -d "$directory_name" ]; then
    mkdir "$directory_name"
fi

for file in *.$file_extension; do
    cp "$file" "$directory_name/"
done

cd "$directory_name"

for file in *.$file_extension; do
    new_filename="new_${count}_$file"
    mv "$file" "$new_filename"
    ((count++))
done
