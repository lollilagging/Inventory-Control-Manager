import sqlite3

conn = sqlite3.connect ('northwind.db')
c = conn.cursor()

# Logic


class inventoryManager(object):

    def add_product(self, prod_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order,_reorder_level, discontinued):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (prod_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order,_reorder_level, discontinued))
        conn.commit()
        conn.close()

    def remove_prod(self, productID):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("DELETE from products WHERE product_id = (?)", (productID,))

        conn.commit()
        conn.close()

    def set_prod_ID(self, idNo, prodName):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("""UPDATE products  SET product_id = (?)
                    WHERE product_name = (?)

       """, (idNo, prodName))
        conn.commit()
        conn.close()

    def set_prod_name(self, prodName, idNo):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("""UPDATE products  SET product_name = (?)
                    WHERE product_id = (?)

       """, (prodName, idNo))
        conn.commit()
        conn.close()

    def set_prod_qty(self, prodQty, idNo):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("""UPDATE products  SET quantity_per_unit = (?)
                    WHERE product_id = (?)

       """, (prodQty, idNo))
        conn.commit()
        conn.close()

    def get_product_ID(self, prodName):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("SELECT * from products WHERE product_name = (?)", (prodName,))
        items = c.fetchall()

        for item in items:
            print(item[0])

        conn.commit()
        conn.close()

    def get_product_name(self, prodID):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("SELECT * from products WHERE product_id = (?)", (prodID,))
        items = c.fetchall()

        for item in items:
            print(item[1])

        conn.commit()
        conn.close()

    def get_product_qty(self, prodID):
        conn = sqlite3.connect('northwind.db')
        c = conn.cursor()
        c.execute("SELECT * from products WHERE product_id = (?)", (prodID,))
        items = c.fetchall()

        for item in items:
            print(item[2])

        conn.commit()
        conn.close()
