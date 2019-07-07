import custom_helper as helper
import db as database
from datetime import datetime
class User:
    def register(self):
        first_name = str(input(" Enter Your First Name :: "))
        last_name = str(input(" Enter Your Last Name :: "))
        email = str(input(" Enter your Email :: "))
        password = (input(" Enter your Password :: "))
        encrypt_password = helper.encryptPassowrd(password)


        insert_data = {
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            'meta_password' : password,
            'password': encrypt_password,
            'status' : 1,
            'user_id' : (helper.getSequenceNumber('users')+1),
            'create_date': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        insertId = database.DB['users'].insert_one(insert_data)
        print(insertId)

    def user_list_by_id(self,user_id):
        userData = database.DB['users']


userObj = User()        
userObj.register()
