#!/usr/bin/bash

i=1
sum=0
ave=0

echo -e "输入文件名：\c"
read file

nl=$(wc -l < ${file})

while ((i<=nl))
do
    sum=$((sum+$(sed -n "${i}p" ${file})))
    i=$((i+1))
done

echo "和：${sum}"
ave=$((sum/nl))
echo "平均值：${ave}"

echo { > output.json
echo "	"sum":$sum" >> output.json
echo "	"average":$ave" >> output.json
echo } >> output.json

echo 已经写入"output.json"，内容如下
cat output.json
