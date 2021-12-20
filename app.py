import tkinter as tk
from item import Item


window = tk.Tk() # Top level (root window)

window.title('test')

window.minsize(width=800, height=600)

label = tk.Label(
    text='Stocklink Lite',
    font='Ariel',
    bg='white',
    width=80,
    height=2
)

programStatusLabelFine = tk.Label(
    text='Status check...',
    bg='blue',
    width=24
)

entry = tk.Entry(
    width=75,
    
)

searchButton = tk.Button(
    width=24,
    text='search'
)




entry.grid(row=2, column=0, columnspan=3)
label.grid(row=1)
programStatusLabelFine.grid(row=1, column=4)
searchButton.grid(row=2, column=4, columnspan=1)

statusCheck = ''


window.mainloop()