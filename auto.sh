#!/bin/bash
input="towns.txt"
now=$(date +'%Y-%m-%d')
while IFS= read -r line
do
  echo "$line"
  scrapy crawl airbnb -a query="$line, Australia" -o "weekly/australia-$now.csv" -t headless
done < "$input"
python photo.py
