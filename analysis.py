# Program to analyse a dataset on Iris
# Author: Breeda Herlihy

# import relevant modules
import pandas as pd

# perform data analysis using (pandas) buit in statistical data
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
# output summary data in text file (pandas)
# output data in visual formats using Matplotlib / Seaborn
    # summary of each variable
    # histogram of each variable
    # scatter plot of each pair of variables
    # any other analyses
# https://medium.com/@siddhardhan23/data-visualization-in-python-a90ddb706b23 [Pair plot example, data visualisation, univariate, multivariate analysis]
# https://www.sisense.com/blog/data-visualizations-in-python-and-r/


# read in data from the file and create a dataframe
filename = 'irisdata.csv'
df = pd.read_csv(filename)
print(df)


filename = "iris.data"
def readText():
 with open(filename,"r") as f:
    chapter = str(f.read())
    return chapter
# test it
chapter = readText()

irisCount= readText().count("Iris")
print(irisCount)

#References

