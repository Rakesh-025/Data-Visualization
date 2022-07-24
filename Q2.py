#  SPEED AND WEIGHT
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Read data into Python
df= pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\Q2_b.csv")
df.info()


### Exploratory Data Analysis FOR SPEED  ###

# Measures of Central Tendency / First moment business decision
df.SP.mean() # '.' is used to refer to the variables within object
df.SP.median()
df.SP.mode()

stats.mode(df.SP)


# Measures of Dispersion / Second moment business decision 
df.SP.var() # variance
df.SP.std() # standard deviation
range = max(df.SP) - min(df.SP) # range
range


# Third moment business decision
df.SP.skew()

# Fourth moment business decision
df.SP.kurt()

# Data Visualization

df.shape

plt.bar(height = df. SP , x = np.arange(1,82,1)) # initializing the parameter

plt.hist(df. SP ) #histogram

plt.boxplot(df. SP ) #boxplot

# EDA  FOR WEIGHT

df.WT.mean()
df.WT.median()
df.WT.mode()

stats.mode(df.WT)

df.WT.var() # variance
df.WT.std() # standard deviation
range = max(df.WT) - min(df.WT) # range
range

# Third moment business decision
df. WT .skew()

# Fourth moment business decision
df.WT.kurt()

# Data Visualization
plt.bar(height = df. WT , x = np.arange(1,82,1)) 

plt.hist(df.WT, color='red')

plt.boxplot(df.WT) #boxplot

## In both speed and weight have the outliers.
