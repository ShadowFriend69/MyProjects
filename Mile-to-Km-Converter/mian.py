from tkinter import *


EXTENSION = 1.609


def calculate():
    user_input = float(miles_input.get())
    calculated = user_input * EXTENSION
    label3.config(text=calculated)


window = Tk()
window.title('Mile to Km Converter')
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Label1
label1 = Label(text='Miles')
label1.grid(column=2, row=0)

#Label2
label2 = Label(text='is equal to')
label2.grid(column=0, row=1)

#Label3
label3 = Label(text='0')
label3.grid(column=1, row=1)

#Label4
label4 = Label(text='Km')
label4.grid(column=2, row=1)

#Button
button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)


window.mainloop()
