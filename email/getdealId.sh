#!/bin/bash

TOKEN=

num=0
rm -f shalini_final_dealId.csv
for i in `cat bar`
do
	num=`expr $num + 1`
	email=`echo $i | cut -d "," -f 2 | cut -d ";" -f 1`
	rm -f res.json
	curl --silent "https://api.pipedrive.com/v1/searchResults?term=$email&start=0&api_token=$TOKEN" > res.json
	dealId=`jq '.data[1].id' res.json`
	echo $i,$dealId >> shalini_final_dealId.csv
	echo $num
done
