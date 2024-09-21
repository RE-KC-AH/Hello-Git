#!/usr/bin/bash

nl=1

mkdir winners_pic
while ((nl<=1000))
do
	name=$(sed -n "${nl}p" name.txt)
	cp ./*${name}.jpg ./winners_pic/
	nl=$((nl+1))
done
