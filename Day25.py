# Pandas
# Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. 
# Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:
# reshaping
# merging
# sorting
# slicing
# aggregation
# imputation. 

# If you are using anaconda, you do not have install pandas.

# Installing Pandas
# For Mac:
# pip install conda
# conda install pandas

# For Windows:
# pip install conda
# pip install pandas
# Pandas data structure is based on Series and DataFrames.
# 
# A series is a column and a DataFrame is a multidimensional table made up of collection of series. 
# In order to create a pandas series we should use numpy to create a one dimensional arrays or a python list. 
# Pandas series is just one column of data. If we want to have multiple columns we use data frames.
# Data frame is a collection of rows and columns.

# Next, we will see how to import pandas and how to create Series and DataFrames using pandas

# Importing Pandas
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np
# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)

#   0    1
#   1    2
#   2    3
#   3    4
#   4    5
#   dtype: int64

# Creating Pandas Series with custom index

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# dtype: int64

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

#    1    Orange
#    2    Banana
#    3    Mango
#    dtype: object

# Creating Pandas Series from a Dictionary

dct = {'name':'Ivan','country':'Serbia','city':'Belgrade'}
s = pd.Series(dct)
print(s)

# name           Ivan
# country      Serbia
# city       Belgrade
# dtype: object

# Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2, 3])
print(s)

#    1    10
#    2    10
#    3    10
#    dtype: int64

# Creating a Pandas Series Using Linspace

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

#    0     5.000000
#    1     6.666667
#    2     8.333333
#    3    10.000000
#    4    11.666667
#    5    13.333333
#    6    15.000000
#    7    16.666667
#    8    18.333333
#    9    20.000000
#    dtype: float64

# DataFrames

# Pandas data frames can be created in different ways.
# Creating DataFrames from List of Lists

data = [
    ['Ivan', 'Serbia', 'Belgrade'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

#    Names Country       City
# 0   Ivan  Serbia   Belgrade
# 1  David      UK     London
# 2   John  Sweden  Stockholm

# Creating DataFrame Using Dictionary

data = {'Name': ['Ivan', 'David', 'John'], 'Country':[
    'Serbia', 'UK', 'Sweden'], 'City': ['Belgrade', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Creating DataFrames from a List of Dictionaries

data = [
    {'Name': 'Ivan', 'Country': 'Serbia', 'City': 'Belgrade'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# Reading CSV File Using Pandas

# To download the CSV file and put it in your working directory, what is needed in this example, console/command line is enough:
# curl -O c:\weight-height.csv https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
# to get current working directory for curl command:
import os
print(os.getcwd())
# c:\

import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)

#       Gender     Height      Weight
# 0       Male  73.847017  241.893563
# 1       Male  68.781904  162.310473
# 2       Male  74.110105  212.740856
# 3       Male  71.730978  220.042470
# 4       Male  69.881796  206.349801
# ...      ...        ...         ...
# 9995  Female  66.172652  136.777454
# 9996  Female  67.067155  170.867906
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103
# 
# [10000 rows x 3 columns]

# Data Exploration
# Let us read only the first 5 rows using head()

print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
#   Gender     Height      Weight
# 0   Male  73.847017  241.893563
# 1   Male  68.781904  162.310473
# 2   Male  74.110105  212.740856
# 3   Male  71.730978  220.042470
# 4   Male  69.881796  206.349801

# Let us also explore the last recordings of the dataframe using the tail() methods.

print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
#       Gender     Height      Weight
# 9995  Female  66.172652  136.777454
# 9996  Female  67.067155  170.867906
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103

# As you can see the csv file has three rows: Gender, Height and Weight. 
# If the DataFrame would have a long rows, it would be hard to know all the columns. 
# Therefore, we should use a method to know the colums. 
# We do not know the number of rows. Let's use shape meathod.

print(df.shape) # as you can see 10000 rows and three columns
# (10000, 3)

# Let us get all the columns using columns.
print(df.columns)
# Index(['Gender', 'Height', 'Weight'], dtype='object')

# Now, let us get a specific column using the column key
heights = df['Height'] # this is now a series
print(heights)
# 0       73.847017
# 1       68.781904
# 2       74.110105
# 3       71.730978
# 4       69.881796
#           ...    
# 9995    66.172652
# 9996    67.067155
# 9997    63.867992
# 9998    69.034243
# 9999    61.944246
# Name: Height, Length: 10000, dtype: float64

weights = df['Weight'] # this is now a series
print(weights)

print(len(heights) == len(weights))
# True

# The describe() method provides a descriptive statistical values of a dataset.
print(heights.describe()) # give statisical information about height data
# count    10000.000000
# mean        66.367560
# std          3.847528
# min         54.263133
# 25%         63.505620
# 50%         66.318070
# 75%         69.174262
# max         78.998742
# Name: Height, dtype: float64

print(weights.describe())

print(df.describe())  # describe can also give statistical information from a dataFrame
#              Height        Weight
# count  10000.000000  10000.000000
# mean      66.367560    161.440357
# std        3.847528     32.108439
# min       54.263133     64.700127
# 25%       63.505620    135.818051
# 50%       66.318070    161.212928
# 75%       69.174262    187.169525
# max       78.998742    269.989699

# Similar to describe(), the info() method also give information about the dataset.

# Creating a DataFrame
# As always, first we import the necessary packages. 
# Now, lets import pandas and numpy.

import pandas as pd
import numpy as np
data = [
    {"Name": "Ivan", "Country":"Serbia","City":"Belgrade"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data, index=[1,2,3])
print(df)

#     Name Country       City
# 1   Ivan  Serbia   Belgrade
# 2  David      UK     London
# 3   John  Sweden  Stockholm

# Adding a column to a DataFrame is like adding a key to a dictionary.
# First let's use the previous example to create a DataFrame. 
# After we create the DataFrame, we will start modifying the columns and column values.
# Adding a New Column
# Let's add a weight column in the DataFrame
weights = [74, 78, 69]
df['Weight'] = weights
df # output is table if stands alone w/o print()
print(df)

#     Name Country       City  Weight
# 1   Ivan  Serbia   Belgrade      74
# 2  David      UK     London      78
# 3   John  Sweden  Stockholm      69

# Let's add a height column into the DataFrame aswell

heights = [173, 175, 169]
df['Height'] = heights
print(df)

#     Name Country       City  Weight  Height
# 1   Ivan  Serbia   Belgrade      74     173
# 2  David      UK     London      78     175
# 3   John  Sweden  Stockholm      69     169

# As you can see in the DataFrame above, we did add new columns, Weight and Height. 
# Let's add one additional column called BMI(Body Mass Index) by calculating their BMI using thier mass and height. 
# BMI is mass divided by height squared (in meters) BMI = Weight/(Height * Height)
 
# As you can see, the height is in centimeters, so we shoud change it to meters. Let's modify the height row.
 
# Modifying column values
df['Height'] = df['Height'] * 0.01
df
print(df)
#     Name Country       City  Weight  Height
# 1   Ivan  Serbia   Belgrade      74    1.73
# 2  David      UK     London      78    1.75
# 3   John  Sweden  Stockholm      69    1.69

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi   

bmi = calculate_bmi()

df['BMI'] = bmi
df
print(df)

#     Name Country       City  Weight  Height        BMI
# 1   Ivan  Serbia   Belgrade      74    1.73  24.725183
# 2  David      UK     London      78    1.75  25.469388
# 3   John  Sweden  Stockholm      69    1.69  24.158818

# Formating DataFrame columns
# The BMI column values of the DataFrame are float with many significant digits after decimal. 
# Let's change it to one significant digit after point. 
df['BMI'] = round(df['BMI'], 1)
print(df)
#     Name Country       City  Weight  Height   BMI
# 1   Ivan  Serbia   Belgrade      74    1.73  24.7
# 2  David      UK     London      78    1.75  25.5
# 3   John  Sweden  Stockholm      69    1.69  24.2

# The information in the DataFrame seems not yet complete, let's add birth year and current year columns.
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2023, index=[1, 2, 3])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
df
print(df)
#     Name Country       City  Weight  Height   BMI Birth Year  Current Year
# 1   Ivan  Serbia   Belgrade      74    1.73  24.7       1769          2023
# 2  David      UK     London      78    1.75  25.5       1985          2023
# 3   John  Sweden  Stockholm      69    1.69  24.2       1990          2023

# Checking data types of Column values

print(df.Weight.dtype)
#     dtype('int64')

df['Birth Year'].dtype # it gives string object , we should change this to number

df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now
# int32

# Now same for the current year:
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype

# Now, the column values of birth year and current year are integers. We can calculate the age.
ages = df['Current Year'] - df['Birth Year']
ages
# 1    254
# 2     38
# 3     33
# dtype: int32

df['Ages'] = ages
print(df)
#     Name Country       City  Weight  Height   BMI  Birth Year  Current Year  \
# 1   Ivan  Serbia   Belgrade      74    1.73  24.7        1769          2023   
# 2  David      UK     London      78    1.75  25.5        1985          2023   
# 3   John  Sweden  Stockholm      69    1.69  24.2        1990          2023   
# 
#    Ages  
# 1   254  
# 2    38  
# 3    33

# Boolean Indexing
print(df[df['Ages'] > 120])
#    Name Country      City  Weight  Height   BMI  Birth Year  Current Year  \
# 1  Ivan  Serbia  Belgrade      74    1.73  24.7        1769          2023   
# 
#    Ages  
# 1   254  