#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import requests

API_UNI = "http://universities.hipolabs.com"

countries = [
    "Poland", 
    "Spain", 
    "Italy",
    "Canada", 
    "Finland", 
    "Greece",
    "Japan",
    "Germany", 
    "India", 
    "Norway", 
    "Ukraine", 
    "Netherlands", 
    "Turkey", 
    "Sweden",
    "Portugal"
]

def get_universities(country, result):
    api_url = f"{API_UNI}/search?country={country}"
    response = requests.get(api_url)
    
    if response.ok:
        university_names = [university['name'] for university in response.json()]
        result[country] = university_names
    else:
        result[country] = []

results = {}
threads = []

for country in countries:
    thread = threading.Thread(target=get_universities, args=(country, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(results)
