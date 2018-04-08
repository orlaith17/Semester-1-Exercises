# Orla Higgins, 2018-04-08
# Topic 5: Input and Output
# (using dataset iris.csv)

# kept getting IndexError: list index out of range, checked csv file and realised there were additional lines


# Re: Wk5 Exercise Discussion by SARAH SCHOLZ - Saturday, 3 March 2018, 10:43 PM



#Hi Gregory, 
#I found the easiest way for me was to split the columns as you mention and apply a format to each column separately, maybe it helps: 

#for line in f:
#print('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))

# :5 assigns 5 spaces to the column but you could just as well add commas etc between every column, e.g. between every {} and format whichever looks best to you. 

#Best,
#Sarah

#Hi All,

#I was able to get as far as Noa with her original post and understand splitting the columns of data. I also understand some parts of the format function in relation to a string. I can't yet marry the two together to format the output from the file. I can see from Ians link  how the numbers are formatted from a string but dont know how to get this result from the csv file.

#Thanks,

#Greg.


with open("data/iris.csv") as f:
  for line in f:
    a = line.split(',')
    print (a[0], a[1], a[2], a[3])



#with open('data/iris.csv') as f:
    #for line in f:
  #      print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))

