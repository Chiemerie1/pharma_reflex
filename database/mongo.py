from pymongo import MongoClient





db_url = f'mongodb://localhost:27017/'
client = MongoClient(db_url)
database = "pharma"
db = client[database]