import unittest
from inventoryManager import inventoryManager

class TestInventoryManager(unittest.TestCase):
    
    def test_addNewItem(self):
        
       addItem = inventoryManager()
       # addItem.addNewItem(1000, 'Cardboard Box', 44, 45, '1000 units', 46.0, 47, 0, 48, 1)
       sampleItem = (1000, 'Cardboard Box', 44, 45, '1000 units', 46.0, 47, 0, 48, 1)
       getItem = addItem.getProdRow(1000)
       self.assertEqual(getItem, sampleItem)

    def test_removeItem(self):
        pass
    
        

    def test_changeData(self):
        pass

    def test_changeID(self):
       pass

    

    def test_getProdInfo(self):
        sampleObject = inventoryManager()    
        sampleProduct = [(1,), ('Chai',),(8,) , (1,),("10 boxes x 30 bags",),  (18,), (39,), (0,),  (10,), (1,)  ]

        
        self.assertEqual(sampleObject.getProdInfo('product_id',0), sampleProduct[0])
        self.assertEqual(sampleObject.getProdInfo('product_id',1), sampleProduct[1])
        self.assertEqual(sampleObject.getProdInfo('product_id',2), sampleProduct[2])
        self.assertEqual(sampleObject.getProdInfo('product_id',3), sampleProduct[3])
        self.assertEqual(sampleObject.getProdInfo('product_id',4), sampleProduct[4])
        self.assertEqual(sampleObject.getProdInfo('product_id',5), sampleProduct[5])
        self.assertEqual(sampleObject.getProdInfo('product_id',6), sampleProduct[6])
        self.assertEqual(sampleObject.getProdInfo('product_id',7), sampleProduct[7])
        self.assertEqual(sampleObject.getProdInfo('product_id',8), sampleProduct[8])
        self.assertEqual(sampleObject.getProdInfo('product_id',9), sampleProduct[9])

    def test_getProductRow(self):
        sampleObject2 = inventoryManager()
        sampleProduct = (1, 'Chai', 8, 1,"10 boxes x 30 bags", 18.0, 39, 0,  10, 1  )

        self.assertEqual(sampleObject2.getProdRow(1), sampleProduct)


def test_addSubQty(self):
    pass

def test_getAllProdID(self):
    pass
=======
from inventoryManager import inventoryManager
import unittest
""" Limited Test Data
1	Chai	8	1	10 boxes x 30 bags	18.0	39	0	10	1
2	Chang	1	1	24 - 12 oz bottles	19.0	17	40	25	1
3	Aniseed Syrup	1	2	12 - 550 ml bottles	10.0	13	70	25	0
4	Chef Anton's Cajun Seasoning	2	2	48 - 6 oz jars	22.0	53	0	0	0
5	Chef Anton's Gumbo Mix	2	2	36 boxes	21.3500004	0	0	0	1
"""
class testManage(unittest.TestCase):
    
    def test_Database() :
        pass

