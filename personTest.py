from person import customer
import unittest

"""Limited Sample Data
ALFKI	Alfreds Futterkiste	Maria Anders	Sales Representative	Obere Str. 57	Berlin		12209	Germany	030-0074321	030-0076545
ANATR	Ana Trujillo Emparedados y helados	Ana Trujillo	Owner	Avda. de la Constitución 2222	México D.F.		05021	Mexico	(5) 555-4729	(5) 555-3745
ANTON	Antonio Moreno Taquería	Antonio Moreno	Owner	Mataderos  2312	México D.F.		05023	Mexico	(5) 555-3932	
AROUT	Around the Horn	Thomas Hardy	Sales Representative	120 Hanover Sq.	London		WA1 1DP	UK	(171) 555-7788	(171) 555-6750
BERGS	Berglunds snabbköp	Christina Berglund	Order Administrator	Berguvsvägen  8	Luleå		S-958 22	Sweden	0921-12 34 65	0921-12 34 67
"""

class testPerson(unittest.TestCase):
    
    def test_login(self):
        """ test different Parameters for login
        Test after database is done
        """
        AnaData = ["ANATR", "Ana Trujillo Emparedados y helados","Ana Trujillo", 
        "Owner", "Avda. de la Constitución 2222", "México D.F.", "", "05021",
        "Mexico", "(5) 555-4729", "(5) 555-3745"]

        thomData = ["AROUT", "Around the Horn", "Thomas Hardy", 
        "Sales Representative", "120 Hanover Sq.", "London", "", 
        "WA1 1DP", "UK", "(171) 555-7788", "(171) 555-6750"]

        testPerson = customer("testData", "ANATR", "Ana Trujillo Emparedados y helados", "Ana Trujillo")

        self.assertTrue(testPerson.checkUser())
 
        self.assertEqual(testPerson.getUID(), AnaData[0])
        self.assertEqual(testPerson.getCompany(), AnaData[1])
        self.assertEqual(testPerson.getName(), AnaData[2])
        self.assertEqual(testPerson.getTitle(), AnaData[3])
        self.assertEqual(testPerson.getAddress(), AnaData[4])
        self.assertEqual(testPerson.getCity(), AnaData[5])
        self.assertEqual(testPerson.getRegion(), AnaData[6])
        self.assertEqual(testPerson.getPostCode(), AnaData[7])
        self.assertEqual(testPerson.getCountry(), AnaData[8])
        self.assertEqual(testPerson.getPhone(), AnaData[9])
        self.assertEqual(testPerson.getFax(), AnaData[10])
        self.assertListEqual(testPerson.getInfo(), AnaData)

        testPerson.logout()
        self.assertFalse(testPerson.checkUser())

        testPerson.login("AROUT","Around the Horn","Thomas Hardy")
        self.assertTrue(testPerson.checkUser())

        self.assertEqual(testPerson.getUID(), thomData[0])
        self.assertEqual(testPerson.getCompany(), thomData[1])
        self.assertEqual(testPerson.getName(), thomData[2])
        self.assertEqual(testPerson.getTitle(), thomData[3])
        self.assertEqual(testPerson.getAddress(), thomData[4])
        self.assertEqual(testPerson.getCity(), thomData[5])
        self.assertEqual(testPerson.getRegion(), thomData[6])
        self.assertEqual(testPerson.getPostCode(), thomData[7])
        self.assertEqual(testPerson.getCountry(), thomData[8])
        self.assertEqual(testPerson.getPhone(), thomData[9])
        self.assertEqual(testPerson.getFax(), thomData[10])
        self.assertListEqual(testPerson.getInfo(), thomData)

        testPerson.logout()
        self.assertFalse(testPerson.checkUser())

    def test_GuestOrLogout(self): #TESTS: guest, logout, setters, getters
        """ TESTS IF GUEST PARAMETER, also test initialization"""
        gData = ["none", "guestComp", "Customer", None, None, None, None, None, None, None, None]
        testPerson = customer("testData", "ANATR", "Ana Trujillo Emparedados y helados", "Ana Trujillo")
        
        self.assertTrue(testPerson.checkUser())
        testPerson.logout()
        self.assertFalse(testPerson.checkUser())

        self.assertEqual(testPerson.getUID(), gData[0])
        self.assertEqual(testPerson.getCompany(), gData[1])
        self.assertEqual(testPerson.getName(), gData[2])
        self.assertEqual(testPerson.getTitle(), gData[3])
        self.assertEqual(testPerson.getAddress(), gData[4])
        self.assertEqual(testPerson.getCity(), gData[5])
        self.assertEqual(testPerson.getRegion(), gData[6])
        self.assertEqual(testPerson.getPostCode(), gData[7])
        self.assertEqual(testPerson.getCountry(), gData[8])
        self.assertEqual(testPerson.getPhone(), gData[9])
        self.assertEqual(testPerson.getFax(), gData[10])
        self.assertListEqual(testPerson.getInfo(), gData)
        
    def test_RegisterAndRemove(self):
        """ Create a Dummy Account and Remove it
        to be implemented after register and database is done
        """
        sampleData = ["MAKEN", "Mapua University", "Kyle Kenshin Morales", 
                    "Student", "Secret", "Manila", "", "111222", "Philippines", 
                    "09338128054", "NULL"]

        testPerson = customer("testData")
        testPerson.register("MAKEN", "Mapua University", "Kyle Kenshin Morales", 
                            "Student", "Secret", "Manila", "", "111222", "Philippines", "09338128054", "NULL")

        self.assertFalse(testPerson.register("MAKEN", "Mapua University", "Kyle Kenshin Morales", 
                            "Student", "Secret", "Manila", "", "111222", "Philippines", "09338128054", "NULL"))
        
        self.assertTrue(testPerson.login("MAKEN", "Mapua University", "Kyle Kenshin Morales"))
        
        self.assertTrue(testPerson.checkUser())

        self.assertEqual(testPerson.getUID(), sampleData[0])
        self.assertEqual(testPerson.getCompany(), sampleData[1])
        self.assertEqual(testPerson.getName(), sampleData[2])
        self.assertEqual(testPerson.getTitle(), sampleData[3])
        self.assertEqual(testPerson.getAddress(), sampleData[4])
        self.assertEqual(testPerson.getCity(), sampleData[5])
        self.assertEqual(testPerson.getRegion(), sampleData[6])
        self.assertEqual(testPerson.getPostCode(), sampleData[7])
        self.assertEqual(testPerson.getCountry(), sampleData[8])
        self.assertEqual(testPerson.getPhone(), sampleData[9])
        self.assertEqual(testPerson.getFax(), sampleData[10])
        self.assertListEqual(testPerson.getInfo(), sampleData)

        testPerson.setCompany("Edits")
        testPerson.setName("Edits")
        testPerson.setTitle("Edits")
        testPerson.setAddress("Edits")
        testPerson.setCity("Edits")
        testPerson.setRegion("Edits")
        testPerson.setPostCode("Edits")
        testPerson.setCountry("Edits")
        testPerson.setPhone("Edits")
        testPerson.setFax("Edits")
        testPerson.updateRecords()

        self.assertNotEqual(testPerson.getUID(), "Edits")
        self.assertEqual(testPerson.getCompany(), "Edits")
        self.assertEqual(testPerson.getName(), "Edits")
        self.assertEqual(testPerson.getTitle(), "Edits")
        self.assertEqual(testPerson.getAddress(), "Edits")
        self.assertEqual(testPerson.getCity(), "Edits")
        self.assertEqual(testPerson.getRegion(), "Edits")
        self.assertEqual(testPerson.getPostCode(), "Edits")
        self.assertEqual(testPerson.getCountry(), "Edits")
        self.assertEqual(testPerson.getPhone(), "Edits")
        self.assertEqual(testPerson.getFax(), "Edits")
        
        testPerson.unRegister()
        self.assertFalse(testPerson.checkUser())
        
        self.assertFalse(testPerson.login("MAKEN", "Mapua University", "Kyle Kenshin Morales"))

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