import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

# Here's an example of how to create a new directory in a specific path using Python's os module:
import os

# specify the path where you want to create a new directory
path = "C:/temp1" # make sure you use FWD-SLASH '/'

# specify the name of the new directory you want to create
dir_name = "PyTEST"

# combine the path and the directory name using os.path.join()
new_dir = os.path.join(path, dir_name)

# create the new directory using os.mkdir()
os.mkdir(new_dir)


