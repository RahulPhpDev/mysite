import time
import db as database
import category as cat
import food_type as foodtype

class Food:

    # if __name__ == '__main__':
    #     print("main")

    def addFood(self):
        print("===== Add Food =====")
        foodName = str(input("Give Food Name :: "))
        print("Give ID for select Category :: ")
        x = cat.obj
        x.categoryListForInsert()

        categoryId =  int(input("Give ID :: "))

        #food Type
        foodtype.ftObj.FoodTypeListForInsert()

        foodTypeID = int(input("Give food Type Id :: "))
        status = 1
        foodID = 0
     
        foodDataOfLast = database.DB["food"].find().sort([('food_id' , -1)]).limit(1)
     
        if foodDataOfLast:
              foodID = foodDataOfLast[0]['food_id']
        insData = {
            "name" : foodName,
             "type_id" : foodTypeID, 
             "category_id" : categoryId,
             'status' : 1,
             'food_id' : foodID+1
             }

        insert = database.DB["food"].insert_one(insData)
        if insert:
            print(" Food Inserted ")


    def foodList(self):
        print("Here is The Food List")
        foodListData = database.DB["food"].find({"status" : 1})
        table = database.DB['food']
        allData = table.aggregate([
            {
                "$lookup":
                {
                    "from" : 'category',
                    "localField": 'category_id',
                    "foreignField": 'cat_id',
                    "as" : 'category'
                },
            },
            {
                "$lookup":
                {
                    "from":"food_type",
                    "localField" :"type_id",
                    "foreignField" : "food_type",
                    "as" : "foodtype"
                }
            },
        { "$unwind": { "path": "$category", "preserveNullAndEmptyArrays": True }},
        { "$unwind" : {"path" : "$foodtype", "preserveNullAndEmptyArrays" : True} },
        ])
        k = 7
        tableHeading = ["ID", "Name", "Category", "Type"]
        for i in range(k):
            print("-"*k),
        print("")  

        for j in range(i):
            print( " "*(j+2)),
            if 0 <= j < len(tableHeading):   
                print(tableHeading[j]),

        print("") 

        for m in range(k):
            print("-"*k),
        print("")  
        
        for data in allData:
            print(data["food_id"]),
            for pp in range(i/2):
                print( " "*(pp)),
            print(data['name']),
            for pp in range(i/2):
                print( " "*(pp)),
            print(data['category']['name']),
            for pp in range(i/2):
                print( " "*(pp)),
            print(data['foodtype']['name'])
            time.sleep(0.5)
        time.sleep(1)    
        print("Enter 1 For Edit ")
        print("Enter 2 For Delete ")
        choice = int(input("Choice :: "))

obj = Food()
obj.foodList()
