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

        id = input("Please Enter Item ID")

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

    def buy():
        pass

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

        return

def main():
    startApp = storeManage()
    startApp.start()

if __name__ == '__main__':
    main()