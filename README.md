# Inventory-Control-Manager
In Partial Completion of CPE106L

Every businessman needs an Inventory Control Management to manage their stocks, pricing and exponential sales on their product. An Inventory Control is a process of managing stocks and products in order to satisfy the customer’s demands without any unnecessary delay. The goal of the program is to heavily focus in managing inventory for stocks and products and to ease the progress in obtaining sales from the business by showing statistics per daily income. 

Below is the list of specifications of the program: 

A customer selects an item from the product list and adds it into the cart. Once selected into the cart, it will now ask to finalize the selected items into the cart in order to total the price of the items combined. 

The product list serves as a list for the product listed and its quantities. It can add or remove items as well as to update its quantities for availability. It has the product’s data to view the product in full details. 

A product will contain the following attributes: Product Name, Product code, Price. This object will return the information it had as well as to update the product’s content if wished to be changed such as changing the information of the product. The product name is available to be on use in Product list. 

A cashier will update the quantity of the product specified by the product code and the sales if a product was reduced. It will compute the following payment of the customer’s finalized items and the customer’s actual payment. Once done, it will return the payment change to the customer and add the payment of the customer’s finalized items into the sales. 

The sales will be updated if the customer payment of the finalized items was done in the cashier as it would receive the payment and adds it into a new income, which the total sale per day will reset and returns the value of the daily sales. 

The nouns attributed and used into the program are: 
Product Name                                       Product Code                                      Price 
Item List                                         Product Quantity                               Customer Cart 
Client Payment                                     Total Payment                                 Updated Sales 
Daily Sales 

 

The verbs attributed and used into the program are: 

Get product                                       Update Item List                       Updated Item Quantity 
Add Item to Cart                                 Finalize Cart Items                       Get Client Payment 
Return Change                                     Updated Sales                            Peek Daily Sales  
