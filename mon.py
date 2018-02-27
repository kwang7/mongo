'''
Caleb Smith-Salzberg and Kelly Wang
Team exceptForTheMongols
SoftDev2 pd7
K #05 -- Import/Export Bank
2018-02-25
'''

'''
We used NASA's Earth Meteorite Landings Dataset, a list of 1000 meteorites that have landed on Earth. It has info about a meteorite's name, class, geolocation, mass, and when it fell. 

To import the dataset into a Mongo db: 
First we used urllib2 and json to get the data and turn it into a dictionary. Then, we used the function insert_many to insert the dictionary into the Mongo db.

Here is the dataset:
https://data.nasa.gov/resource/y77d-th95.json

'''

from pymongo import MongoClient
import json, urllib2

def printstuff(ret):
    for re in ret:
        print re
#BEGINNING OF PREVIOUS HW


c = MongoClient('lisa.stuy.edu')
coll = c.test
rests = coll.restaurants


def allBoro(boro):
    ret = rests.find({'borough': boro })
    printstuff(ret)
'''
allBoro('Queens')
''' 

def allZip(zipe):
    ret = rests.find({'address.zipcode': zipe })
    printstuff(ret)
'''
allZip('11373')
'''

def zg(zipe, grade):
    #ret = rests.find( {'address.zipcode': zipe , 'grades.grade':grade} )
    ret = rests.find({ '$and': [ {'address.zipcode': zipe},{'grades.grade':grade} ] })
    printstuff(ret)
'''
zg('11373','A')
'''

def zs(zipe, score):
    #ret = rests.find( {'address.zipcode': zipe , 'grades.grade':grade} )
    ret = rests.find({ '$and': [ {'address.zipcode': zipe}, {'grades.score': { '$lt' : score } } ] } )
    printstuff(ret)
'''
zs('11378',12)
'''

def bgs(boro, grade, score):
    ret = rests.find({ '$and': [ {'borough': boro }, {'grades.grade':grade}, {'grades.score': { '$lt' : score } } ] } )
    printstuff(ret)
    
#bgs("Queens","A",30)



#END OF PREVIOUS HW



'''

#random stuff for fun

with open('comets.json') as jfile:
    data = json.load(jfile)
    min=data[0]['year'][0:data[0]['year'].find('-')]
    print min
    for entry in data:
        if entry['year'][0:data[0]['year'].find('-')] < min:
            min = entry['year'][0:data[0]['year'].find('-')]
        print entry['year'][0:data[0]['year'].find('-')]
    print min
    #print data
#db.exceptForTheMongols.insert({})
'''


nas = c.exceptForTheMongols
nasa = nas.nasa

com = urllib2.urlopen("https://data.nasa.gov/resource/y77d-th95.json")
come = com.read()
comet = json.loads(come) #load into python dictionary
#for stuff in comet:
    #print stuff
for meteor in comet:
    if "mass" in meteor:
        meteor["mass"] = float(meteor["mass"]) #change the mass field to an int for easier use later to compare values
    
def insert():
    nasa.insert_many(comet)
#insert() #add the data to the db

def findName(name):
    return nasa.find({"name":name})

#findName("Aachen")


def findId(id):
    return nasa.find({"id":id})
'''
findId("4984")
'''

def findYear(year):
    return nasa.find({"year": {"$regex": year}})
'''
findYear("1775")
'''

def my(mass, year):
    return nasa.find( {"$and": [ {"mass": mass}, {"year": {"$regex": year}}]})
'''
my(4000,"1890")
'''

def massRange(minM,maxM):
    return nasa.find( {"$and" : [ {"mass": {"$lte": maxM} }, {"mass": {"$gte": minM} } ] } )
'''    
massRange(4000,4500)
'''

