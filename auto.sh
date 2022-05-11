#!/bin/bash

original="locations-nz.txt"
input="locations-nz-copy.txt"

if [[ -f "$input" ]]
then
  cd weekly
  last_file=$(ls | sort -V | tail -n 1)
  cd ..
  now=${last_file:0:10}
else
  cp "$original" "$input"
  now=$(date +'%Y-%m-%d')
fi

while IFS= read -r line
do
  echo "$line"
  scrapy crawl airbnb -a query="$line, New Zealand" -o "weekly/$now-nz.xlsx"
  sed -i "1d" "$input"
done < "$input"

rm "$input"

python photo.py
