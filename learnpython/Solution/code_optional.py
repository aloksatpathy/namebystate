import glob
import os

curr_path = os.getcwd()  # setup of the present working directory

for eachfile in glob.glob('*.txt'):  # reading data files 
    with open(eachfile) as a:
        dbset = a.readlines()
        set1=[]
        set2=[]
        for eachline in dbset:      # breaking records seperated by comma
            x = eachline.split(",")
            if x[2]=="2013" and x[1]=='F': # condition to check for female names in 2013
                set1.append(x[3])
                set1.append(x[4])
            elif x[2]=="2013" and x[1]=='M': # condition to check for male names in 2013
                set2.append(x[3])
                set2.append(x[4])


total=0
b=['']*5
c=[0]*5
for m in range(0,len(set1),2):
        for n in range(0,len(set2),2):
                if set1[m]==set2[n]:   # ambiguity check for names belonging to both male and female
                    postn=c.index(min(c))
                    total=int(set1[m+1])+int(set2[n+1])
                    lowest=min(c)
                    if total>lowest:   # condition to replace the least greatest value
                                       # in the array with greater count value
                        c[postn]=total
                        b[postn]=set2[n]
print(b)