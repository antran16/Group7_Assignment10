# Name: An Tran, Morgan Miller
# email: tran2a3@mail.uc.edu, mile8m9@uc.mail.edu
# Assignment Title: Assignment 10
# Due Date: 11/08/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: Work with API URL and requests library 
# Citations: NASA API: https://api.nasa.gov/ (Asteroids NeoWs)
# Anything else that's relevant:  

#functions.py

import json 
import requests 

class EarthObjects:     # creates a class of EarthObjects
    def __init__(self):    
        # get the URL from NASA's API
        self.response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-01-16&end_date=2023-01-18&api_key=3RNYshglaENikKuhhinTEUx5hFMVaXu2jwB2DAmd')
        
        #response.content is a string with everything on the page
        #json.loads turns that string into the dictionary
        self.json_object = json.loads(self.response.content)
        
        #loop through the  near_earth_objects on the given date (can be start_date or end_date)
        self.near_earth = self.json_object['near_earth_objects']['2023-01-16']
    
    def nearestEarthObjects(self):
        output = []     # creates an empty list to store information for nearestEarthObjects
        for near in self.near_earth:
            obj = {}    # turn into a dictionary 
            obj['name'] = near['name']
            approach = near['close_approach_data'][0]   # access the first element of the object
            obj['full_approach'] = approach['close_approach_date_full']
            #print(f"{name} approached Earth on {full_approach}")
            output.append(obj)
        return output   # return the list