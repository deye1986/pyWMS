import tkinter as tk
from tests import runTests
from item import Item


def demoButtonClicked():
    return runTests()

def refreshStatusButtonClicked():
    try:
        with open('inventory.txt', 'r') as invDataCheck:
            programStatusLabelChecking.destroy()
            programStatusError.destroy()
            programStatusFine.pack()         
            displayInventory() 
            invDataCheck.close()
    except:
        programStatusLabelChecking.pack_forget()
        programStatusError.pack()

def displayInventory():
    loadDisplay = Item.inventory()
    cleanedData = str(loadDisplay)
    return tk.Label(
        frameRight,
        text=cleanedData)

window = tk.Tk() # Top level (root window)

window.title('Orion - v.0 development build - David Ikin 2021')

upperFrame = tk.Frame()
statusFrame = tk.Frame()
frameLeft = tk.Frame()
frameRight = tk.Frame()


searchBarEntry = tk.StringVar()

mainPortion = tk.Canvas(
    frameRight,
    bg='red')

label = tk.Label(
    upperFrame,
    text='Orion: Prototype build v.0',
    font='Ariel',
    bg='white')

entryText = tk.Label(
    frameLeft,
    text='Search Inventory:',
    font = 'Ariel')

programStatusLabelChecking = tk.Label(
    statusFrame,
    text='Status check...',
    bg='blue',)

programStatusError = tk.Label(
    statusFrame,
    text='Error: No data.',
    bg='red')

programStatusFine = tk.Label(
    statusFrame,
    text='System Online.',
    bg='green')

entry = tk.Entry(
    frameLeft,
    textvariable=searchBarEntry,
)
searchButton = tk.Button(
    frameLeft,
    text='search')

generateInventoryButton = tk.Button(
    frameLeft,
    text='Create Demo Inventory',
    command=demoButtonClicked)

refreshStatusButton = tk.Button(
    frameLeft,
    text='Refresh',
    command=refreshStatusButtonClicked)

devButtonInv = tk.Button(
    frameLeft,
    text='dev button',
)

upperFrame.pack()
statusFrame.pack(side='bottom', fill='x')
frameLeft.pack(side='left', padx=4, pady=4)
frameRight.pack(side='right', padx=4, pady=4)

label.pack(side='left', padx=10)

programStatusLabelChecking.pack()

entryText.pack()
entry.pack()
searchButton.pack(padx=4, pady=4)

generateInventoryButton.pack(padx=4, pady=4)
refreshStatusButton.pack(padx=4, pady=4)
devButtonInv.pack(padx=4, pady=4)

mainPortion.pack()

window.mainloop()