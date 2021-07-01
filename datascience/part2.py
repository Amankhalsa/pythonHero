# import numpy
import os 
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# import sklearn
# import matplotlib


df =pd.read_csv("test.csv")


print(df['Name'])
print("=="*40)
print(df.sample())

