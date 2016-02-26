import urllib.request
import zipfile
import glob
import os

path = os.getcwd()
url = 'http://www.ssa.gov/oact/babynames/state/namesbystate.zip'

data=urllib.request.urlretrieve(url, "data.zip")

fh = open('data.zip', 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = path
    z.extract(name, outpath)

for filename in glob.glob('*.txt'):
    with open(filename) as f:
        data = f.readlines()
        x=0
        for line in data:
            words = line.split(",")
            if int(x)<int(words[4]):
                x=words[4]
                y=words[3]
print(y)