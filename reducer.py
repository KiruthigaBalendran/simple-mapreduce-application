#!/usr/bin/python
#Reducer.py
import sys

country_product = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    country, product = line.split('\t')

    if country in country_product:
        country_product[country].append(str(product))
    else:
        country_product[country] = []
        country_product[country].append(str(product))

#Reducer
for country in country_product.keys():
    sum_product = len(country_product[country])
    print(country +'\t' + str(sum_product))
