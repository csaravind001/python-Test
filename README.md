# python-Test


Readme for Python API Details goes here

It contains one services,
	1. api_get_email
	
Getting started:
================

create a virtualenv using the command "mkvirtualenv AAP_GATEWAY_API".

Installation Dependencies:

pip install flask==0.10

Configure the Mongodb 
	1. Create one database as name Testing
	2. Create one collection as name email_details
	3. Create one record for precessing  

### Email credentials
For email notification we need to configure the email credentials on config.py file

Run - python main.py

Web URL:
========

http://localhost:3000/message

Email Service: Fetching the email details from database.

Note: 

I have used the Cache functionality for saving the time consumption. Every first hit on the corresponding API, fetching the data from database. Second hit onwards API fetching the data from cache. 

 
