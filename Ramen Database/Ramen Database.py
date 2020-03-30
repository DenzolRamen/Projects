from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Ramen Database by Denzol')
root.iconbitmap('ramenbowl.ico')

'''
frame1 = LabelFrame(root, text='Main Menu', labelanchor=N, padx=10, pady=10)
frame2 = LabelFrame(root, text='Database', labelanchor=N)
frame3 = LabelFrame(root, text='Input', labelanchor=N)
frame4 = LabelFrame(root, text='Image Viewer', labelanchor=N)
'''

frame1 = Frame(root, padx=10, pady=10)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

frame1.grid(row=0, column=0, padx=10, pady=(10,0))
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0, padx=10, pady=(10,10))
frame4.grid(row=1, column=1)

# Frame 1
# =====
addButton = Button(frame1, text = 'Add Entries')
editButton = Button(frame1, text = 'Edit Entries')
deleteButton = Button(frame1, text= 'Delete Entries')

addButton.grid(row=0, column=0, ipadx=100)
editButton.grid(row=1, column=0, ipadx=100, pady=(10,0))
deleteButton.grid(row=2, column=0, ipadx=94, pady=(10,0))
# =====

# Frame 3
# =====
# Create labels
restaurant_name_label = Label(frame3, text='Restaurant Name')
restaurant_name_label.grid(row=0, column=0, sticky=W, padx=20)

address_label = Label(frame3, text='Address')
address_label.grid(row=1, column=0, sticky=W, padx=20)

ramen_dish_label = Label(frame3, text='Ramen Dish')
ramen_dish_label.grid(row=2,column=0, sticky=W, padx=20)

price_label = Label(frame3, text='Price (in Php)')
price_label.grid(row=3, column=0, sticky=W, padx=20)

rating_label = Label(frame3, text='Rating')
rating_label.grid(row=4, column=0, sticky=W, padx=20)

# Create Entries
restaurant_name_entry = Entry(frame3, width=30)
restaurant_name_entry.grid(row=0, column=1, padx=20)

address_entry = Entry(frame3, width=30)
address_entry.grid(row=1, column=1, padx=20)

ramen_dish_entry = Entry(frame3, width=30)
ramen_dish_entry.grid(row=2,column=1, padx=20)

price_entry = Entry(frame3, width=30)
price_entry.grid(row=3, column=1, padx=20)

image_entry = Entry(frame3, width=30)
image_entry.grid(row=5, column=1, padx=20)

select_entry = Entry(frame3, width=30)
select_entry.grid(row=6, column=1, padx=20)

# Create drop down menu
ratingList = ['1 Star','2 Stars','3 Stars','4 Stars','5 Stars']
ratingVar = StringVar()
ratingVar.set(ratingList[4])

ratingOpt = OptionMenu(frame3, ratingVar, *ratingList)
ratingOpt.grid(row=4, column=1, padx=20, ipadx=58)

# Create button
image_button = Button(frame3, text='Add Image')
image_button.grid(row=5, column=0, ipadx=15)

select_button = Button(frame3, text='Select Entries')
select_button.grid(row=6, column=0, ipadx=10)
# =====

root.mainloop()