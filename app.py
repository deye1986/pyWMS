import tkinter as tk
from tests import runTests


window = tk.Tk() # Top level (root window)
demoLoaded = False

def demoButtonClicked():
    return runTests()

def refreshStatusButtonClicked():
    try:
        with open('inventory.txt', 'r') as invDataCheck:
            programStatusLabelChecking.pack_forget()
            programStatusError.pack_forget()
            programStatusFine.pack()
            invDataCheck.close()
    except:
        programStatusLabelChecking.pack_forget()
        programStatusError.pack()


window.title('Stocklink Lite - v.0 development build - David Ikin 2021')

frameLeft = tk.Frame()
frameRight = tk.Frame()
upperFrame = tk.Frame()


searchBarEntry = tk.StringVar()

mainPortion = tk.Canvas(
    frameRight,
    bg='red')

label = tk.Label(
    upperFrame,
    text='Stocklink Lite: Prototype build v.0',
    font='Ariel',
    bg='white')

entryText = tk.Label(
    frameLeft,
    text='Search Inventory:',
    font = 'Ariel')

programStatusLabelChecking = tk.Label(
    upperFrame,
    text='Status check...',
    bg='blue')

programStatusError = tk.Label(
    upperFrame,
    text='Error: No data.',
    bg='red')

programStatusFine = tk.Label(
    upperFrame,
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

frameLeft.pack()
frameRight.pack()
upperFrame.pack()

label.pack()

programStatusLabelChecking.pack()

entryText.pack()
entry.pack()
searchButton.pack()

generateInventoryButton.pack()
refreshStatusButton.pack()

mainPortion.pack()

window.mainloop()