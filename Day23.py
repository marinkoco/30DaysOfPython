# Setting up Virtual Environments

# To start with project, it would be better to have a virtual environment. 
# Virtual environment can help us to create an isolated or separate environment. 
# This will help us to avoid conflicts in dependencies across projects. 
# If you write pip freeze on your terminal you will see all the installed packages on your computer. 
# If we use virtualenv, we will access only packages which are specific for that project.

# Python Flask is a web framework used for building web applications and APIs in Python. Flask is lightweight, flexible, and easy to learn, making it a popular choice for developing web applications.
# Flask can be used for a wide range of tasks, including building simple web pages, creating RESTful APIs, handling user authentication, and interacting with databases. It provides a variety of tools and extensions that make it easy to add functionality to your web application.
# Some common use cases of Flask include:
#  1 Developing web applications: Flask can be used to build web applications for businesses, personal projects, and more.
#  2 Building RESTful APIs: Flask's lightweight nature and ease of use make it a popular choice for building APIs.
#  3 Handling user authentication: Flask provides tools for handling user authentication and authorization, making it easy to secure your web application.
#  4 Interacting with databases: Flask supports a variety of databases, including SQL and NoSQL databases, making it easy to interact with your data.
# Overall, Flask is a versatile and powerful tool for building web applications and APIs in Python.

# Open your terminal and install virtualenv

# pip install virtualenv

# Inside the 30DaysOfPython folder create a flask_project folder.

# After installing the virtualenv package go to your project folder and create a virtual env by writing:

# For Mac/Linux:
# >>> ~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

# For Windows:
# cd - Navigate to the directory where you want to create your virtual environment
# type the following command:
# >>> python -m venv venv

# I prefer to call the new project venv, but feel free to name it differently. 
# Let us check if the the venv was created by using ls (or dir for windows command prompt) command.

# asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls venv/
# Let us activate the virtual environment by writing the following command at our project folder.
# For Mac/Linux:

# asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate

# Activation of the virtual environment in Windows may very on Windows Power shell and git bash.

# For Windows Power Shell:
# C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate

# For Windows Git bash:
# C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate

# After you write the activation command, your project directory will start with venv. See the example below.
# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$

# Now, lets check the available packages in this project by writing pip freeze. 
# You will not see any packages.

# We are going to do a small flask project so let us install flask package to this project.

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask

# Now, let us write pip freeze to see a list of installed packages in the project:

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
# Click==7.0
# Flask==1.1.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# MarkupSafe==1.1.1
# Werkzeug==0.16.0

# When you finish you should dactivate active project using deactivate.

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
# The necessary modules to work with flask are installed. 
# Now, your project directory is ready for a flask project. 
# You should include the venv to your .gitignore file not to push it to github.