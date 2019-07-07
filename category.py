import db as database
import subprocess
import time
from bson.objectid import ObjectId

class Category:
    table = database.DB['category']
    print(__name__)
    if __name__ == "__main__":
        def __init__(self):
            print("Print 1 for Category List :: ")
            print("Print 2 for Add Category :: ")
            print("Print 3 for Exit :: ")
            indata =  int(input(""))
            time.sleep(1)
            if(indata == 1):
                self.categoryList()
            elif(indata == 2):
                self.addCategory()
            elif(indata == 3):
                self.exit()

    def categoryList(self):
        allCategory =  database.DB["category"].find()
        for cate in allCategory:
            print(cate['cat_id'] , str(cate['name']))

        time.sleep(1)
        print("1 for edit")
        print("2 for Delete")
        print("3 for Previous Menu")
        opt = int(input(""))
        optInput =  int(input("Give ID :: "))
        print(opt)
        if(opt == 1):
         self.editCategory(optInput)
        elif(opt == 2):
         self.deleteCategory(optInput)
        else:
         self.editCategory(optInput)



    def editCategory(self, catId):
       catData =  database.DB['category'].find_one({"cat_id":catId})
       print(catData['name'])
       newName = str(input("Give New Name for Category :: "))

       cat_data = {"name": newName}
       myquery = {"cat_id": catId}
       newvalues = {"$set": cat_data}

       x = database.DB["category"].update_one(myquery, newvalues)
       if(x):
           print(" Data Updated :: List Show in few Minute ")
           time.sleep(0.3)
           self.categoryList()
       else:
        print("uncommon data")

    def deleteCategory(self, id):
        print("======= In Category Delete ==========")
        condition = {"cat_id": id}
        xx = database.DB["category"].delete_one(condition)
        self.categoryList()
        # print("Are you sure to delete")


    def addCategory(self):
        print("You want to add new data :: ")
        cat_name = str(input("Enter Category Name :: "))
        lastCategory = database.DB["category"].find().sort([('cat_id', -1)]).limit(1)
        lastCateID = 0
        if(lastCategory):
            lastCateID = lastCategory[0]['cat_id']
            # lastCateID = lastCateID+1

        insertData = {"status": 1, "cat_id" : lastCateID + 1, "name" : cat_name}
        res = self.table.insert_one(insertData)
        if(res):
         print("Data Inserted ")
         self.categoryList()
        else:
         print("Data Not Inserted: ")

    def exit(self):
        exit()
        
    # @staticmethod
    def categoryListForInsert(self):
        allCategory =  database.DB["category"].find({"status": 1})
        for cate in allCategory:
            print(cate['cat_id'] , str(cate['name']))    

obj = Category()
# obj.categoryListForInsert()