# Program to analyse a dataset on Iris
# Author: Breeda Herlihy

# import relevant modules and libraries

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

'''
#a_dataframe = df.head(5)
#numpy_array = a_dataframe.to_numpy()
#np.savetxt("test_file.txt",numpy_array, fmt = "%s")
#
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
# print(df.loc[df['species'] == "Iris-virginica"])
# print(df["species"].value_counts())



# plot histograms


# pandas histogram
df['sepal_length'].hist(by=df['species'])
df.hist(column="sepal_length", by="species", grid=True, bins=10, legend=True)
df.hist(column="sepal_width", by="species", grid=True, bins=10, legend=True)
df.hist(column="petal_length", by="species", grid=True, bins=10, legend=True)
df.hist(column="petal_width", by="species", grid=True, bins=10, legend=True)


# matplotlib histogram cannot use objects
iris_vi = df.loc[df['species'] == "Iris-virginica"]
iris_se = df.loc[df['species'] == "Iris-secosa"]
width = 0.5  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(iris_vi, width, label='Iris-virginica')
rects2 = ax.bar(iris_se, width, label='Iris-secosa')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('count')
ax.set_title('Petal Length by Species')

ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
'''

''''
#seaborn histogram
# https://stackoverflow.com/questions/36362624/how-to-plot-multiple-histograms-on-same-plot-with-seaborn
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = df, x = "sepal_length", 
                         hue = "species", 
                         kde = True, 
                         bins = 25,  # https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot
                         element = "bars") 
ax.set_xlabel("Sepal length / cm", fontsize = 10)

plt.title("Sepal length distribution of 3 Iris species", weight = "bold")
plt.savefig("histogram_sepal_length.png")
plt.show()

# Scatter plots
sns.set(style='whitegrid')
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df)
plt.title("Sepal length versus width for Iris species", weight = "bold")
plt.xlabel("Sepal length / cm", fontsize=8)
plt.ylabel("Sepal width / cm", fontsize=8)
plt.savefig("scatterplot_sepal_length_v_width.png")
plt.show()

#sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
#plt.savefig("scatterplot_petal_length_v_width.png")
plt.show()

'''



'''
# Any other analyses
# heatmap of variables
iris = sns.load_dataset("iris")
sns.heatmap(iris.corr(),cmap = "YlGnBu", linecolor = 'white', linewidths = 1)

# Multivariate analysis of variables, pair plot of variable class (species)
# https://seaborn.pydata.org/tutorial/axis_grids.html
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
g = sns.pairplot(df,hue="class")
'''



