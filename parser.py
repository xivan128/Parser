from urllib.request import urlopen
from xml.dom import minidom

f=open('file.txt','r')
for line in f:
 line=line[:len(line)-1]
 p=open('out/'+line,'wb')
 print(line)
 url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term='+line
 xmldoc = minidom.parseString(urlopen(url).read())
 id = xmldoc.getElementsByTagName('Id')[0].firstChild.data
 print(id)
 url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=nuccore&report=fasta&id='+id
 p.write(urlopen(url).read())
 p.close()