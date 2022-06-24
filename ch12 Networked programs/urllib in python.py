from itertools import count
import urllib.request, urllib.parse, urllib.error

fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())


fhand1= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand1:
    words=line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)
