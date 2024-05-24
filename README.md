# Dockerize-Python
Python script to pull data from google sheet
Steps involved:
1. Create a google sheet with the data 
2. Create a account in developer console which gives the service account with google sheet api enabled
3. Add the credentials to this account in developer console 
4. Give access to the service account to the google sheet created
5. Create a python script to pull the data from the google sheet which also creates an output  json file that contains the data from the  google sheet.

Creation of Docker Image
Steps Involved:
1. Install Docker Desktop
2. Add docker extensions in visual studio code
3. Create a docker file which include all dependencies
4. Type the cmd: docker build –t imagename which will create an image which can be viewed in docker desktop application
5. Type the cmd: docker run  imagename which will run the image and display the output in the same console


