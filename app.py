import tkinter as tk
from item import Item


window = tk.Tk() # Top level (root window)

window.title('test')

window.minsize(width=800, height=600)

label = tk.Label(
    text='Stocklink Lite',
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
    width=24
)
programStatusError = tk.Label(
    text='Error: No data',
    bg='red',
    width=24
)
programStatusFine = tk.Label(
    text='System Online.',
    bg='green',
    width=24
)

entry = tk.Entry(
    width=75,    
)

searchButton = tk.Button(
    width=24,
    text='search'
)



label.grid(row=1, column=0, columnspan=2)

programStatusLabelChecking.grid(row=1, column=3)
try:
    with open('inventory.txt', 'r') as invDataCheck:
        if invDataCheck != True:
            programStatusFine.grid(row=1, column=3)
            invDataCheck.close()

except:
    programStatusError.grid(row=1, column=3)

entry.grid(row=2, column=1, columnspan=1)
searchButton.grid(row=2, column=3, columnspan=1)
entryText.grid(row=2, columnspan=1, column=0)

statusCheck = ''


window.mainloop()