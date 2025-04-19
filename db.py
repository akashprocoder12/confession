from pymongo import MongoClient

import os


client = MongoClient("mongodb+srv://proversionofakash:yXmPmDDhLvZfSx62@cluster0.eiefq2m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.confessionDB
confessions = db.confessions
