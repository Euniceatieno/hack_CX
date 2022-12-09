# HackCX
  * HackCX is a customer-business conversational tool for businesses that 
  summarizes dialogue between  the customer and the business, 
  does  analysis and compiles the data so a business can be able  to track the most reported issues 
  by their customers. 

# Core Technologies and Libraries Used

Technology/Library | Description 
--- | --- |
*Django REST Framework* | *Api building framework for django*
*cohere AI* | *Provision for NLP tools*
*Postgres* | *A relational database service*
*Django* | *A python framework for building serverside applications*

  

# Setting up the codebase locally

This is a step by step guide on how to set up the codebase locally

Clone the project
----------------------
``` shell
git clone https://github.com/Euniceatieno/HackCX.git
```
Set up your virtual environment
----------------------
``` shell
gpython3 -m venv env
```
Activate your virtual environment
----------------------
``` shell
source env/bin/activate
```
Install the required packages
----------------------
``` shell
python3 -m pip install -r requirements.txt --no-cache-dir
```
Create a .env file with the following environment variables
------------------------------------------------------------------
``` shell
SECRET_KEY=yoursecretkey
DATABASE_NAME=yourdb
DATABASE_USER=yourdbuser
DATABASE_PASSWORD=yourbdpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
Export your environment variables
--------------------------------------------
``` shell
source .env
```
Create a local database with the credentials in your .env file
---------------------------------------------------------------

Run migrations
----------------------
``` shell
python3 manage.py makemigrations
```
Migrate database updates
----------------------
``` shell
python3 manage.py migrate
```
Start local server
----------------------
``` shell
python3 manage.py runserver
```

# Contacts
For any queries ,reach out to either: 
 * *okelezo@gmail.com*
 * *shiunduflavian56@gmail.com*
 * *eunniceatieno@gmail.com*

