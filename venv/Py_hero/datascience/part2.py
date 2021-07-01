# import numpy
import pandas as pd
pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
# import sklearn
# import matplotlib


df =pd.read_csv("train.csv")

# print(df.sample())
print(df['Age'])

"""
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
 
 
df = pd.read_csv('train.csv')
# df['Age'] = 0
del df['Age']
print(df)
 
# print(df.describe())
# print(df.info())
# print(df.sample())
# print(df.columns)
 
 
 
pd.crosstab(df['Sex'],df['Survived'])
"""