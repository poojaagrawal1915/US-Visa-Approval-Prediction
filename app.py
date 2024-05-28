import pymongo

DB_NAME='US_VISA'
COLLECTION_NAME='visa_data'
CONNECTION_URL='mongodb+srv://poojagrawal1915:poojagrawal1915@cluster0.ff9lvcf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client=pymongo.MongoClient(CONNECTION_URL)
print(client)
data_base=client[DB_NAME]
collection=data_base[COLLECTION_NAME]
rec=collection.insert_many(data)