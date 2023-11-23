#Create a Food Storage System which perform following Operation on it. 
#using OOPS Concept (Class and Object )

#Class Food has Following Properties (foodId, foodName, foodType(Veg/Non-Veg) ,foodPrice)


class Food:
    a = [] #Using List To Store Foods Temperory (Because Not Useing External files to store data)
    b = {} #Append one by one food to dict. then dict add to list
    def adddata(self, get): # Creating seperate function to avoid repition of code used in Add And Update food
        self.foodId = int(input(get + " Food Id: "))
        self.foodName = input(get + " Food Name: ")
        self.foodType = input(get + " Food Type (Veg/NonVeg): ")
        self.foodPrice = float(input(get + " Food Price: "))
    def data(self):  #to add Food
        while True:
            self.adddata("Enter")
            self.b["Id"] = self.foodId
            self.b["Food"] = self.foodName
            self.b["Type"] = self.foodType
            self.b["Price"] = self.foodPrice
            self.a.append(self.b.copy())
            con = input("Continue To Add Food Yes or No (Y/N): ")
            if(con == 'N' or con == "n"):
                break
                
        # print(self.a)
    def update(self):  #To Update Food
        ent = int(input("Enter food Id Want to update: "))
        for i in range(len(self.a)):
            if(self.a[i]['Id'] == ent):
                del self.a[i]
                self.adddata("Update")
                self.b["Id"] = self.foodId
                self.b["Food"] = self.foodName
                self.b["Type"] = self.foodType
                self.b["Price"] = self.foodPrice
                self.a.append(self.b.copy())
    def delete(self):   #To Delete foods
        self.a.clear()
        print("Food List Deleated....")
    def showbyid(self):  # To Show Food By Id
        ent = int(input("Enter Id of food: "))
        for i in range(len(self.a)):  #If enntered Id is correct then it shows other details
            if(ent == self.a[i]["Id"]):
                print(self.a[i])
                break
        else: #Else Not
            print("Id Not Found")
    def showbyname(self):
        ent = input("Enter Name of food: ")
        for i in range(len(self.a)):   #If entered food Name is correct then it show other details
            if(ent == self.a[i]['Food']):
               print(self.a[i])
               break
        else: #Else Not
            print("Name Not Found")
    def showbytype(self):  # show Food By type
        ent = input("Enter Type of food: ")
        for i in range(len(self.a)):
            if(ent == self.a[i]['Type']):
                print(self.a[i])
                break
            #If Entered type is found display food
            # if(ent == i['Type']):
            #     print(self.a[i])
            #     break
        else:  #Else not
            print("Type Not Found")
    def sortbyname(self):  #sort food by name
        newlist = sorted(self.a, key=lambda k: k['Food'])
        print(newlist)
    def sortbyprice(self):  #sorted by price
        newlist = sorted(self.a, key=lambda k: k['Price'])
        print(newlist)
    def open(self): #Show Stored Food in List
        if len(self.a) == 0:  # If list is empty show Message
            print("Food List is Empty Try Adding Foods...")
        else:  # if food list is not empty display foods
            for i in self.a:
                print(i)
# Object Data
def objectdata(): # defining Function because we have to run this program 2 times For Yes Condition And for No condition. Otherwise we have to write this code 2 times
    f = Food()
    print('1.Add Food \n2.Update Food \n3.Delete Food \n4.Show Food List\n5.Show Food by Id\n6.Show Food by Name\n7.Show Food by Type \n8.Sort Food List by Name\n9.Sort Food List by Price')
    choice = int(input("Enter a choice: "))
    if(choice == 1):
        f.data()
    elif(choice == 2):
        f.update()
    elif(choice == 3):
        f.delete()
    elif(choice == 4):
        f.open()
    elif(choice == 5):
        f.showbyid()
    elif(choice == 6):
        f.showbyname()
    elif(choice == 7):
        f.showbytype()
    elif(choice == 8):
        f.sortbyname()
    elif(choice == 9):
        f.sortbyprice()
    else:
        print("Invalid Choice")
objectdata()  # calling function first time
while True:
    choice = input("MAIN MENU.. (Y/N)")  # Get User Input
    if(choice == "y" or choice =="Y"):  # Ask User To show option
        objectdata()  #calling function 2nd time
    elif(choice == "n" or choice == 'N'): #if not code breaks
        break
    else:
        print("Invalid Choice")
