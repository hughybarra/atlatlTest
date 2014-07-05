# Atlatl Test

### About this app

This app is a test program given to me by Atlatl software. The test is designed to test my skills in Python/Django. Bellow are instructions on how to get up and running with my test program.

### Do you have Django Installed? 

If you have Django installed on your computer already you can skip this step. That being said, if you don't you can follow these instructions to get it installed. 

I decided to go with VirtualEnv for this assignment. VirtualEnv helps keep dependencies organized in a simple manner so lets go ahead and get started with that. go to the [virtualenv](http://virtualenv.readthedocs.org/en/latest/) website and download virtual env. 

Set up a new Virtual Environment. Open up a terminal window and enter this command.  You can use any name you like, swap out the ENV for whatever you want

`virtualenv ENV --no-site-packages`

Next cd into  ENV 

`cd ENV`

Now lets activate our Virtualenv. 

`source bin/activate` 

This activates your virtual environment and you're now working in the virtual env box.
Now you're going to need to install Django. I used pip for my installation. If you dont have pip navigate to [pip](https://pypi.python.org/pypi/pip) and follow the installation instructions. Once you're ready and pip is installed install django

`pip install django `

This will install django into your virtual environment. Now that that is installed our virtual env is ready for our Dajngo app.

### Download the Project 

Go ahead and download the project now. You can do that by clicking on the download zip. Once the project is downloaded and you have unzipped the download. cd into the project using terminal

`cd atlatlTest`

Onc inside the atlatlTest directory we can run our Django server.

`python manage.py runserver`

navigate your browser to `http://127.0.0.1:8000/` and you should see the project.

### Command Line Commands

Below I have listed out all of the django custom commands. You will find an explanation and the instructions for each command.

** add_owner **

 `python manage.py add_owner --name [enter name]`

** add_house **

 `python manage.py add_house --address [enter address] --owner [enter name]`

** show_houses **

 `python manage.py show_houses`

** show_houses [owner] **

 `python manage.py show_houses --owner`

** delete_house **
 `python manage.py delete_house --addr-contains [enter partial address]`








