## Steps to install and run the application
Python Version 3.8 or above is required to run this application.

- Clone the repository on your local system
- pip install -m venv .venv (run this to create virtual env)
- To activate the virtual environment - .venv\Scripts\activate
- Once activated run - pip install -r requirements.txt to install required libs
- To run the application - python app.py
- Application will request parameters from console
- Supported date format is YYYY-MM-DD


## Features

- Application support acquiring data from remote server based on given parameters
- Once data is obtained application inserts data in SQLite tables
- Displays the count of number of new rows inserted
- No duplicate check is applied while inserting. 