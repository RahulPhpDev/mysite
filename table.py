import sys
def table():
    tableHeading = ["name", "address", "work"]
    dataDect = {
        '1': {
            'name' :'Rahul1',
            'address' : 'Noida1',
            'work' : 'PHP1'
        },
        '2': {
            'name' :'Rahul2',
            'address' : 'Noida2',
            'work' : 'PHP2'
        },
        '3' :{
            'name' :'Rahul3',
            'address' : 'Noida3',
            'work' : 'PHP3'
        },
    }
    # print(dataDect)
    k = 7
    # print(" "),
    for i in range(k):
        print("-"*k),
        # if k == k-1:
        #     print(" ")
    print("")    
    for j in range(i):
        # print(j)
        # print(" "*(j)),
        print( " "*(j+2)),
        if 0 <= j < len(tableHeading):   
            print(tableHeading[j]),

    print("") 

    for m in range(k):
        print("-"*k),
        # if k == k-1:
        #     print(" ")
    print("") 

    for key,data in dataDect.items():
        print(data["name"]),

        for pp in range(i/2):
            print( " "*(pp)),
        print(data['address']),

        for s in range(i):
            
            print( ""),
        print(data['work'])
        # for d in range(i):
        #     print( " "*(d+2)),
        # # if 0 <= j < len(tableHeading):   
        #     print(data['work'])   


           # if(i == k-1):
        #     for r in range(k):
        #         if r == 0:
        #             print("\n")
        #         print("|"),
        #         print(" "*((k*2)/2)),
        #         print("|")    
        #     for j in range(k):
        #         if(j == 0):
        #             print(" "),
        #         print("="),
                

        # if b == 3:
            # print("")
            

                # if(j == 3):
                #     for b in range(4):
                #         # print(" "*6)
                #         print("_"),



table()        