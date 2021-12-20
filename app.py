import tkinter as tk
from tests import runTests


window = tk.Tk() # Top level (root window)
demoLoaded = False

def demoButtonClicked():
    return runTests()

def refreshStatusButtonClicked():
    try:
        with open('inventory.txt', 'r') as invDataCheck:
            if invDataCheck != True:
                programStatusFine.grid(row=1, column=3)
                invDataCheck.close()
    except:
        programStatusError.grid(row=1, column=3)


window.title('Stocklink Lite - v.0 development build - by David Ikin')
window.minsize(width=800, height=400)

label = tk.Label(
    text='Stocklink Lite: Prototype build v.0',
    font='Ariel',
    bg='white',
    width=40,
    height=2
)
entryText = tk.Label(
    text='Search Inventory:',
    font = 'Ariel',
    height = 2,
    width=24
)
programStatusLabelChecking = tk.Label(
    text='Status check...',
    bg='blue',
    width=24,
    height=2
)
programStatusError = tk.Label(
    text='Error: No data.',
    bg='red',
    width=24,
    height=2
)
programStatusFine = tk.Label(
    text='System Online.',
    bg='green',
    width=24,
    height=2
)
entry = tk.Entry(
    width=75,    
)
searchButton = tk.Button(
    width=24,
    text='search'
)
generateInventoryButton = tk.Button(
    width=18,
    height=3,
    text='Create Demo Inventory',
    command=demoButtonClicked
)
refreshStatusButton = tk.Button(
    width=18,
    height=3,
    text='Refresh',
    command=refreshStatusButtonClicked
)

label.grid(row=1, column=0, columnspan=2)

programStatusLabelChecking.grid(row=1, column=3)

entry.grid(row=2, column=1, columnspan=1)
searchButton.grid(row=2, column=3, columnspan=1)
entryText.grid(row=2, columnspan=1, column=0)

generateInventoryButton.grid(row=3, column=0)
refreshStatusButton.grid(row=4, column=0)


window.mainloop()