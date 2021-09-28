# HHA507_introAPI
This is the APIs Introduction assignment for the HHA 507 course. 

The COVID-19 Tracker Project in Canada is a webpage that allows users to see COVID19 updates for Canada in real time. 
The webpage shows the number of reported cases, deaths, hospitalizations, recoveries, tests performed, and vaccine doses administered. 
This information is updated multiple times throughout the day. 
Please see the URL provided: https://covid19tracker.ca/ 

The API documentation linked to this webpage was retrieved from a public GitHub API. 
Please use the URL provided to view: https://api.covid19tracker.ca/docs/1.0/overview

The API documentation provides a URI, which links to JSON responses for multiple routes within the database. 
For this assignment the routes used were 'summary', 'cases' and 'reports'. 

The summary route provides a basic summary of the latest information generated on the webpage. 
This JSON reponse includes subjects like changes in fatality counts, hospitalizations, recoveries, total cases, total vaccines distributed and much more. 

The cases route provides the latest 100 cases reported within the webpage database. 
This JSON response provides an id, province, city, age, travel history, source, and date. 

The reports route provides a daily summary of COVID19 statistics for every province in Canada. 
This JSON response includes changes in things enlisted above, such as changes in fatalities and hospitalizations. 
