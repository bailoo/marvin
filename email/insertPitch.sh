#!/bin/bash

TOKEN=

for i in `cat shalini_final_dealId_notnull.csv | tr " " "#"`; 
do 
	pitch=`echo $i | awk -vFPAT='([^,]*)|("[^"]+")' -vOFS=, '{print $3}' | tr "#" " " | sed -e 's/\"//g'`; 
	deal=`echo $i | awk -vFPAT='([^,]*)|("[^"]+")' -vOFS=, '{print $4}'`;  
	curl -X PUT -d "00ad4eb98f63fbc58824c74cb67ffafefa51b41b=$pitch" https://api.pipedrive.com/v1/deals/$deal?api_token=$TOKEN; 
done

