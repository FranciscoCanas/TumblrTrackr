#!/bin/sh

BASEURL="http://127.0.0.1:30945"
testfile="testurls"

exec<$testfile

while read curline
do
	echo $BASEURL$curline
	wget -q --spider $BASEURL$curline
done
