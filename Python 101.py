# how to create a dataframe using numpy and pandas 

import pandas as pd
import numpy as np

mydata = [[45,55,65],[44,55,66],[77,22,33]]
# print(np.array(mydata))    printts the np array
myindex = ['USA','INDIA','CHINA']
mydata1 = ['POP','GDP','AREA']

df = pd.DataFrame(mydata,myindex,mydata1)
print(df)

