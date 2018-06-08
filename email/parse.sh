#!/bin/bash

for i in `ls *.eml`; 
do 
	email=`grep -m 1 "To: \'*@*.*\'" $i`; 
	artist=`grep -E "https?://starclinch.com/\/*" $i | grep -v href | grep -v emi-pe-ent | grep -v book\/form`; 
	artist1=`echo $artist | tr "\n" " "`; 
	echo $i,"$email","$artist1"; 
done > shambhavi.csv

grep -v subscription.html shambhavi.csv > foo

for i in `cat foo`; 
do 
	eml=`echo $i | cut -d "," -f 1`; 
	email=`echo $i | cut -d "," -f 2`; 
	artist=`echo $i | cut -d "," -f 3 | tr "#" " "`; 
	pitch=''; 
	for j in `echo $artist`; 
	do 
		temp=`echo $j | grep https`; pitch=$pitch" "$temp; 
	done; 
	p1=`echo $pitch | tr " " "\n" | sort | uniq | tr "\n" ","`; 
	echo $eml,$email,\"$p1\"; 
done > prasanta_final.csv

