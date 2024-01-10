#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static. It must

if [ ! -d data ]; then
    mkdir data
fi
if [ ! -d data/web_static ]; then
    mkdir data/web_static
fi
if [ ! -d data/web_static/releases ]; then
    mkdir data/web_static/releases
fi
if [ ! -d data/web_static/shared ]; then
    mkdir data/web_static/shared
fi
if [ ! -d data/web_static/releases/test ]; then
    mkdir data/web_static/releases/test
fi
if [ ! -d data/web_static/releases/test/index.html ]; then
    touch data/web_static/releases/test/index.html
    echo "Holberton School" > data/web_static/releases/test/index.html
fi