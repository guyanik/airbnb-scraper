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

# increment=50

# for i in `seq 0 $increment 1000`
# do
#   echo "price range: $i - $(($i+$increment))"
#   scrapy crawl airbnb -a query="Rotorua District, New Zealand" -a min_price=$i -a max_price=$(($i+$increment)) -o "weekly/rotorua-nz.xlsx"
# done
# scrapy crawl airbnb -a query="Rotorua District, New Zealand" -a min_price=1000 -o "weekly/rotorua-nz.xlsx"
