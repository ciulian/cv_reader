# cv_reader
Simple rest api that parses cv/resume information
# Prerequisites:
Any environment with flask installed (anaconda)

# Creating the environment/Running the app:

1)Open anaconda prompt

2)Install all packages needed for flask(all are stored inside environment):

#### conda env create -f environment.yml

3)Application Discovery
The flask command is installed by Flask, not your application; it must be told where to find your application in order to use it. The FLASK_APP environment variable is used to specify how to load the application.

Unix Bash (Linux, Mac, etc.):

$ export FLASK_APP=cv_reader.py
$ flask run

Windows CMD:

> set FLASK_APP=cv_reader.py
> flask run

Windows PowerShell:

> $env:FLASK_APP="cv_reader.py"
> flask run

---------------------------------

# ENDPOINTS:

#### GET /personal 
#### GET /summary 
#### GET /experience
#### GET /licenses_and_certifications
#### GET /skills

# Flask CLI command that prints the data to the console:

### flask show-candidate-info
