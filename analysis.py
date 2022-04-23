# Program to analyse a dataset on Iris
# Author: Breeda Herlihy

# import relevant modules
from fileinput import filename
import numpy as np
import pandas as pd
from regex import F
import seaborn as sns
import matplotlib.pyplot as plt

# perform data analysis using (pandas) buit in statistical data
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
# output summary data in text file (pandas)
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
    # summary of each variable
# output data in visual formats using Matplotlib / Seaborn
    # histogram of each variable
    # scatter plot of each pair of variables
    # any other analyses
# https://medium.com/@siddhardhan23/data-visualization-in-python-a90ddb706b23 [Pair plot example, data visualisation, univariate, multivariate analysis]
# https://www.sisense.com/blog/data-visualizations-in-python-and-r/


# read in data from the file and create a dataframe
filename = 'iris.data'
df = pd.read_csv(filename, names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])


# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
f = open("summary.txt", "a")
#print(df.head(5), file=f)
#print(df.tail(5), file=f)
#print(df.columns, file=f)
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

print(df["sepal_length"].describe(), file=f)
print(df["sepal_width"].describe(), file=f)
print(df["petal_length"].describe(), file=f)
print(df["petal_width"].describe(), file=f)
print(df[["sepal_length","species"]].groupby("species").describe(), file=f)
print(df[["sepal_width","species"]].groupby("species").describe(), file=f)
print(df[["petal_length","species"]].groupby("species").describe(), file=f)
print(df[["petal_width","species"]].groupby("species").describe(), file=f)

f.close()


# Summary of each variable 
'''
print(df["sepal_length"].describe(), file=f)
print(df["sepal_width"].describe(), file=f)
print(df["petal_length"].describe(), file=f)
print(df["petal_width"].describe(), file=f)

'''


#a_dataframe = df.head(5)
#numpy_array = a_dataframe.to_numpy()
#np.savetxt("test_file.txt",numpy_array, fmt = "%s")
#https://www.adamsmith.haus/python/answers/how-to-write-contents-of-a-dataframe-into-a-text-file-in-python
# top 5 rows of df
# print(df.head(5))
# random sample of 10 rows
# print(df.sample(10))
# list the column headers and data types
# print(df.columns)
# list the number of rows and number of columns
# print(df.shape)
# slice data e.g. for one species
# print(df[100:150])
# use loc and iloc to display specific rows
# print(df.iloc[2])
# return data where the species matches the str
# print(df.loc[df['class'] == "Iris-virginica"])
# 
# print(df["class"].value_counts())

'''
# Any other analyses
# heatmap of variables
iris = sns.load_dataset("iris")
sns.heatmap(iris.corr(),cmap = "YlGnBu", linecolor = 'white', linewidths = 1)

# Multivariate analysis of variables, pair plot of variable class (species)
# https://seaborn.pydata.org/tutorial/axis_grids.html
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
g = sns.pairplot(df,hue="class")
plt.show()


filename = "iris.data"
def readText():
 with open(filename,"r") as f:
    chapter = str(f.read())
    return chapter
# test it
chapter = readText()

irisCount= readText().count("Iris")
print(irisCount)
'''

#References
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
