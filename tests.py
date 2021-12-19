from item import Item

def runTests():
    phone = Item('mobile phone', 'small', 1)
    tin = Item('tin', 'small', 1)
    lighter = Item('Clipper Lighter', 'very small', 1)
    desktopCPU = Item('Desktop Computer', 'large', 1, False)

    phone.storeItem()
    tin.storeItem()
    lighter.storeItem()
    desktopCPU.storeItem()


runTests()