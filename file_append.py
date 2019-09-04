import os
import csv
path  = "your path"
with open('filename.csv','w') as writefile:
    writer = csv.writer(writefile)
    for root,dirs,files in os.walk(path):
        for name in files:
            columns = [c.strip() for c in name.strip('_').split('_')]