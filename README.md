# Installation

This project assumes that python 3 and pip are installed in the system. A virtual environment is highly recommended, however, you can proceed without it.

Start by running the requirements.txt file through the following command:

```$ pip3 install -r requirements.txt```

After this, you are almost set. The only thing remaining is creating a valid PostgreSQL database.

# Setting up

You must fill up the [settings file](grydd_access/settings.py) environment values. As such, creating a .env file is recommended. You will need to set the database connections as well as the SECRET_KEY, DEBUG and ALLOWED_HOST values.