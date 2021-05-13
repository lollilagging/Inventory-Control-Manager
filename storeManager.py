from person import customer
""" The Main Logic """

class manager(object):
    """ The Class If Manager """


class cashier(object):
    """ The class for handling selling """
    cust = customer()
    shopDict = {}

    def login(self, userID, CN, currentUser) :
        self.cust(userID,CN,currentUser)

    def initializeDict(self) :
        """ shopdictionary = {prodID : {name, price}} """
        pass