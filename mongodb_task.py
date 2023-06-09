

import pymongo      
import time         
import requests
import json      

# Established connection with my mongo server using pymongo module
conn = pymongo.MongoClient("mongodb://balu:balakrishna@ac-mpkatov-shard-00-00.v63vj7u.mongodb.net:27017,ac-mpkatov-shard-00-01.v63vj7u.mongodb.net:27017,ac-mpkatov-shard-00-02.v63vj7u.mongodb.net:27017/?ssl=true&replicaSet=atlas-do4334-shard-0&authSource=admin&retryWrites=true&w=majority")


database = conn["Satellite"]        # Created a database named Satellite 
collection = database["ISS"]        # Created a collection named ISS in satellite database


for i in range(10800):        # To collect data of around 3 hours. We use "for" loop (60*60*3 = 10800)
  url = requests.get('http://api.open-notify.org/iss-now.json')       #Using requests module we collect the data from the website
  data = url.json()       # Collected data is stored in json format
  collection.insert_one(data)     #In each iteration the data is inserted into mongodb server 
  time.sleep(1)         # 1Sec delay is given so the loop halts for a second and run again
    
    
    
