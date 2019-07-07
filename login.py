import custom_helper as helper
import db as database
from datetime import datetime
class Login:
    def __init__(self):
        self.index()

    def index(self):
        # email = (input("Enter Email :: "))
        email = 'rahul@gmail.com'
        password = '12345'    

        # password = (input("Enter Password :: "))    
        myDict = {"email" : email, 'password' :password }
        # print(myDict)
        self.passLogin(myDict)


    def validate_pass_login(func):
        def check_for_cred(self,myDict):
            if(myDict['email'] == ''):
                return False
            if(myDict['password'] == ''):
                return False   
            emailExist = database.DB['users'].find_one({'email':myDict['email']})
            if(emailExist):
                encrypt_password = helper.decryptPassowrd(b'fdds')
                print(encrypt_password)
                # if(encrypt_password == myDict['password']):
                #     print("Here is details")
                #     func() 
                # else:
                #     print('Password is wrong')
                #     pass
            else:
                print('Email Is not Exist') 
                pass  

           
        return check_for_cred
    

    @validate_pass_login
    def passLogin(self, myDict):
        print('Hello')






loginObj = Login()
# loginObj.index()        