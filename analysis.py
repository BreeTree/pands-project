# Program to analyse a dataset on Iris
# Author: Breeda Herlihy

# import relevant modules

from fileinput import filename
import pandas as pd
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

# plot histograms
# https://realpython.com/python-histograms/
# https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib
'''
# pandas histogram
df['sepal_length'].hist(by=df['species'])
df.hist(column="sepal_length", by="species", grid=True, bins=10, legend=True)
df.hist(column="sepal_width", by="species", grid=True, bins=10, legend=True)
df.hist(column="petal_length", by="species", grid=True, bins=10, legend=True)
df.hist(column="petal_width", by="species", grid=True, bins=10, legend=True)
'''
'''
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

'''
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
# https://stackoverflow.com/questions/1388450/giving-graphs-a-subtitle-in-matplotlib 
plt.title("Sepal length distribution of 3 Iris species", weight = "bold")
# https://www.geeksforgeeks.org/matplotlib-pyplot-savefig-in-python/
plt.savefig("histogram_sepal_length.png")
plt.show()
'''
#seaborn scatter plots
# https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/
sns.set(style='whitegrid')
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df)
plt.title("Sepal length versus width for Iris species", weight = "bold")
plt.xlabel("Sepal length / cm", fontsize=8)
plt.ylabel("Sepal width / cm", fontsize=8)
plt.savefig("scatterplot_sepal_length_v_width.png")
#plt.show()

#sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
#plt.savefig("scatterplot_petal_length_v_width.png")
#plt.show()

'''
# Summary of each variable 
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
f = open("summary.txt", "a")

#https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
print(df["sepal_length"].describe(), file=f)
print(df["sepal_width"].describe(), file=f)
print(df["petal_length"].describe(), file=f)
print(df["petal_width"].describe(), file=f)

print("Variables grouped by Species", file=f)
print(df[["sepal_length","species"]].groupby("species").describe(), file=f)
print(df[["sepal_width","species"]].groupby("species").describe(), file=f)
print(df[["petal_length","species"]].groupby("species").describe(), file=f)
print(df[["petal_width","species"]].groupby("species").describe(), file=f)
https://www.geeksforgeeks.org/how-to-create-a-correlation-matrix-using-pandas/#:~:text=variables%20are%20related.-,Pandas%20dataframe.,na%20values%20are%20automatically%20excluded.
print("Correlation Matrix for Iris dataset variables", file=f)
print(df.corr(), file=f)

f.close()
# https://pandas.pydata.org/docs/user_guide/style.html# Table Visualisation - consider
# https://pandas.pydata.org/docs/user_guide/basics.html#sorting sorting results
# https://pandas.pydata.org/docs/user_guide/reshaping.html pivot tables

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
# print(df.loc[df['species'] == "Iris-virginica"])
# print(df["species"].value_counts())




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

#plt.show()

#References
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
