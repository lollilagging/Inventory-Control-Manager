import sqlite3

# Logic
class inventoryManager(object):

    def __init__(self, dataName = "northwind"):
        """ A Class For Fetching Information From Object"""
        self.database = dataName

    def addNewItem(self, prod_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order,reorder_level, discontinued):
        """ Adding Specific Item To Database"""
        conn = sqlite3.connect('database/{}.db'.format(self.database))
        c = conn.cursor()
        c.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (prod_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order,reorder_level, discontinued))
        conn.commit()
        conn.close()

    def removeItem(self, productID):
        """ Removing Specific Item From Database """
        conn = sqlite3.connect('database/{}.db'.format(self.database))
        c = conn.cursor()
        c.execute("DELETE from products WHERE product_id = ?", (productID))

        conn.commit()
        conn.close()

    def changeData(self, columnType, idNo, data):
        """ NOT FOR ADDING OR SUBTRACTING QTY; columnType:columnNo; idNo: row; data: updated Val"""

        column = ("product_id","product_name","supplier_id","category_id","quantity_per_unit","unit_price","units_in_stock","units_on_order","reorder_level","discontinued")
        if not columnType == 0 : 
            conn = sqlite3.connect('database/{}.db'.format(self.database))
            c = conn.cursor()
            c.execute("""UPDATE products SET {} = '{}'
                        WHERE product_id = '{}'
        """.format(column[columnType], data, idNo))
            conn.commit()
            conn.close()

    def changeId(self, newData, oldData) :
        """ Exclusive For Changing Item ID """

        conn = sqlite3.connect('database/{}.db'.format(self.database))
        c = conn.cursor()
        c.execute("""UPDATE products SET product_id = '{}'
                    WHERE product_id = '{}'
        """.format(newData, oldData))
        conn.commit()
        conn.close()

    def getProdInfo(self, idNo, columnType):
        """ NOT FOR ADDING OR SUBTRACTING QTY; columnType:columnNo; idNo: row; data: updated Val"""

        column = ("product_id","product_name","supplier_id","category_id",
        "quantity_per_unit","unit_price","units_in_stock","units_on_order",
        "reorder_level","discontinued")

        conn = sqlite3.connect('database/{}.db'.format(self.database))
        c = conn.cursor()

        c.execute("""SELECT {} FROM products WHERE product_id = '{}'""".format(column[columnType],idNo))
        
        info = c.fetchone()[0][0]
        conn.close()
        return info
    
    def getProdRow(self, idNo):
        """ Get Prod Row """
        conn = sqlite3.connect('database/{}.db'.format(self.database))

        c = conn.cursor()
        c.execute("""SELECT * FROM products WHERE product_id = '{}'""".format(idNo))
        
        info = c.fetchone()
        conn.close()
        return info

    def addSubQty(self, addSub, idNo):
        """ ADD OR SUBTRACT BY VALUE addSub """
        initialQty = self.getProdInfo(idNo, 6) #6 = units_in_stocks
        newQty = initialQty + addSub
        if newQty >= 0:
            self.changeData(6,idNo,newQty)
        else:
            return False
        return True

    def getAllProdId(self) :
        conn = sqlite3.connect('database/{}.db'.format(self.database))

        c = conn.cursor()
        c.execute("""SELECT product_id FROM products""")
        
        info = c.fetchall()
        conn.close()

        return info
