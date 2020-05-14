#! /usr/bin/python3.7

# DBConnection requires app to configure and set mongoDB connection
class DBConnection():
    def __init__(self):
        pass

    def getDB(self):
        return self.connection
    
    def setDB(self, connection):
        self.connection = connection

# Object to be exported
DB = DBConnection()

# from db import DB
# database = DB.getDB()