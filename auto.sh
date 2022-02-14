#!/bin/bash
input="towns.txt"
while IFS= read -r line
do
  echo "$line"
  scrapy crawl airbnb -a query="$line, Australia" -o "towns/$line.csv"
done < "$input"
