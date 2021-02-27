import csv,os,re
with open(os.environ.get('ticker','ticker.csv')) as csv_file: 
    csv_reader = list(csv.DictReader(csv_file))

def ticker(nameofcompany):
    return [ c for c  in csv_reader if  re.match(nameofcompany,c['NAME OF COMPANY'],re.IGNORECASE)]