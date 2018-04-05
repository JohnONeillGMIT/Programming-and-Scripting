#John O'Neill Iris formatting file 24/03/18

#Iris data set prints the four numerical values on each 
#row in a nice format. That is, on the screen should
# be printed the petal length, petal width, sepal length 
# and sepal width, and these values should have the
# decimal places aligned, with a space between the columns

#NB "Read" the file... print (file.read())
#need u to work!!!

import json
import csv

f = open("Data/Iris.csv.txt",newline='')
reader =csv.reader(f) #reader function to parse data from the file

#insert headers

data=[]
for row in reader:
  print(row[0],row[1],row[2],row[3],row[4])
 #for line in f:
  #line.split(',')
  #print(line)#need to convert thestring to alist

#list = int(line.split(','))
#for l in list:
 # print (list[0,1,2,4,5])
 #"with" opens and closes file when finished
#with open("Data/iris.csv.txt") as f:
  #  for line in f:
    #   print (line.split(',')([0])
        #line.split(',')
        

        #Line split breaks up a string and used the 
        #defined seaparator "," in this case placed between each variable
        #  http://www.pythonforbeginners.com/dictionary/python-split
   
        
        #output = '{0[:4.2f]}{1[:4.3f]}'
       # print(output)
    

#measures = ['PetalLength', 'PetalWidth','SepalLength','SepalWidth']
#output = '{0[1]}{0[2]}'.format(measures) 
#https://www.youtube.com/watch?v=vTX3IwquFkc (String Format Tutorial)
#print(output)

    
   # for x in openedfile[0,16]:
    #    print(repr(x).rjust(3), end='')
   # print(openedfile.read())
   # for line in openedfile:
    #    print(line.split(",")[0])
    #    '{}{}{}'.format('5''6''11')