from item import Item

def runTests():
    phone = Item('mobile phone', 'small', 1)
    tin = Item('tin', 'small', 1)
    lighter = Item('Clipper Lighter', 'very small', 1)
    desktopCPU = Item('Desktop Computer', 'large', 1, False)
    beans = Item('TinOfBeans', 'small', '1')

    phone.storeItem()
    tin.storeItem()
    lighter.storeItem()
    desktopCPU.storeItem()
    beans.storeItem()


runTests()