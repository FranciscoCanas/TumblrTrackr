#!/bin/sh

if test $# -ne 2
then
    echo "Usage: proftests.sh <host> <port>" >&2
    exit 1
fi

echo Sending requests to: ${1}:${2}

curl -X POST -d blog=fastcompany.tumblr.com http://${1}:${2}/blog
curl -X POST -d blog=theatlantic.tumblr.com http://${1}:${2}/blog
curl -X POST -d blog=condenasttraveler.tumblr.com http://${1}:${2}/blog
curl -X POST -d blog=thisistheverge.tumblr.com http://${1}:${2}/blog
curl -X POST -d blog=csc309woohoo.tumblr.com http://${1}:${2}/blog
curl -X POST -d blog=artgalleryofontario.tumblr.com http://${1}:${2}/blog
