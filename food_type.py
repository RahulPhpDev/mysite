import db as database
import time

from bson.objectid import ObjectId

class FoodType:
    if __name__  == "__main__":
        def __init__(self):
            typeOpt =  input( "Check 1 for Type Options :: ")
            if(typeOpt == 1):
                options = {
                    "1" : "All Food Type",
                    "2" : "Add Food Type",
                    "0" : "Back"
                }
            for opt,optV in options.items():
                print(opt+" ==> "+optV)

            selectOpt = input("Select Any Options :: ")
            time.sleep(3)
            if(selectOpt == 1):
                self.FoodTypeList()
            elif(selectOpt == 2):
                self.addFoodType()


    def addFoodType(self):
        name = str(input("Enter Food Type Name: "))
        if((len(name) > 1) and (len(name) < 17)):
            collectionList = database.DB.list_collection_names()
            if "food_type" in collectionList:
                food_data = {"name": name, "status": "Active"}
                x =  database.DB["food_type"].insert_one(food_data)
                if(x.inserted_id):
                    time.sleep(3)
                    self.FoodTypeList()

    def FoodTypeList(self):
        print("======== Here is List =====")
        allType = database.DB["food_type"].find()

        for typeF in allType:
            # typeF['_id'],
            print(str(typeF['name']), typeF['_id'])
        time.sleep(3)
        option = int(input("1 For Edit, 2 For Delete : "))
        if option == 1:
          uId =  str(input("Give Us Id : "))
          findData  =  database.DB["food_type"].find({"_id": ObjectId(uId)})
          time.sleep(3)
          self.editFoodType(uId)
        elif option == 2:
          uId =  str(input("Give Us Id : "))
          findData  =  database.DB["food_type"].find({"_id": ObjectId(uId)})
          if(findData):
              time.sleep(3)
              self.deleteFoodType(uId)


    def deleteFoodType(self, id):
        # print("======== Here is List =====")
        myquery = {"_id":  ObjectId(id)}
        result = database.DB["food_type"].delete_one(myquery)
        time.sleep(3)
        self.FoodTypeList()

    def editFoodType(self, id):
        print("============== Want to Edit ========== ")
        # indData = database.DB["food_type"].find({"_id": ObjectId(uId)})
        idData = database.DB["food_type"].find_one({"_id" : ObjectId(id)})
        print("Name :: "+str(idData['name']))
        newName = str(input("Update Name : "))
        if((len(newName) > 1) and (len(newName) < 17)):
            food_data = {"name": newName}
            myquery = {"_id": ObjectId(id)}
            newvalues = {"$set": food_data}

            x = database.DB["food_type"].update_one(myquery, newvalues)
            if x:
                time.sleep(1)
                print("============== Successfully  Edit ========== ")
                time.sleep(2)
                self.FoodTypeList()
            else:
               time.sleep(3)
               inp =  int(input("Error Insert 1 For View List"))
               if inp == 1:
                 self.FoodTypeList()

    def FoodTypeListForInsert(self):
        print("======== Here is Food Type List =====")
        allType = database.DB["food_type"].find({'status': 'Active'})
        for type in allType:
            print(int(type['food_type']), str(type['name']))


# str(my_list[0])
ftObj = FoodType()