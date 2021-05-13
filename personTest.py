from person import customer
import unittest

class testPerson(unittest.TestCase):
    
    def test_login(self):
        """ test different Parameters for login
        Test after database is done
        """
        pass

    def test_GuestOrLogout(self): #TESTS: guest, logout, setters, getters
        """ TESTS IF GUEST PARAMETER, also test initialization"""
        testUser = customer()
        self.assertEqual(testUser.getName(),"Customer")
        self.assertEqual(testUser.getUID(), "none")
        self.assertTrue(testUser.verifyPassword(None))

        """ Test for Setters """
        testUser.setName("JOHN")
        testUser.setPassword("Testing")
        testUser.setUID("random UID")
        testUser.addRemoveRp(10)
        

        self.assertEqual(testUser.getName(),"JOHN")
        self.assertTrue(testUser.verifyPassword("Testing"))
        self.assertEqual(testUser.getUID(), "random UID")
        self.assertEqual(testUser.getRp(), 10)
        """ Test for logout """      
        testUser.logout()
        self.assertEqual(testUser.getName(),"Customer")
        self.assertEqual(testUser.getUID(), "none")
        self.assertEqual(testUser.getRp(), 0)
        self.assertTrue(testUser.verifyPassword(None))

    def test_RegisterAndRemove(self):
        """ Create a Dummy Account and Remove it
        to be implemented after register and database is done
        """
        pass

    def test_addRemoveCart(self):
        """ Tests for addition or removal of item """
        itemDict = {
                    "Item1": {'name': 'bread', 'price': 2.5, 'qty': None}, 
                    "Item2": {'name': 'wine', 'price': 4, 'qty': None},
                    "Item3": {'name': 'grapes', 'price': 1, 'qty': None}
                    }
                    
                     #testing for quantity is on other object
        """ Tests for addition of Item"""
        testUser = customer()
        testUser.addCart("Item1", 3, 2.5)
        testUser.addCart("Item2", 1, 4)
        testUser.addCart("Item3", 2, 1) 
        
        cartList = [{'ID':"Item1",'amt':3,'price':2.5},{'ID':"Item2",'amt':1,'price':4},{'ID':"Item3",'amt':2,'price':1}]

        """ Tests for getting the Item  """
        self.assertListEqual(testUser.getCart(), cartList, 'Check if Listing is correct') 
        self.assertEqual(testUser.getCart()[0], cartList[0], "test for getting the list of dictionary cart")
        self.assertEqual(itemDict[testUser.getCart()[1]['ID']], {'name': 'wine', 'price': 4, 'qty': None}, "Test for output")
        self.assertEqual(testUser.getItem(2), cartList[2], 'test for getItem() function')
        self.assertEqual(testUser.getItem_str("Random Thing"), None)
        
        """ Tests for Removing Items """
        self.assertTrue(testUser.removeCart("Item2"), 'tests to see if search function works')
        cartList.pop(1)
        self.assertListEqual(testUser.getCart(), cartList, 'test if the lists still holds')
        self.assertEqual(testUser.getCart()[1]['ID'], 'Item3', 'Tests to see if Item 3 got moved up after removal')
        self.assertTrue(testUser.lessenProd("Item1", 1), 'test to see if item is found')
        self.assertEqual(testUser.getItem(0)['amt'], 2, 'tests if there is subtraction')
        
        """ Test for Item Adding """
        testUser.addCart("Item1", 1, 2.5)
        self.assertListEqual(testUser.getCart(), cartList, 'test if the lists still holds')

        """ Test for Clearing Cart """
        testUser.clearCrt()
        self.assertEqual(testUser.getCart(), [])

    def test_rewardPts(self):
        """ Test For Reward Points System 
        Implement After Creation of Customer Database
        """