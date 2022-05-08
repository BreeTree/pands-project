# Program to analyse the Iris flower dataset
# Author: Breeda Herlihy
# 2022-05-08

# Import relevant modules and libraries
from fileinput import filename
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in dataset and create a dataframe
filename = 'bezdekIris.data'
df = pd.read_csv(filename, names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])


# Outputs a summary of each variable to a single text file
f = open("summary.txt", "a")

print("Summary data for each variable\n", file=f)
print(df["sepal_length"].describe(), file=f)
print(df["sepal_width"].describe(), file=f)
print(df["petal_length"].describe(), file=f)
print(df["petal_width"].describe(), file=f)

print("Variables grouped by Iris species", file=f)
print(df[["sepal_length","species"]].groupby("species").describe(), file=f)
print(df[["sepal_width","species"]].groupby("species").describe(), file=f)
print(df[["petal_length","species"]].groupby("species").describe(), file=f)
print(df[["petal_width","species"]].groupby("species").describe(), file=f)

print("\nCorrelation Matrix for Iris dataset variables", file=f)
print(df.corr(), file=f)


# Outputs a histogram of each variable
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7) # configure plot appearance, grids, dotted lines, colour of lines and transparency
plt.grid() # set grid lines
ax = sns.histplot(data = df, # take values from data frame
                        x = "sepal_length", # set x-axis values
                         hue = "species", # group by species to give multiple plots on one histogram
                         kde = True, # include KDE analysis
                         bins = 25,  # number of bins
                         element = "bars") # style of histogram bins
ax.set_xlabel("Sepal length / cm", fontsize = 10) # set x-axis label
plt.title("Sepal length distribution of 3 Iris species", weight = "bold") # set plot title
plt.savefig("histogram_sepal_length.png") # save plot to a png file
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = df, 
                        x = "sepal_width", 
                         hue = "species", 
                         kde = True, 
                         bins = 25,  
                         element = "bars") 
ax.set_xlabel("Sepal width / cm", fontsize = 10)
plt.title("Sepal width distribution of 3 Iris species", weight = "bold")
plt.savefig("histogram_sepal_width.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = df,
                        x = "petal_length", 
                         hue = "species", 
                         kde = True, 
                         bins = 25, 
                         element = "bars") 
ax.set_xlabel("Petal length / cm", fontsize = 10)
plt.title("Petal length distribution of 3 Iris species", weight = "bold")
plt.savefig("histogram_petal_length.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = df, 
                        x = "petal_width", 
                         hue = "species", 
                         kde = True, 
                         bins = 25,  
                         element = "bars") 
ax.set_xlabel("Petal width / cm", fontsize = 10)
plt.title("Petal width distribution of 3 Iris species", weight = "bold")
plt.savefig("histogram_petal_width.png")
plt.show()


# Output scatterplots of each pair of variables
sns.set(style='whitegrid') # set style of the plot
sns.scatterplot(x="sepal_length", # set variable for x values
                y="sepal_width", # set variable for y values
                hue="species", # group by species
                data=df) # take data from dataframe
plt.title("Sepal length versus width for Iris species", weight = "bold") # set title of plot
plt.xlabel("Sepal length / cm", fontsize=8) # set x-axis label
plt.ylabel("Sepal width / cm", fontsize=8) # set y-axis label
plt.savefig("scatterplot_sepal_length_v_width.png") # save plot to a png file
plt.show()


sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
plt.title("Petal length versus width for Iris species", weight = "bold")
plt.xlabel("Petal length / cm", fontsize=8)
plt.ylabel("Petal width / cm", fontsize=8)
plt.savefig("scatterplot_petal_length_v_width.png")
plt.show()


'''
# Any other analyses
# heatmap of variables
iris = sns.load_dataset("iris")
sns.heatmap(iris.corr(),cmap = "YlGnBu", linecolor = 'white', linewidths = 1)

# Multivariate analysis of variables, pair plot of variable class (species)
# https://seaborn.pydata.org/tutorial/axis_grids.html
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
g = sns.pairplot(df,hue="class")

# Box plot 
# sns.boxplot(x='petal_length', y='petal_width', data=df)
# https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51

'''

