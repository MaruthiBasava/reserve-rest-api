import pymongo

class Database(object):

    URI = "mongodb://127.0.0.1:27017"
    DATABASE_ID = 'reserve-db'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[Database.DATABASE_ID]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query, {'_id': False})

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def delete_one(collection, query):
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def get_all_instances(collection):
        return [data for data in Database.find(collection=collection, query={})]
