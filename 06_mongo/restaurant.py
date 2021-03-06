#Max Millar
#SoftDev pd06
#K06 -- Yummy Mongo Py
#2019-03-01

from pymongo import MongoClient
#SERVER_ADDR='68.183.141.192'
client = MongoClient()
db = client.test
restaurants = db['primer-dataset']

def queryBorough(borough):
    for restaurant in restaurants.find({'borough':borough}):
        print(restaurant["name"])        

def queryZip(zipcode):
    for restaurant in restaurants.find({'address.zipcode':zipcode}):
        print(restaurant["name"])

def queryZipGrade(zipcode, grade):
    for restaurant in restaurants.find({'$and': [{'address.zipcode':zipcode},{'grades.0.grade':grade}]}):
        print(restaurant['name'])

def queryZipScore(zipcode, score):
    for restaurant in restaurants.find({'$and': [{'address.zipcode':zipcode},{'grades.0.score':{'$lt':score}}]}):
        print(restaurant['name'])

print('--------------------borough-------------------')
queryBorough("Bronx")
print('--------------------zipcode-------------------')
queryZip("11225")
print('--------------------zipgrade------------------')
queryZipGrade('10462','A')
print('--------------------zipscore------------------')
queryZipScore('10462',2)
    
