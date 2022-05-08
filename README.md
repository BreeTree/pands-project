# pands-project
# Project for Programming and Scripting


## Data set
The data set is a collection of measurements of flower parts from 3 different Iris species: *Iris setosa*, *Iris versicolor* and *Iris virginica*. They were collected in the early twentieth century by Edgar Anderson, an American botanist in the Gaspé peninsula of Quebec and used by the British statistician Ronald A. Fisher to demonstrate his linear discriminant analysis method **[1]**.   
Anderson was interested in the evolution and taxonomic origins of various Iris species and Fisher was interested in “linear functions of the measurements by which the populations are best discriminated”.  The hypothesis for examining this dataset originally was that *Iris versicolor* arose from a combination of *Iris virginica* and *Iris setosa*. The Fisher paper considered whether “the mean value for *I. versicolor* takes an intermediate value, and, if so, whether it differs twice as much from *I. setosa* as from *I. virginica*, as might be expected, if the effects of genes are simply additive, in a hybrid between a diploid and a tetraploid species.” **[2]** While this proposal didn’t resolve as neatly as proposed, it has subsequently been proven via molecular and cytogenic tools that *Iris virginica* and *Iris setosa* are the progenitors of *Iris versicolor*.**[3]**   
For this project, the data set is examined to review the data and to establish whether the morphological features can be used to distinguish between the species using quantitative analyses. Plant identification and classification does not rely on flower parts alone as highlighted by Anderson. **[4]** From the perspective of plant breeding for modern agriculture, however, the statistical tools developed by Fisher such as linear regression and ANOVA have been an integral part of the advances in crop breeding.  
This project uses the Fisher Iris flower dataset archived by the UC Irvine Machine Learning Repository and licensed for reuse through CC-BY. **[5]** The original dataset was found to have a number of errors and has been updated by Bezdek *et al*. **[6]** bezdekIris.data was the dataset used for this project. The data has 50 measurements related to petal and sepal size for each species and these are analysed and plotted using the Python programming language. 

## How to use
The program analysis.py was created using the Python programming language in Visual Studio and the Anaconda environment. It can be run in a variety of ways depending on your set up. The various methods are outlined [here](https://realpython.com/run-python-scripts/#:~:text=To%20run%20Python%20scripts%20with,python3%20hello.py%20Hello%20World!) 


## Analysis
The program is used to analyse the Iris data set, output data to a text file and generate plots. 

### Import additional modules and libraries
Additional modules and libraries are imported to support [file output](https://docs.python.org/3/library/fileinput.html), [data analysis](https://pandas.pydata.org/), [plotting] (https://matplotlib.org/) and [data visualization](https://seaborn.pydata.org/) in Python. 

'''
from fileinput import filename
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
'''

output data perform data analysis using (pandas) built in statistical data
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

### Read in data

### Analyse each variable

### Output summary data to a text file
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
# correlation matrix https://www.geeksforgeeks.org/how-to-create-a-correlation-matrix-using-pandas/#:~:text=variables%20are%20related.-,Pandas%20dataframe.,na%20values%20are%20automatically%20excluded. 
# https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time

# https://pandas.pydata.org/docs/user_guide/style.html# Table Visualisation - consider
# https://pandas.pydata.org/docs/user_guide/basics.html#sorting sorting results
# https://pandas.pydata.org/docs/user_guide/reshaping.html pivot tables



### Output histograms
# https://realpython.com/python-histograms/
# https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib
# seaborn histogram
# https://stackoverflow.com/questions/36362624/how-to-plot-multiple-histograms-on-same-plot-with-seaborn
# bin size https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot
# graph subtitle https://stackoverflow.com/questions/1388450/giving-graphs-a-subtitle-in-matplotlib 
# save the plots # https://www.geeksforgeeks.org/matplotlib-pyplot-savefig-in-python/ 


### Output scatterplots
# seaborn scatter plots
# https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/


### Any other analyses
Multivariate analysis of variables, pair plot of variable class (species)
# https://seaborn.pydata.org/tutorial/axis_grids.html
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 

## References 
**[1]** Wikipedia (2022) Iris flower data set - Wikipedia. Available at: https://en.wikipedia.org/wiki/Iris_flower_data_set  (Accessed: 30/04/2022)   
**[2]** Fisher, R.A. (1936), The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7: 179-188. https://doi.org/10.1111/j.1469-1809.1936.tb02137.x  
**[3]** Lim KY, Matyasek R, Kovarik A, Leitch A. (2007) Parental origin and genome evolution in the allopolyploid Iris versicolor. Ann Bot.;100(2):219-24. doi: https://doi.org/10.1093/aob/mcm116.  
**[4]** Anderson, E. (1936). The Species Problem in Iris. Annals of the Missouri Botanical Garden, 23(3), 457–509. https://doi.org/10.2307/2394164  
**[5]** Fisher, R.A.. (1988). Iris. UCI Machine Learning Repository. https://archive-beta.ics.uci.edu/ml/datasets/iris   
**[6]** J. C. Bezdek, J. M. Keller, R. Krishnapuram, L. I. Kuncheva and N. R. Pal, "Will the real iris data please stand up?," in IEEE Transactions on Fuzzy Systems, vol. 7, no. 3, pp. 368-369, June 1999, doi: https://doi.org/10.1109/91.771092.  

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

