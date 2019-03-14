# Flocka_records

Welcome to the new era of music!!
This app enables you to access music from your Flocka_Records favorite artists and enjoy your music.

### API ENDPOINTS

**_NOTE_**:

- API endpoints are prefixed by `/api/v1`.
- Fields for the date are specified like this `month day year time`. An example date format: `"Jan 10 2019 12:15AM"`

| Method        | Endpoint                                    | Description              |
| ------------- | --------------------------------------------| ------------------------ |
| POST          | `/auth/signup`                              | Create a user            |
| POST          | `/auth/login`                               | Log in a user            |
| GET           | `/auth/user/profile  `                      | Fetch a user's proifle   |
| GET           | `/auth/user/music`                          | Fetch all user's music   |


## Pre-requisites

Make sure you have Python version 3 and Postgres installed on your local machine.

## Usage

1. Clone the repository 

2. Change directory to the location you cloned the repository

3. Set environment variables for **APP_SETTINGS**, **SECRET_KEY**, **JWT_SECRET_KEY**, **DATABASE_URL** and **DATABASE_TEST_URL**. For more information see the `config.py` file from the _instance_ directory.

4. Create a database for the development database and test environment, example:

    ```bash
    $ sudo -u postgres psql
    $ CREATE DATABASE yourdbname;
    $ CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpassword';
    $ GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;
    ``` 

4. Create a virtual environment and activate it.
5. Install the required dependencies:

    ```bash
    $ pip install -r requirements.txt
    ``` 

6. Create the tables by running this script:

    ```bash
    $ python3 manage.py -a migrate
    ```

7. Run the Flask application:

    ```bash
    $ export FLASK_APP=run.py
    $ flask run
    ``` 

### Test the API on Postman

- The accepted content type header is as follows:

  - *key*: **Content-Type** 
  - *value*: **application/json**

- Authorization header is as follows:

  - *key*: **Authorization** 
  - *value*: **Bearer** `<access-token>`

The **access-token** is found from the response when a user logs in.

### Unit testing

Running the unit test is done using the command `pytest --cov=app/api` or `python -m unittest discover -v` on your terminal.
