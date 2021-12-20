# zone1 - most used stock, zone2 - long storage.
# S.K.U. = Stock Keeping Unit; the items unique identifier in warehouse operations.

class Item:
    '''An item to be stored, location determined by isUsed, which value defaults to True'''
    def __init__(self, name, category, qty, isUsed=True):
        self.name = name
        self.category = category
        self.qty = qty
        self.isUsed = isUsed
        self.zone = []

    def getSKU(self):
        '''Usually initially called from the storeItem method.'''

        # combination of first three characters of the name and category to make an Stock Keeping Unit(sku).

        firstHalf = self.name[:3]
        secondHalf = self.category[:3]
        return firstHalf + secondHalf    
    
    
    def storeItem(self):
        '''Creates and stores details of the item in the inventory.txt file'''

        stockRecord = []
        self.createSKU = self.getSKU()
        self.itemDetails = [self.name, self.category, self.qty, self.isUsed, self.createSKU]
        print(' ** Alert ** Creating inventory : ' + str(self.itemDetails))
        itemLocation = self.placeItem()
        stockRecord.append(self.itemDetails)
        stockRecord.append(itemLocation)
        with open("inventory.txt", "a") as inventoryFile:
            inventoryFile.write(str(self.itemDetails + self.zone) + '\n')
            inventoryFile.close()
        


    def placeItem(self):
        '''Called within storeItem() to determine stock placement based on isUsed parameter'''

        if self.isUsed == True:
            z1 = self.zone.append('Zone 1')
            return z1
        else:
            z2 = self.zone.append('Zone 2')
            return z2
    
    def locateItem(self): # test method.
        methodName = str(self.name)
        print(methodName, self.zone)



