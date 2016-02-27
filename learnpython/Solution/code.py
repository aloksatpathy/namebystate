import urllib.request
import zipfile
import glob
import os

curr_pwd = os.getcwd()
url = 'http://www.ssa.gov/oact/babynames/state/namesbystate.zip'

print("Downloading file")
dbset=urllib.request.urlretrieve(url, "dbset.zip") # downloading the file from given url

print("Extracting file")
# extracting the downloaded file
x = open('dbset.zip', 'rb')
y = zipfile.ZipFile(x)
for t in y.namelist():
    newpath = curr_pwd
    y.extract(t, newpath)

print("Calculating Highest Occurence of name")
for eachfile in glob.glob('*.txt'):  # for each data file
    with open(eachfile) as k:
        db = k.readlines()
        a=0
        for eachline in db: 
            parts = eachline.split(",") # break the file and implement condition to check the highest count value for the name
            if int(a)<int(parts[4]):
                m=parts[4]
                n=parts[3]
print("Most popular name of all time in US: ",n)