import sqlite3
#import Cashier/Cashier

class customer(object):

    monthList = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "Septmber", "October", "November", "December")
    rPRate = 1

    def __init__(self, UID = "guest", password = 'guest'):
        """ Initialization of Data """
        self.login(UID, password)
        self.cart = []
        self.password = None
        #ADD LATER THE rPRate Initialization
    
    def login(self, userID, password):
        """ Sets Up Personal Infrmation for Certain Usernames """
        
        if userID  == "guest" and password == "guest": 
            self.guest()
            return True

        conn = sqlite3.connect('database/customers.db')
        c = conn.cursor()
        c.execute("Select * FROM customers WHERE username LIKE {} AND password LIKE {}".format(userID, password))

        if c.rowcount() <= 0 or c.rowcount() > 1:
            self.guest()
            return False
        
        user = c.fetchall()

        self.name = user[0]
        self.UID = user[1]
        self.expData = {"month":user[2], "day":user[3], "year":user[4]}
        self.rp = user[5]
        return True  

    def register(self, Name, Password):
        """registers the user to the database of the shop, also checks for same name"""
        pass

    def guest(self):
        """Logs Out, Guest Account Init"""
        self.name = "Customer"
        self.UID = "none"
        self.expData = {"month":None, "day":None, "year":None}
        self.password = None
        self.rp = 0
    
    def logout(self): 
        self.guest()

    def addCart(self, prodID, amt, price): 
        """ Adds the prodId and the amount for the cart """
        found = False

        if len(self.cart) != 0:
            for index in range(0,len(self.cart)-1) : 
                if prodID == self.cart[index]['ID']:
                    self.cart[index]['amt'] = self.cart[index]['amt'] + amt
                    found = True

        if not found:
            self.cart.append({'ID':prodID, 'amt':amt, 'price':price})

    def removeCart(self, prodID):
        """ Remove An Item in The Cart """
        found = False
        for item in range(0, len(self.cart)-1):
            if prodID == self.cart[item]['ID'] :
                self.cart.pop(item)
                found = True
        return found

    def lessenProd(self, prodID, amt):
        """ Lessen the Item in the Cart (Subtract)"""
        found = False
        for item in self.cart : 
            if prodID == item['ID']:
                item['amt'] = item['amt'] - amt
                found = True
        return found
                
    def clearCrt(self):
        self.cart.clear()
        return

    def getCart(self):
        """ returns list of dictionaries for cart
        Requires The List of Items in the shops dictionary to be viewed
        shopdictionary = {prodID : {name, price}}
        """
        return self.cart

    def getItem(self, index = 0):
        """ Return a Specific Item in Index 'index' """
        if len(self.cart) == 0:
            return None
        return self.cart[index]
    
    def getItem_str(self, prodID):
        """ Return a Specific Item string """
        for item in self.cart : 
            if prodID == item['ID']:
                return item                
        return None

    def getTotal(self):
        totalPrice = 0
        for items in self.cart : 
            totalPrice = totalPrice + items['price']
        return totalPrice

    def setName(self, newName):
        self.name = newName

    def setPassword(self, newPass):
        self.password = newPass
    
    def setUID(self, args):
        self.UID  = args
    
    def verifyPassword(self, input):
        return self.password == input

    def setExpDate(self):
        pass
        """ Expected to create 
        a new valid expiration date for 
        registrations and renewal"""

    def changePtRate(self, newRate):
        self.rPRate  = newRate

    def resetRp(self):
        """ For Possible Reward System """
        self.rp = 0
    
    def addRemoveRp(self, amt):
        if amt >= 0 or self.rp > amt:
            self.rp = self.rp + amt
        else:
            return False
        return True

    def getRp(self):
        return self.rp
    
    def getUID(self): 
        return self.UID
    
    def getName(self): 
        return self.name

    def getExpDate(self): 
        return self.expData

    def __str__(self):
        """ returns all attributes as string """
        pass 

        
