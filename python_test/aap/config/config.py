
__author__ = 'Aravind'

#### Mongodb config
from pymongo import Connection
connection = Connection('localhost', 27017)
db = connection.Testing


### Email credentials
username = 'your emaild'
receivers = ['receivers email']
password = "enter your password"

### API links #####

message_api ="http://localhost:3000/message"