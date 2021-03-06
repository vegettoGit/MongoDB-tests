# Coursera Introduction to MongoDB

import pymongo
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

client = MongoClient("connectionString")

pipeline = [
    {
        '$match': {'language': 'Korean, English'}
    }
]

clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))