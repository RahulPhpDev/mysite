import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
DB = myclient["resturantDB"]

# print(myclient.list_database_names())
# dblist = myclient.list_database_names()
# if "resturantDB" in dblist:
#
#   # print("The database exists.")
#
# else:
#   print("Error In Connection")