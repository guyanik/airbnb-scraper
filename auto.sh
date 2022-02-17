#!/bin/bash
input="towns.txt"
now=$(date +'%Y-%m-%d')

scrapy crawl airbnb -a query="Abercrombie Caves, NSW, Australia" -o "weekly/australia-$now.csv" -t headless
python photo.py
