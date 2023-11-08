# Name: An Tran
# email: tran2a3@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/08/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: Work with API URL and requests library 
# Citations: NASA API: https://api.nasa.gov/ (Asteroids NeoWs)
# Anything else that's relevant:  

#main.py

from functionsPackage.functions import *

if __name__ == "__main__":
    # creates an instance of the EarthObjects class that created in functionsPackage
    earth = EarthObjects()
    nearObjects = earth.nearestEarthObjects()
    for obj in nearObjects:
    #print the name of the object approached Earth on a given date
        print(f"{obj['name']} approached Earth on {obj['full_approach']}")
 
   
    
