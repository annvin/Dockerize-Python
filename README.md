# Dockerize-Python
Python script to pull data from google sheet
Steps involved:
Create a google sheet with the data 
Create a account in developer console which gives the service account with google sheet api enabled
Add the credentials to this account in developer console 
Give access to the service account to the google sheet created
Create a python script to pull the data from the google sheet which also creates an output  json file that contains the data from the  google sheet.

Creation of Docker Image
Steps Involved:
Install Docker Desktop
Add docker extensions in visual studio code
Create a docker file which include all dependencies
Type the cmd: docker build –t imagename which will create an image which can be viewed in docker desktop application
Type the cmd: docker run  imagename which will run the image and display the output in the same console


