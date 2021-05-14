import sqlite3
from unittest.runner import TextTestRunner
#import Cashier/Cashier

class customer(object): #LOGIC

    def __init__(self, dataName = "northwind", uid = "guest", CN = 'guestComp', currentUser = 'guest'):
        """ Initialization of Data """
        self.database = dataName
        self.login(uid, CN, currentUser)
        self.cart = []
    
    def login(self, userID = "guest", CN="guestComp", currentUser="guest"): 
        """ Sets Up Personal Infrmation for Certain Usernames """
        if userID  == "guest" and CN == "guestComp" and currentUser == "guest": 
            self.guest()
            self.guestUser = True
            return True

        conn = sqlite3.connect('database/' + self.database + '.db')
        c = conn.cursor()
        c.execute("Select * FROM customers WHERE customer_id LIKE '{}' AND company_name LIKE '{}' AND contact_name LIKE '{}'".format(userID, CN, currentUser))
        
        user = c.fetchone()
        if user == None:
            self.guest()
            self.guestUser = True
            return False

        self.UID = user[0]
        self.companyName = user[1]
        self.name = user[2]
        self.title = user[3]
        self.address = user[4]
        self.city  = user[5]
        self.region = user[6]
        self.postalCode = user[7]
        self.country = user[8]
        self.phone = user[9]
        self.fax = user[10]

        self.guestUser = False

        conn.commit()
        conn.close()
        return True  

    def register(self, uid, company, newName, newTitle, newAddress, 
                newCity, newRegion, newPostal, newCountry, newPhone, 
                newFax):
        """registers the user to the database of the shop, also checks for same name"""
        check = False
        conn = sqlite3.connect('database/' + self.database + '.db')

        c = conn.cursor()

        if self.checkUnique(uid):
            c.execute("""INSERT INTO customers VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(uid, company, newName, newTitle, newAddress, 
                    newCity, newRegion, newPostal, newCountry, newPhone, newFax))
            check = True
        else:
            check = False
        conn.commit()
        conn.close()

        self.login(uid,company,newName)

        return check

    def checkUnique(self, id):
        check = True
        conn = sqlite3.connect('database/' + self.database + '.db')

        c = conn.cursor()

        c.execute("""SELECT customer_id FROM customers WHERE customer_id = '{}'""".format(id))

        checkID = c.fetchone()
        if not checkID == None:
            check = False

        return check

    def unRegister(self) : 
        if not self.guestUser:
            conn = sqlite3.connect('database/' + self.database + '.db')
            c = conn.cursor()
            c.execute("DELETE from customers WHERE customer_id = '{}'".format(self.UID))
            conn.commit()
            conn.close()
            self.guest()
            self.guestUser = True          
        return

    def checkUser(self):
        """ Check if the User is Logged In"""
        return not self.guestUser
        
    def checkAvail(self, uid, company, newName):
        """ Check if user is available """
        conn = sqlite3.connect('database/' + self.database + '.db')
        c = conn.cursor()
        c.execute("SELECT EXISTS(SELECT 1 FROM customers WHERE customer_id = '{}')".format(uid))
        if c.fetchone():
            return False
        c.execute("SELECT EXISTS(SELECT 1 FROM customers WHERE contact_name = '{}' AND company_name = '{}')".format(newName, company))
        if c.fetchone():
            return True
        else:
            return True
            

    def guest(self):
        """Logs Out, Guest Account Init"""
        self.UID = "none"
        self.companyName = "guestComp"
        self.name = "Customer"
        self.title = None
        self.address = None
        self.city  = None
        self.region = None
        self.postalCode = None
        self.country = None
        self.phone = None
        self.fax = None

        return
    
    def logout(self): 
        self.guest()
        self.guestUser = True

    def addCart(self, prodID, amt, price): 
        """ Adds the prodId and the amount for the cart ,,, CART DESIGN: [{ID, amt, price}]"""
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
        """ CLEAR OUT CART """
        self.cart.clear()
        return

    def getCart(self):
        """ returns list of dictionaries for cart
        Requires The List of Items in the shops dictionary to be viewed
        shopdictionary = {prodID : {name, price}}
        """
        return self.cart

    def getItem(self, index = 0):
        """ Return a Specific Item in Index 'index' from cart"""
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

    """def setUID(self, newUID):
        
        conn = sqlite3.connect('database/' + self.database + '.db')
        c = conn.cursor()
        if self.checkUnique():
            self.UID = newUID
            c.execute("UPDATE customers SET customer_id = '{}'".format(self.UID))
            
            conn.commit()
            conn.close()""" #CANNOT BE DUE TO UNIQUE ATTRIBUTE

    def setCompany(self, newComp):
        self.companyName = newComp
        
    def setName(self, newName):
        self.name  = newName

    def setTitle(self, newTitle):
        self.title  = newTitle

    def setAddress(self, newAdd):
        self.address  = newAdd
    
    def setCity(self, newCity):
        self.city = newCity

    def setRegion(self, newRegion):
        self.region = newRegion

    def setPostCode(self, newPC):
        self.postalCode = newPC

    def setCountry(self, newCountry):
        self.country = newCountry
    
    def setPhone(self, newPhone):
        self.phone = newPhone

    def setFax(self, newFax):
        self.fax = newFax

    def updateRecords(self):
        """ Commit to SQLite Database """
        conn = sqlite3.connect('database/' + self.database + '.db')
        c = conn.cursor()
        c.execute("""UPDATE customers SET company_name = '{}', 
                    contact_name = '{}', contact_title  = '{}', 
                    address = '{}', city = '{}', region = '{}', postal_code = '{}', country = '{}', phone = '{}', 
                    fax = '{}' WHERE customer_id = '{}'""".format(self.companyName, self.name, 
                    self.title, self.address, self.city, self.region, self.postalCode, 
                    self.country, self.phone, self.fax, self.UID))
        conn.commit()
        conn.close()

    def getCompany(self):
        return self.companyName
        
    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getAddress(self):
        return self.address
    
    def getCity(self):
        return self.city

    def getRegion(self):
        return self.region

    def getPostCode(self):
        return self.postalCode

    def getCountry(self):
        return self.country
    
    def getPhone(self):
        return self.phone

    def getFax(self):
        return self.fax

    def getUID(self): 
        return self.UID

    def getInfo(self):
        """ get all information in one go"""
        return [self.UID, self.companyName, self.name, 
        self.title, self.address, self.city,
        self.region, self.postalCode, self.country, 
        self.phone, self.fax]

    def verifyUser(self, id, User, Company):
        """ Input UID, CUSTOMER NAME/REPRESENTATIVE, COMPANY. to check validity """
        return self.companyName == Company and self.UID == id and self.name == User 

    def __str__(self):
        """ returns all attributes as string """
        pass 

        
