#!/bin/bash

mkdir newdirectory

for file in .txt; do
    cp "$file" $1
done

cd $1

for file in .txt; do
    mv "$file" "new$file"
done
