# Orla Higgins, 2018-04-08
# Topic 5: Input and Output
# (using dataset iris.csv)

# kept getting IndexError: list index out of range, checked csv file and realised there were additional lines in iris.csv

# open, work with and close data set file
with open('data/iris.csv') as f:
    for line in f:

      # indent by 4 characters for each number, 
        print(line.split(',') [:4]) 

# result not quite right: ['5.1', '3.5', '1.4', '0.3']



# file: iris.csv http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

# open, work with and close data set file
with open("data/iris.csv") as f:

  for line in f:
    # character in the .csv file seperated by commas
    # split each individual line into number sets using line.split() function 
    # each number/item in set is defined as seperated by a comma
    a = line.split(',')

    # print the zeroth, first, second and third items on each line
    # no need to format indents or left leading as numbers are all one-digit number and one decimal placing
    print (a[0], a[1], a[2], a[3])


# Option 2
# Re: Wk5 Exercise Discussion by SARAH SCHOLZ - Saturday, 3 March 2018, 10:43 PM
# this works in aligning and spacing the numbers but requires alot of writing

# open, work with and close data set file
with open('data/iris.csv') as f:
    for line in f:

      # indent by 4 characters for each number, followed by .format 
      # each number/item in set is defined as seperated by a comma and the zeroth, first, second and third items on each line is printed
        print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))





