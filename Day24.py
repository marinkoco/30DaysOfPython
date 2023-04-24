# Statistics

# Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation and presentation of data. 
# Statistics is a branch of Mathematics that is recommended to be a prerequisite for data science and machine learning. 
# Statistics is a very broad field but we will focus in this section only on the most relevant part. 
# After completing this challenge, you may go onto the web development, data analysis, machine learning and data science path. 
# Whatever path you may follow, at some point in your career you will get data which you may work on. 
# Having some statistical knowledge will help you to make decisions based on data, data tells as they say.

# Data

# What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. 
# It can be any character, including text and numbers, pictures, sound, or video. 
# If data is not put in a context, it doesn't make any sense to a human or computer. 
# To make sense from data we need to work on the data using different tools.
# 
# The work flow of data analysis, data science or machine learning starts from data. 
# Data can be provided from some data source or it can be created. 
# There are structured and unstructured data.
# 
# Data can be found in small or big format. Most of the data types we will get have been covered in the file handling section.
# 
# Statistics Module
# The Python statistics module provides functions for calculating mathematical statistics of numerical data. 
# The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. 
# It is aimed at the level of graphing and scientific calculators.

# NumPy

# In the first section we defined Python as a great general-purpose programming language on its own, but with the help of other popular libraries as(numpy, scipy, matplotlib, pandas etc) it becomes a powerful environment for scientific computing.
# 
# NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.
# 
# So far, we have been using vscode but from now on I would recommend using Jupyter Notebook. To access jupyter notebook let's install anaconda. If you are using anaconda most of the common packages are included and you don't have install packages if you installed anaconda.
# 
# asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy

# Importing NumPy
# Jupyter notebook is available if your are in favor of jupyter notebook

    # How to import numpy
import numpy as np
    # How to check the version of the numpy package
print('numpy:', np.__version__)
    # Checking the available methods
print(dir(np))

# Creating numpy array using
# Creating int numpy arrays

# Creating python List
python_list = [1,2,3,4,5]

    # Checking data types
print('Type:', type (python_list)) # <class 'list'>
    #
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# Creating float numpy arrays
# Creating a float numpy array from list with a float data type parameter
    # Python list
python_list = [1,2,3,4,5]

numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2) # array([1., 2., 3., 4., 5.])

# Creating boolean numpy arrays
# Creating a boolean a numpy array from list

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

# Creating multidimensional array using numpy
# A numpy array may have one or multiple rows and columns
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Creating numpy array from tuple
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

# Shape of numpy array
# The shape method provide the shape of the array as a tuple. The first is the row and the second is the column. 
# If the array is just one dimensional it returns the size of the array.

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10, 11]])
print(three_by_four_array.shape)

# Data type of numpy array
# Type of data types: str, int, float, complex, bool, list, None

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Size of a numpy array
# In numpy to know the number of items in a numpy array list we use size

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 9

# Mathematical Operation using numpy
# NumPy array is not like exactly like python list. 
# To do mathematical operation in Python list we have to loop through the items but numpy can allow to do any mathematical operation without looping. 
# Mathematical Operation:
 # Addition (+)
 # Subtraction (-)
 # Multiplication (*)
 # Division (/)
 # Modules (%)
 # Floor Division(//)
 # Exponential(**)

# Addition
 # Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)
    # original array:  [1 2 3 4 5]
    # [11 12 13 14 15]

# Converting types
# We can convert the data types of numpy array
# 
# Int to Float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr

# Int to Str
int_list = [1, 2, 3, 4, 5]
str_list = np.array(int_list).astype(str)
str_list
# array(['1', '2', '3', '4', '5'], dtype='<U11')

# Multi-dimensional Arrays
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
    # <class 'numpy.ndarray'>
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    # Shape:  (3, 3)
    # Size: 9
    # Data type: int64

# Getting items from a numpy array

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
    # First row: [1 2 3]
    # Second row: [4 5 6]
    # Third row:  [7 8 9]

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
    # First column: [1 4 7]
    # Second column: [2 5 8]
    # Third column:  [3 6 9]

# Slicing Numpy array
# Slicing in numpy is similar to slicing in python list
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
    # [[1 2]
    #  [4 5]]

# How to reverse the rows and the whole array?
two_dimension_array[::]

# Reverse the row and column positions
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array[::-1,::-1]

# How to represent missing values ?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    # [[ 1  2  3]
    #  [ 4 55 44]
    #  [ 7  8  9]]

 # Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
numpy_zeroes
 # array([[0, 0, 0],
 #           [0, 0, 0],
 #           [0, 0, 0]])

 # Numpy Zeroes

numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
    # [[1 1 1]
    #  [1 1 1]
    #  [1 1 1]]

twoes = numpy_ones * 2

# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
    # [[1 2 3]
    #  [4 5 6]]
    # [[1 2]
    #  [3 4]
    #  [5 6]]

flattened = reshaped.flatten()
flattened
 # array([1, 2, 3, 4, 5, 6])

    ## Horitzontal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
    # [5 7 9]
    # Horizontal Append: [1 2 3 4 5 6]

    ## Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
    # Vertical Append: [[1 2 3]
    #  [4 5 6]]

# Generating Random Numbers