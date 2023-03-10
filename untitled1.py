# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jE3YR8sQWRP90_Ux-amhD4uPs2UXVkQp
"""

pip install pycaret

# for dealing with dataframes
import pandas as pd
pd.set_option('display.max_columns',None)  
pd.set_option('display.expand_frame_repr',False)
pd.set_option('display.max_colwidth',100)

# for visualization
import plotly.express as px

import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt

# for mathematical operations
import numpy as np

# for ml in pycaret
from pycaret.classification import *

data=pd.read_csv('/content/UsedCarsData.csv')

data

# importing section
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# Finding the missing values
data.isna().any()

# Finding if missing values
data.isnull().any()

data.sold.unique()

# Here it contains '?', so we Drop it
data = data[data.sold != '?']

# checking it again
data.dtypes

data.selling_price.unique()

# Here it contains '?', so we Drop it
data = data[data.selling_price != '?']

# checking it again
data.dtypes

"""important factors in deciding cars' selling **price**"""

# binning- grouping values
bins = np.linspace(min(data['selling_price']), max(data['selling_price']), 4)
group_names = ['Low', 'Medium', 'High']
data['selling_price-binned'] = pd.cut(data['selling_price'], bins,
							labels = group_names,
							include_lowest = True)

print(data['selling_price-binned'])
plt.hist(data['selling_price-binned'])
plt.show()

# categorical to numerical variables
pd.get_dummies(data['fuel']).head()
  
# descriptive analysis
# NaN are skipped
data.describe()

# examples of box plot
plt.boxplot(data['selling_price'])
  
# by using seaborn
sns.boxplot(x ='km_driven', y ='selling_price', data = data)
  
# Predicting price based on engine size
# Known on x and predictable on y
plt.scatter(data['km_driven'], data['selling_price'])
plt.title('Scatterplot of km_driven vs selling_price')
plt.xlabel('km_driven')
plt.ylabel('selling_pricee')
plt.grid()
plt.show()

# examples of box plot
plt.boxplot(data['selling_price'])
  
# by using seaborn
sns.boxplot(x ='seats', y ='selling_price', data = data)
  
# Predicting price based on engine size
# Known on x and predictable on y
plt.scatter(data['seats'], data['selling_price'])
plt.title('Scatterplot of seats vs selling_price')
plt.xlabel('seats')
plt.ylabel('selling_pricee')
plt.grid()
plt.show()

# Grouping Data
test = data[['year', 'selling_price', 'km_driven']]
data_grp = test.groupby(['year', 'selling_price'],
						as_index = False).mean()

data_grp

# pivot method
data_pivot = data_grp.pivot(index = 'year',
							columns = 'selling_price')
data_pivot

# heatmap for visualizing data
plt.pcolor(data_pivot, cmap ='RdBu')
plt.colorbar()
plt.show()

# Analysis of Variance- ANOVA
# returns f-test and p-value
# f-test = variance between sample group means divided by
# variation within sample group
# p-value = confidence degree
data_annova = data[['fuel', 'selling_price']]
grouped_annova = data_annova.groupby(['fuel'])

annova_results_l = sp.stats.f_oneway(
                             grouped_annova.get_group('Diesel')['selling_price'],
                             grouped_annova.get_group('Petrol')['selling_price']
                             
                                    )
print(annova_results_l)

# Correlation- measures dependency, not causation
sns.regplot(x ='seats', y ='selling_price', data = data)
plt.ylim(0, )

from scipy.stats import chi2_contingency
  
# defining the table
data = [[207, 282, 241], [234, 242, 232]]
stat, p, dof, expected = chi2_contingency(data)
  
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')

"""# New Section"""