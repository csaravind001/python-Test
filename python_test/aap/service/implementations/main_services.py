
from python_test.aap.config.config import *
import smtplib

__author__ = 'Aravind'
#-------------------------------------------email_notification --------------------------------------------------------#
def email_notification():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #Next, log in to the server
        server.ehlo()
        server.starttls()
        server.login(username, password)
        msg = "Hello! your API is Internal server error.. Thanks" # The /n separates the message from the headers
        server.sendmail(username, receivers, msg)
        respose= {"status": "sucessfullt sent "}
    #checks status while sendin the email if any error occurs handles exception
    except Exception:
        respose= {"status": "failed "}
    return respose
#-----------------------------------------------------------------------------------------------------------------------#


#---------------------------------For getting family details based on Pet family ids-----------------------------------#
def get_email_details_service(cache):
    response_dict={}
    data_dict={}
    cached = cache.get(str(1))
    if cached:
        return cached
    for data in db.email_details.find():
        data_dict["emailId"]=data["emailId"]
        data_dict["uuid"]=data["uuid"]
        response_dict["response"]=data_dict
        cache.set(str(1),response_dict)
    return response_dict
#----------------------------------------------------------------------------------------------------------------------#

