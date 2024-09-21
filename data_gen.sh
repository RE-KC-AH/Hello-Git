#!/usr/bin/bash

i=1

declare -A name
nl_1=$(wc -l < ./last_name.txt)
nl_2=$(wc -l < ./first_name.txt)

while ((i<=10000))
do
       	last_name=$(sed -n "$(shuf -i 1-"$nl_1" -n 1)p" ./last_name.txt)
	first_name=$(sed -n "$(shuf -i 1-"$nl_2" -n 1)p" ./first_name.txt)
	full_name=${last_name}${first_name}
	if [[ -z ${name[${full_name}]} ]]
	then
		name[${full_name}]=1
		echo "${i}${full_name}"
		echo "${full_name}" > name.txt
		i=$((i+1))
	fi
done
echo "name.txt generated"

shuf -n 9990 name.txt > names_attend.txt
echo "names_attend.txt generated"
