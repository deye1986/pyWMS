**Orion - Warehouse management system** <br/>


Development log:<br/>
App now creates and saves sku's to a text file. <br/>
App creates unique sku's for a named item and stores the item details in an inventory.txt file. <br/>
App determines location of item in warehouse based on item data and appends inventory.txt. <br/>
GUI in development. <br>
GUI Status bar fully functional and responds with warnings if stock data is absent<br/>
SKU generator has been changed to create a random number at the start of the sku code<br/>
in order to avoid duplicate SKU codes for items with similar names.<br/>

Binded functions and methods to the GUI for interactivity.<br>
Cleaned code (slightly)<br>

26.12.2021
Prior to this log an issue was discovered. The layout manager method grid() was positioning widgets<br>
in relation to other widgets which presented a GUI issue. To resolve this, place() and pack() layout<br>
methods were considered but for ease of use and relative simplicity, the pack() layout manager is <br> prefered. The GUI is now compact and ready to feature new functionality. <br>
The application is now named Orion.<br>

28.12.2021
Working on main features of inventory management and user input and linking it to GUI<br>
           