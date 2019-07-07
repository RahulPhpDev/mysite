import user
class Outlet:
    
    def __init__(self):
        print(" 1 for Order Food \n 2 For Login \n 3 for Register ")
        choice =  int(input( " Your Choice ") )    
        if choice == 3:
            print("food")
            user.userObj.register()



outletObj = Outlet()

