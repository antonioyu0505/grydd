# Installation

This project assumes that python 3 and pip are installed in the system. A virtual environment is highly recommended, however, you can proceed without it.

Start by running the requirements.txt file through the following command:

```$ pip3 install -r requirements.txt```

After this, you are almost set. The only thing remaining is creating a valid PostgreSQL database.

# Setting up

You must fill up the [settings file](grydd_access/settings.py) environment values. As such, creating a .env file is recommended. You will need to set the database connections as well as the SECRET_KEY, DEBUG and ALLOWED_HOST values.

# Run

In order to access the administration panel, you must first create a superuser through the command below

```$ python manage.py createsuperuser```

Once you have done so, you can deploy the application on your desired port with

```$ python manage.py runserver <port>```

on `localhost:port/admin` with the credentials that you have set up during the super user creation.

# API

You can check the API available at `localhost:port/` for a list view of the basic CRUD available. There's another operation that you can make in order to validate if a certain user has access to certain points with the following action 

`GET /companies/{id}/validate-access/?user={user_id}&access-point={access_point_id}`