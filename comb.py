import os, json
import requests 
from bs4 import BeautifulSoup as bs 

jobj = { "nodes" : [], "links" : []}
k = os.listdir("./pages/")
for f in k:
    jobj["nodes"].append({"id" : f, "name" : f, "val" : 1})
    s = bs(open(f"./pages/{f}","r").read().rstrip())
    ws = s.select('a') 
    try:
        all = [w['href'] for w in ws] 
    except:
        continue
    c = 0
    for l in all:
        if c >= 5:
            break;
        if "/diff/" in l or "HomePage" in l:
            continue
        if "/nlab/show/" in l:
            p = l.split("/")[3]
            if(p not in [x["name"] for x in jobj["nodes"]]):
                jobj["nodes"].append({"id" : p, "name" : p, "val" : 1})

            jobj["links"].append({"source" : f, "target" : p})
            print(f"added edge {f} to {p}")
            c += 1
    print(100*(k.index(f) + 1)/len(k), len(jobj["nodes"]), len(jobj["links"]))

with open('data5.json', 'w') as fp:
    json.dump(jobj, fp)
        
        
