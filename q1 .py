
#   "C:\Users\kaval\OneDrive\Desktop\Assignments\Assignment Datasets\Statistical Datasets\Q1_a.csv"


import pandas as pd

# Read data into Python
df= pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\Assignments\Assignment Datasets\Statistical Datasets\Q1_a.csv")

df.info()

# C:\Users\education.csv - this is windows default file path with a '\'
# C:\\Users\\education.csv - change it to '\\' to make it work in Python

# Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
df.speed.mean() # '.' is used to refer to the variables within object
df.speed.median()
df.speed.mode()

df.dist.mean()
df.dist.median()
df.dist.mode()


# pip install numpy
from scipy import stats
stats.mode(df.speed)
stats.mode(df.dist)

# Measures of Dispersion / Second moment business decision 
# for speed
df.speed.var() # variance
df.speed.std() # standard deviation
range = max(df.speed) - min(df.speed) # range
range
#   For distance
df.dist.var() # variance
df.dist.std() # standard deviation
range = max(df.dist) - min(df.dist) # range
range

# Third moment business decision
df.speed.skew()
df. dist .skew()

# Fourth moment business decision
df.speed.kurt()
df.dist.kurt()

# Data Visualization
import matplotlib.pyplot as plt
import numpy as np

df.shape

plt.bar(height = df. dist , x = np.arange(1,51,1)) # initializing the parameter
plt.bar(height = df. speed , x = np.arange(1,51,1)) 

plt.hist(df. dist ) #histogram
plt.hist(df.speed, color='red')



plt.boxplot(df. dist ) #boxplot
plt.boxplot(df.speed) #boxplot
