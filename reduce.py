import os, json
import requests 
from bs4 import BeautifulSoup as bs 

jobj = {}
k = json.load(open("dataAll.json"))
for f in k["nodes"]:
    jobj[f["id"]] = []

for f in k["links"]:
    jobj[f["source"]].append(f["target"])

with open('dataAllReduced.json', 'w') as fp:
    json.dump(jobj, fp)
        
        
