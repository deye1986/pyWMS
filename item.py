# zone1 - most used stock, zone2 - long storage.

class Item:
    def __init__(self, name, category, qty, isUsed=True):
        self.name = name
        self.category = category
        self.qty = qty
        self.isUsed = isUsed
        self.zone = []

    def storeItem(self, location):
        self.zone.append(location)
    
    def locateItem(self):
        methodName = str(self.name)
        print(methodName, self.zone)

    def getSKU(self):
        # combination of first two characters of the name and category to make an Stock Keeping Unit(sku)
        firstHalf = self.name[:2]
        secondHalf = self.category[:2]
        return firstHalf + secondHalf

    def saveItem(self):
        x = self.getSKU()
        with open('sku.txt', 'a') as f:
            f.write(x + '\n')
