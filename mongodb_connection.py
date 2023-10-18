#mongodb connect with python pymongo lib

from pymongo import MongoClient
import bson

client = MongoClient('mongodb://localhost:27017')

#Access the DB

db_name = client['AT6DB']
collection_name = db_name['table_1']


#insetion part
# collection_name.insert_one({'ID': 106, 'Name': 'Sourav', 'Language': ['Java','Python'], 'Year': 2020})


# Fetching and Evaluate part
all_data  = collection_name.find()

li_at6_data = []
for data in all_data:
    li_at6_data.append(data)
print(li_at6_data)

# for i in li_at6_data:
#     lang = {i.get('Name'):i.get('Language')}
#     print(lang)

# for i in li_at6_data:
#     if i.get('ID') == 103:
#     print(i)

#ObjectId('652cacc590b1c3e662b86269')

# for i in li_at6_data:
#     # print(type(i.get('_id')))
#     a = bson.objectid.ObjectId('652cacc590b1c3e662b86269')
#     if i.get('_id')== a:
#         print(i)