from person import customer
from inventoryManager import inventoryManager
""" The Main Logic """

key = "x1x1"
class storeManage(object):
    def __init__(self, dataName = "northwind"):
        """ A Class For Fetching Information From Object"""
        self.database = dataName

    def printItems(self, itemList , invMan = inventoryManager("northwind")):
        for items in itemList:
            print("{}: {}, amt: {}".format(invMan.getProdInfo(items[0],0)[0], 
            invMan.getProdInfo(items[0],1)[0], invMan.getProdInfo(items[0],6)[0]))

    def retNull(self, inp):
        if inp == "None" or inp == "none":
            return "NULL"
        else :
            return inp

    def addItem(self, itemList, invMan = inventoryManager("northwind")):
        prod_id = int(input("Please Enter Product Id: "))
        allow = False
        for check in itemList:
            allow = not check == prod_id
            if not allow: 
                print("ID NOT AVAILABLE, RETURNING...")
                return
        print("Enter None for Null input")
        product_name = self.retNull(input("Product Name?: "))
        supplier_id = int(input("Supplier ID?: "))
        category_id = int(input("Category ID?: "))
        quantity_per_unit = input("Quantity Per Unit?: ")
        unit_price = float(input("Unit Price?: "))
        units_in_stock = int(input("Units in Stock?: "))
        units_on_order = int(input("Units On Order?: "))
        reorder_level = int(input("Reorder Level: "))
        discontinued = 0

        if unit_price >= 0:
            invMan.addNewItem(prod_id, product_name, supplier_id, category_id, 
            quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued)

        return

    def qtyManage(self, itemList, invMan = inventoryManager("northwind")):
        self.printItems(itemList, invMan)

        found = False

        id = input("Please Enter Item ID")

        for check in itemList:
            if id == check:
                found = True

        if found == True:
            itemAmt = invMan.getProdInfo(id, 6)
            print("Item Has {} Amount of Units".format(itemAmt))
            negPos = input("[0]Add; [1]Subtract")
            if negPos:
                add = -input("Subtract By How Much?")
            else:
                add = input("Add By How Much?")

            if not invMan.addSubQty(add, id):
                print("Failed To Subtract, Theres isn't enough quantity")

        else:
            print("Item Id not Found, Check Spelling")
        

    def removeItem(self, itemList, invMan = inventoryManager("northwind")):
        self.printItems(itemList, invMan)

        found = False

        id = int(input("Please Enter Item ID"))

        for check in itemList:
            if id == check:
                found = True
        
        if found:
            confirm = input("Are you sure you want to remove product {}?".format(invMan.getProdInfo(id,1)))
            if confirm:
                inventoryManager.removeItem(id)
        else:
            print("Item Id not Found, Check Spelling")

    def getProdInfo(self, itemList, invMan = inventoryManager("northwind")):

        column = ("product_id","product_name","supplier_id","category_id",
        "quantity_per_unit","unit_price","units_in_stock","units_on_order",
        "reorder_level","discontinued")

        found = False

        self.printItems(itemList, invMan)

        id = input("Please Enter Item ID")
        ctr = 0

        for check in itemList:
            if id == check:
                found = True

        if found:
            print("Please Select What Kind Of Data")
            for type in column:
                print("[{}] : {}".format(ctr, type))
                ctr = ctr+1
            ctr = 0
            choice = input("-->")

            if choice >= 0 and choice < 10:
                print(invMan.getProdInfo(id, choice))
            else:
                print("Input was Invalid")
        else:
            print("Item Id not Found, Check Spelling")

    def updateInfo(self, invMan = inventoryManager("northwind")):
        pass

    def manage(self):
        invMan = inventoryManager(input("Please Enter The Database File: "))
        itemList = invMan.getAllProdId()
        cont = True

        while cont:
            option = int(input("""Choose What You Want To Do?: 
                    1. Print Lists of Items
                    2. Add New Item
                    3. Add or Subtract Qty
                    4. Remove Item from Data
                    6. Update Item Information
                    7. Quit
                    ---> """))
            if option == 1:
                self.printItems(itemList, invMan)
            elif option == 2:
                self.addItem(itemList, invMan)
            elif option == 3:
                self.qtyManage()
            elif option == 4:
                self.removeItem()
            elif option == 5:
                self.getProdInfo()
            elif option == 6:
                self.updateInfo()
            elif option == 7:
                cont = False
            else:
                print("Error Input")
        return

    """ BUY PART """

    def print2Dictionary(self, dict, ids):
        for id in ids:
            print("|ID: {}| NAME: {}| PRICE: {}| QTY: {}|".format(id[0], dict[id[0]]["NAME"], dict[id[0]]["PRICE"], dict[id[0]]["QTY"]))
        return

    def checkExist(self, inItem, list):
        for item in list:
            if inItem == item[0]:
                return True
        return False
    
    def checkValidQty(self, amount, id, itemDict):
        return itemDict[id]["QTY"] >= amount and amount >= 0

    def buy(self):
        buyer = customer()
        cashier = inventoryManager()
        itemList = cashier.getAllProdId()
        done = 1
        cont = 1
        itemDict = {}

        for item in itemList:
            itemDict.update({item[0] : {"NAME" : cashier.getProdInfo(item[0],1)[0], "PRICE" : cashier.getProdInfo(item[0],5)[0], "QTY" : cashier.getProdInfo(item[0],6)[0]}})
        # ITEM DICTIONARY : {ID : {NAME:-, PRICE:-, QTY:-}}

        log = int(input("Are you a new customer or old customer: (0/1)"))

        while done == 1:
            if log == 1:
                id = input("Please Enter Your ID: ")
                name = input("Please Enter Your Full Name: ")
                comp = input("Please Enter The Company You Belong: ")
                if buyer.login(id, comp, name):
                    print("Successful Login")
                    done = 0
                else:
                    done = input("Login Failed, Do You Wish To Try Again (0/1)")
            else :
                done = 0
                    
        while cont == 1:
            choice = int(input(""" Please Choose What You Want To Do: 
                    1: add to cart
                    2: remove from cart
                    3: clear cart
                    4: show cart items
                    5: finalized order
                    6: login/logout
                    7: quit
                    """))

            if choice == 1:
                done = False
                self.print2Dictionary(itemDict, itemList)
                id = int(input("Please Enter Item Id: "))
                done = self.checkExist(id, itemList)
                if not done:
                    print("No Id Found, Returning")
                else:
                    amount = int(input("Enter Amount: "))
                    if self.checkValidQty(amount, id, itemDict):
                        buyer.addCart(id, amount, itemDict[id]["PRICE"])
                        itemDict[id]["QTY"] = itemDict[id]["QTY"] - amount
                    else:
                        print("Input Invalid")

            elif choice == 2:
                for item in buyer.getCart():
                    print("|{}| Name: {} | Qty: {} | Price: {} | Total: {}".format(item["ID"], itemDict[item["ID"]]["NAME"], item["amt"], item["price"], item["price"]*item["amt"]))
                
                remItem = int(input("Please Enter The Id of Removal: "))
                returnedItem = buyer.getItem_str(remItem) #ID amt price
                if buyer.removeCart(remItem):
                    itemDict[returnedItem["ID"]]["QTY"] = itemDict[returnedItem["ID"]]["QTY"] + returnedItem["amt"]
                    print("Successfully Removed Item")
                else:
                    print("ID not found in cart")

            elif choice == 3:
                if int(input("Are You Sure(0/1): ")) == 1:
                    returnedItems = buyer.getCart()
                    for item in returnedItems:
                        itemDict[item["ID"]]["QTY"] = itemDict[item["ID"]]["QTY"] + item["amt"]
                    buyer.clearCrt()

                    print("Cart Cleared")
                else:
                    print("Cart Not Cleared")

            elif choice == 4:
                sum = 0
                for item in buyer.getCart():
                    print("|{}| Name: {} | Qty: {} | Price: {} | Total: {}".format(item["ID"], itemDict[item["ID"]]["NAME"], item["amt"], item["price"], item["price"]*item["amt"]))
                    sum = sum + item["price"]*item["amt"]
                print(sum)
                
            elif choice == 5:
                sum = 0

                for item in buyer.getCart(): # {ID : {NAME, PRICE, QUANTITY}}
                    print("|{}| Name: {} | Qty: {} | Price: {} | Total: {}".format(item["ID"], itemDict[item["ID"]]["NAME"], item["amt"], item["price"], item["price"]*item["amt"]))
                    sum = sum + item['amt']*item['price']
                print(sum)
                
                if int(input("Are You Sure?(0/1): ")) == 1:
                    pay = float(input("How Much Money To Pay: "))
                    if pay >= sum:
                        for item in buyer.getCart():
                            cashier.addSubQty(-1*item['amt'], item['ID'])
                            print("Bought {} units of {} for ".format(item['amt'], itemDict[item['ID']]["NAME"], item['amt']*item['price']))
                        buyer.clearCrt()
                        print("Payment Successful; Change is {} Dollars".format(pay-sum))
                    else:
                        print("Payment Failed")
                else:
                    print("Returning")                


            elif choice == 6 :
                if buyer.checkUser():
                    inp = int(input("Logging Out Yes? (0/1)"))
                    if inp == 1:
                        buyer.logout()
                        print("Thank You For Using This Program!")
                    else :
                        print("Returning...")
                else:
                    inp = int(input("Do You Want To Login, Register, or Guest? (0/1/2): "))
                    if inp == 0:
                        id = input("Please Enter Your Specified ID: ")
                        CN = input("Please Enter Your Company: ")
                        User = input("Please Enter Your Full Name: ")
                        if buyer.login(id, CN, User):
                            print("Successfully Logged In")
                        else:
                            print("Failed To Log In, Check Credentials")
                    elif inp == 1:
                        uid = input("Please Enter 5 Letter id")
                        if buyer.checkUnique(uid) and len(uid) == 5:
                            print("New ID Created")
                            company = input("Please Enter Company: ")
                            newName = input("Please Enter Full Name: ")
                            newTitle = input("Please Enter Position in Company: ")
                            newAddress = input("Please Enter Address: ")
                            newCity = input("Please Enter City: ")
                            newRegion = input("Please Enter Region: ")
                            newPostal = input("Please Enter Postal: ")
                            newCountry = input("Please Enter Country: ")
                            newPhone = input("Please Enter Phone: ")
                            newFax = input("Please Enter Fax: ")
                            if buyer.register(uid, company, newName, newTitle, newAddress, newCity, 
                                            newRegion, newPostal, newCountry, newPhone, newFax) :
                                print("Successfully Registered")
                                buyer.login(uid,company,newName)
                            else:
                                print("Error")
                        else:
                            print("Invalid ID or Already Existing")

                    elif inp == 2: 
                        buyer.guest()

            elif choice == 7:
                cont = 0

            else:
                print("Input Error")
        return

    def start(self):
        choice = int(input("Manager or Customer(0/1): "))
        cont = 1
        while cont == 1: 
            if choice == 0 :
                check = (input("Please Enter Password: ") == key)
                if check:
                    self.manage()

                else :
                    print("Wrong Password")

            elif choice == 1:
                self.buy()

            else:
                print("""Error""")
            cont = int(input("Continue?: (0/1)"))
            if cont:
                choice = int(input("Manager or Customer(0/1): "))
        return

def main():
    startApp = storeManage()
    startApp.start()

if __name__ == '__main__':
    main()