#John O'Neill Iris formatting file 24/03/18

#Iris data set prints the four numerical values on each 
#row in a nice format. That is, on the screen should
# be printed the petal length, petal width, sepal length 
# and sepal width, and these values should have the
# decimal places aligned, with a space between the columns

#NB "Read" the file... print (file.read())

#with open("Data/iris.csv.txt") as openedfile:
    #for x in range(1,12):
measures = ['PetalLength', '1','PetalWidth', '2']
output = 'see {0[0]}{0[2]}'.format(measures) 
#https://www.youtube.com/watch?v=vTX3IwquFkc (String Format Tutorial)
print(output)

    #"with" opens and closes file when finished
   # for x in openedfile[0,16]:
    #    print(repr(x).rjust(3), end='')
   # print(openedfile.read())
   # for line in openedfile:
    #    print(line.split(",")[0])
    #    '{}{}{}'.format('5''6''11')


