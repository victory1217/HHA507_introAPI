# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Import the request and pandas packages 

import requests
import pandas as pd 

##GET Request for a basic summary of COVID19 Tracking in Canada

jsonresponse = requests.get('https://api.covid19tracker.ca/summary')

##Confirm GET Request was successful 

jsonresponse.status_code

##View basic summary information for COVID19 Tracking in Canada
jsonresponse.json()

##GET Request for the latest confirmed cases within the COVID19 Tracking System for Canada

jsonresponse2 = requests.get('https://api.covid19tracker.ca/cases')

##Confirm second GET Request was successful 

jsonresponse2.status_code

##View the latest confirmed cases in COVID19 Tracking in Canada

jsonresponse2.json()

##GET Request for daily COVID19 summaries for all Canadian provinces

jsonresponse3 = requests.get('https://api.covid19tracker.ca/reports')

##Confirm third GET Request was successful 

jsonresponse3.status_code

##View of daily COVID19 summaries for all Canadian provinces 

jsonresponse3.json()