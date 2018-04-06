#John O'Neill 06/04/2019! need u to work!!!

#import json
import csv #using reader function

#with open("Data/Iris.csv",'r',newline='') as f:
f = open("Data/Iris.csv",'r',newline='')
#reader = csv.reader(f) #reader function to parse data from the file
#for row in reader:
  #  print(row[0],row[1],row[2],row[3],row[4])
for line in f:
 # header = []
   PetalLength = float(line[1:4])
   PetalWidth= float(line[5:8])
   SepalLength= float(line[9:12])
   SepalWidth= float(line[13:16])
   # Description= str(line[18:50])

 # data.append([pl,pw,sl,sw])
print('{:5.1f}{:5.1f}{:5.1f}{:5.1f}'.format(PetalLength,PetalWidth,SepalLength,SepalWidth))
  



  
#list = int(line.split(','))
#for l in list:
 # print (list[0,1,2,4,5])
#