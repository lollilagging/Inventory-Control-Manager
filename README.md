# Inventory-Control-Manager
In Partial Completion of CPE106L

Initial Proposal: https://mymailmapuaedu-my.sharepoint.com/:b:/g/personal/kktmorales_mymail_mapua_edu_ph/ETf1Wm3zWZ9CqZa__rU6CDAB1GU7AmPbtYFWZkZCjdSh4A?e=WfAAWn

Deliverables/Sprints: https://mymailmapuaedu-my.sharepoint.com/:f:/g/personal/kktmorales_mymail_mapua_edu_ph/ElucEOgIzEFFtBQW0HyFGC4Bs132i9J_8SVzX6XjjNn1cw?e=dIZziW

Class Diagram: https://mymailmapuaedu-my.sharepoint.com/:i:/g/personal/kktmorales_mymail_mapua_edu_ph/Edj31m3BQ65Ir4AI00PqAX8BCevhfidNXuXpr8L7YabfMw?e=lmxaaB

Database Used: https://docs.yugabyte.com/latest/sample-data/northwind/
 
Sprint 1:
The initial Goal of Sprint 1 is to estbalish the structure of program. We did create an initial class diagram, but we knew that there as much more to the structure
as such our first official meeting was about building the new class diagram. We unfortunately loss the audio for the meeting but the actual class diagram itself will be seen in the link above.

Due to the amount of college requirements we had to do during the last week, we had to limit on what we can do. I started to project by initializing the object person. In the following days, I will be starting to work on other objects that fall under data structure together with Seth Dayao, whilst my other member, Jemuel will be working on the UI implementation of the program. On the following days, we will be focusing on the the objects and have a goal being able to test all objects on a unittest while my other member focus on the ui aspect of the program. 

The person object may now be able to accept different values and can now be integrated with a unittest

Sprint 2 (To be edited): 
After a week of production, Kenshin was able to finish the whole Customer object while other objects have progressed as well. Some objects were not finished due to lack of time and some due to lack of proper communication because of the different schedules and workloads of the group members.  Seth was able to make the Product object and it was almost complete but it has been decided to be merged with the InventoryManager object due to new ideas and knowledge after the second official meeting. Jemuel has found a proper UI tool called IronPython to be used in implementing a GUI for the project and has started practicing it while visualizing the proper UI for the program. 

There is also newly created UI samples as well as updated class diagram to follow that of sqlite. 
For the remaining days of the week, certain objects in the program will be modified by both Kenshin and Seth while Jemuel creates a sample UI for the program while it is still in progress. 

Goals for Sprint 3: 

Modified objects 

UnitTest all objects 

Start implementing a UI for the program  
 
Sprint 3:

After a week of producing the code with a limited of time, the group now has cancelled the plan of integrating the code into a GUI (via IronPython by WPF/XAML Integration). Instead the code now will be presented on a console form with the same output. The Unit testing has been implemented in inventoryManager.py and person.py, but all of the objects created was done this week, recently the storeManager.py. The problems that we most had is time constraint since it heavily imposed a lot of requirements and workload in different subject for the group ever since academic respite ended. The InventoryManager has been checked and modified by Kenshin as while as adding functions in the class such as the GetProdRow, GetAllProdID, and AddSubQty. Unit testing for inventoryManager is taking time due to lack of knowledge,practice and struggles of unit testing objects that heavily requires input. 



Instructions on how to use the program: 

To use the program, storeManager.py must be run which can be done on a terminal such as anaconda terminal.

The command for running it on anaconda terminal is python storeManager.py

1. Once the program is run, it will prompt the user to input either 1 or 0. 1 for customer and 0 for manager. It is important to note that manager is incomplete and hence some      functions will not work. 

2. If the user inputs 1 (customer) the user will then be prompted for another 1 or 0 choice this time for 1 for old customer or 0 for new customer. 

     - If the user inputs 1 for old customer, then the user will be asked for a log in before continuing further into the program.

     - If the user inputs 0 for new customer instead, then we the user will be logged in as a guest user and instantly given a menu. 
     
3. Once the menu is given the user will have 7 choices.
      1: add to cart
      2: remove from cart
      3: clear cart
      4: show cart items
      5: finalized order
      6: login/ logout
      7: quit
      
          - Inputting 1 for add to cart will display available items and let the users add items to               the cart given that there is enough quantity for the user's desired item.
          - Inputting 2 for remove from cart will allow the user to remove from the cart as long as               the item exists and is in the cart.
          - Inputting 3 for clear cart prompt the user for a choice if the user is sure to clear cart             or not. The cart will only be cleared if the user is sure else it will return to the                 menu.
          - Inputting 4 for show cart items will print the items in the cart.
          - Inputting 5 for finalized order will prompt the user if the user is sure about finalizing             the order and will be asked to pay by putting the amount of money. The amount of money               will only be valid if it is equal to or greater than the total price.
          - Inputting 6 for login/ logout will let the user login or logout.
          - Inputting 7 quits the program.
