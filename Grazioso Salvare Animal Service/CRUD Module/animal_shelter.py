#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CRUD in Python
#Author: Taylor Stapus
#SNHU CS340 Module 4-1 Milestone 
#Date: 03/27/2025

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33154
        #34615
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary 
            if insert != 0:
                return True
            else:
                return False
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData is not None:
            data = self.database.animals.find(searchData, {"_id": False})  
            for document in data:
                print(document)
        else:
            data = self.database.animals.find({}, {"_id": False})
        
        return data
    
#Method to implement the U in CRUD.
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData})
            return result.raw_result
        else:
            return "{}"
        return result.raw_result

#Method to implement the D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        return results.raw_result


# In[ ]:





# In[ ]:




