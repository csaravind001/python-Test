import timeit
import statistics
import pandas as pd
from python_test.aap.config.config import *

__author__ = 'Aravind'

class ResponseTime(object):

    def __init__(self):

        print "process started"
        self.get_api_response_timeing=[]
        self.post_api_response_timeing=[]
        self.get_api_mean=[]
        self.get_api_stddev=[]
        self.post_api_mean= []
        self.post_api_stddev =[]

    def build(self):
        self.get_api_response_timing()
        print "process end"

    def get_api_response_timing(self):
        # Hit the dynamic page 100 times, time the response time

        t = timeit.Timer("h.request('http://localhost:3000/message',headers={'cache-control':'no-cache'})","from httplib2 import Http; h=Http()")

        times_p1 = t.repeat(10,1)
        self.get_api_response_timeing.append(times_p1)

        # Now hit a similar static page 100 times
        t = timeit.Timer("h.request('http://localhost:3000/message', headers={'cache-control':'no-cache'})","from httplib2 import Http; h=Http()")
        times_p2 = t.repeat(10,1)
        self.post_api_response_timeing.append(times_p2)

        get_api_mean= statistics.mean(self.get_api_response_timeing[0])
        post_api_mean= statistics.mean(self.post_api_response_timeing[0])

        get_api_stddev=  statistics.stdev(self.get_api_response_timeing[0])
        post_api_stddev= statistics.stdev(self.post_api_response_timeing[0])

        self.get_api_mean.append(get_api_mean)
        self.post_api_mean.append(post_api_mean)
        self.post_api_stddev.append(post_api_stddev)
        self.get_api_stddev.append(get_api_stddev)

        ew = pd.ExcelWriter('ResponseTime.xlsx')
        df=pd.DataFrame({"GET_API":self.get_api_response_timeing[0],"POST_API":self.post_api_response_timeing[0]}).to_excel(ew, sheet_name='APIResponseTime')
        df=pd.DataFrame({"GET_API_Mean":self.get_api_mean,"GET_API_Stddev":self.get_api_stddev,"POST_API_Mean":self.post_api_mean,"POST_API_Stddev":self.post_api_stddev}).to_excel(ew, sheet_name='Mean&Stddev')


if __name__ == '__main__':
    runner = ResponseTime()
    runner.build()