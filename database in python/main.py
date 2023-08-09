import pymongo

client = pymongo.MongoClient("mongodb+srv://tushargupta2k3:tUshar%40123@twitter.fzbvq5v.mongodb.net")
database = client['ml']
collection = database['students']

d = {'name':'tushar','age':'20'}
rec = collection.insert_one(d)
d = [{'name':'tushar','age':'20'},{'name':'tushar','age':'20'}]
rec = collection.insert_many(d)
all_records = collection.find()

for record in (all_records):
    print(f"{record}")