#John O'Neill Iris formatting file 24/03/18

#Iris data set prints the four numerical values on each 
#row in a nice format. That is, on the screen should
# be printed the petal length, petal width, sepal length 
# and sepal width, and these values should have the
# decimal places aligned, with a space between the columns

#NB "Read" the file... print (file.read())

 #"with" opens and closes file when finished
with open("Data/iris.csv.txt") as openedfile:
    for line in openedfile:
        print (line.split(','), end ='')
        
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


