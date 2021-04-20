import sqlite3
import datetime

class customer(object):
    
    def __init__(self, shop, username = 'guest', password = 'guest'):
        """ Initialization of Data """
        self.monthList = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "Septmber", "October", "November", "December")
        self.login(username, password)
        self.cashier = shop
        self.cart = []

    def login(self, username, password):
        """ Sets Up Personal Infrmation for Certain Usernames """
        conn = sqlite3.connect('database/customers.db')

        c = conn.cursor()
    
        c.execute("Select * FROM customers WHERE username LIKE {} AND password LIKE {}".format(username, password))

        if c.rowcount() == 0:
            self.guest()
            return "ERROR CREDS"
        
        user = c.fetchall()
        self.name = user[0]
        self.UID = user[1]
        self.expData = {"month":user[2], "day":user[3], "year":user[4]}
        return "Successful"  

    def guest(self):
        """ Sets All Default Information As Default Guest """

        self.name = "Guest"
        self.UID = 0
        self.expData = {"month":None,"day":None, "year":None}

    def checkExp(self):
        """ Check if reward card should be renewed
            Might be Removed Later
        """
        pass

    def addToCart(self, itemID):
        """ Adds the Cart The Item ID to be handled by other programs """
        self.cart.append(itemID)

    def getTotal(self):
        """ Requires The Class Shop to Compute Total """
        pass
        """ expected return is integer
        return cashier.getTotal()
        """
    
    def getCart(self):
        """ Requires Shop Class"""
        pass
        #return cashier.getItemList()

    def clearCart(self):
        self.cart.clear()
    
    def pay(self,total,payment):
        pass
        """ return Bool 
        0: Failed Transaction
        1: Successful Transaction 
        # return cashier.payTotal(getTotal(), payment) 
        """

    def shop(self):
        "Main Program To Run"
        pass
