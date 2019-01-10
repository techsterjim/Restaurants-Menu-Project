# Restaurants-Menu-Project
The Item Catalog project is part of Udacity's Full Stack Developer program. It is a simple web application built using Flask (a Python web framework) that lists restaurants along with their menus. Additionally, it  allows registered users to add, edit, and delete restaurants and menu items in the restaurants. Users will register using Google or Facebook. 

## Required Libraries and Dependencies
The project code requires the following software:
- Python 2.7
- VirtualBox
- Vagrant

## Setting up OAuth2.0
1. You will need to sign up for a Google email account and use your credentials to log into Google Cloud Platform. Visit [Google Cloud Console](http://console.developers.google.com) to create oAuth credentials. Click [here](https://developers.google.com/identity/protocols/OAuth2) to learn more.  
2. Also, you will need to a Facebook account to access the [Facebook For Developers](https://developers.facebook.com) account to create oAuth credentials.


## Install the virtual machine
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

1. Download and install VirtualBox.
2. Download and install Vagrant.
3. Create a folder on your PC from which you'd like to store this project.
4. Fork and clone this repository into the folder you've just selected.
5. Update client_secrets.json and fb_client_secrets.json with your Oauth credentials. 

## Instructions to run the project
Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows) and navigate to the project directory. Once the VM has been installed, run vagrant up to start the machine. Then run vagrant ssh to log in. 

1. In VM, change the directory to `/vagrant`
2. Initialize the database by typing `python database_setup.py` 
3. Populate the database with some initial data by typing `python lotsofmenus.py` 
4. Launch the application by typing `python 'project.py'`
5. Open your web browser and visit http://localhost:5000/
6. The `Restaurants-Menu-Project` application main page will open and you will have to login with Google or Facebook to demo the web app. 



