from item import Item

phone = Item('mobile phone', 'small', 1)
tin = Item('tin', 'small', 1)
lighter = Item('Clipper Lighter', 'very small', 1)

phone.storeItem('Zone1')
tin.storeItem('Zone1')
lighter.storeItem('Zone1')

phone.locateItem()
tin.locateItem()
lighter.locateItem()

phone.getSKU()