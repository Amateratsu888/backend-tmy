# Typical Meteorological Year RESTFUL API DOC



## Setup and running instructions 

-   Python 3.8 or above
    
-   A MongoDB Atlas cluster. Follow the "[Get Started with Atlas](https://docs.atlas.mongodb.com/getting-started/)" guide to create your account and MongoDB cluster. Keep a note of your database username, password, and [connection string](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/#connect-to-your-atlas-cluster) as you will need those later.
-  Before you begin, ensure that you have Python and `pip` (Python package manager) installed on your system.


### Step 1: Clone a Project Directory 
Start by cloning the repository for Flask project: 
``` git clone url```
``` cd backend-tmy```
### Step 2: Create a virtual environment
Inside your project directory, create a virtual environment to isolate your project's dependencies:
1.  Create a virtual environment. This will create a directory called .venv in your current directory. This is your virtual environment.
    
    ```python3 -m venv .tmy-env```
    
2.  To use and install stuff into your virtual environment, you need to "activate" it first. Activating it will tell your interpreter to use this when running your programs etc.
    
   -   On Windows:
`venv\Scripts\activate`
-   On macOS and Linux:
`source venv/bin/activate`
    
3.  Now you can install stuff into your virtual environment (Flask, requests, whatever else you need).
### Step 3: Install the dependencies
Now, install the dependencies using `pip`:
`pip install -r requirements.txt`
### Step 4: Add environment's variables
In root folder create a .env file and add the follow environment's variables

 - MONGO_URI = "your mongo DB uri"
 - AWS_ACCESS_KEY = "your aws access key "
 - AWS_PRIVATE_KEY = "your aws private key"
 - S3_BUCKET_NAME= "the name of your S3 bucket"

hint: click on this [link](https://medium.com/@shamnad.p.s/how-to-create-an-s3-bucket-and-aws-access-key-id-and-secret-access-key-for-accessing-it-5653b6e54337) to know how aws S3 work ;)
### Step 5: Run the Flask App

To run your Flask app, use the following command:
`flask run` 

Your Flask API should now be running locally. You can access it at `http://localhost:5000/api/tmy`.

## Libraries & tools

 - pymongo (Use a mongo database in your flask app)
 - boto3 (Use aws S3 service in your flask app)
 - python-dotenv (enable to use environments variables in .env )
 - PyYAML (for generate a yaml file from a python dictionary)
 
## Application structure 

Explanation of the directory structure:

- `/`: The root directory of your project.
- `/app/`: This directory contains your Flask application code.
  - `__init__.py`: An initialization script for your Flask app.
  - `dictToYml.py`: A Python module for dictionary to YAML conversion.
  - `routes.py`: A Python module defining the routes and views of your app.
  - `tmyValidator.py`: A Python module for TMY validation functionality.
- `/tmy-env/`: This directory is for virtual environment and environment configuration.
  - `.env`: Environment variables file.
  - `.flaskenv`: Flask environment configuration file.
  - `.gitignore`: Git ignore file to specify which files should be ignored by Git.
- `app.py`: The main Python script for running your Flask app.
- `config.py`: Configuration settings for your Flask app.
- `README.md`: Markdown file for project documentation.
- `requirements.txt`: File listing project dependencies for easy installation.

This directory structure provides a clear separation of your Flask app code, configuration files, and environment-related files. You can add your Flask application logic to the appropriate Python modules within the `/app/` directory and manage your dependencies using `requirements.txt`.

  
