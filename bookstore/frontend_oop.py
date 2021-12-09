from tkinter import *
from backend_in_oop import Database

database = Database()
#creating an object containing database class



"""
a program that stores the book information
Title, Author
Year ISBN

user can:
view all records 
search an entry 
add entry 
update entry
delete 
close

"""

class BookStore():
    
    def __init__(self):
        
        self.window = window

        self.window.wm_title("BookStore Version 0")

        l1 = Label(text = "Title")
        l1.grid(row = 0, column = 0)
        l2 = Label(text = "Author")
        l2.grid(row = 0, column = 2)
        l3 = Label(text = "Year")
        l3.grid(row = 1, column = 0)
        l4 = Label(text = "ISBN")
        l4.grid(row = 1, column = 2)


        self.title_text = StringVar()
        self.e1 = Entry(textvariable = self.title_text)
        self.e1.grid(row = 0, column = 1)

        self.author_text = StringVar()
        self.e2 = Entry(textvariable = self.author_text)
        self.e2.grid(row = 0, column = 3)

        self.year_text = StringVar()
        self.e3 = Entry(textvariable = self.year_text)
        self.e3.grid(row = 1, column = 1)

        self.isbn_text = StringVar()
        self.e4 = Entry(textvariable = self.isbn_text)
        self.e4.grid(row = 1, column = 3)

        self.list1 =  Listbox(height = 6, width = 35)
        self.list1.grid(row=2,column = 0, rowspan = 6, columnspan =2)

        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=2, column = 2,rowspan = 6)

        self.list1.configure(yscrollcommand = self.sb1.set)
        #vertical scroll bar alongy axis is set to yaxis
        self.sb1.configure(command = self.list1.yview)
        #passing command when scroll the vertical view will change

        self.list1.bind("<<ListboxSelect>>",self.get_selected_row)
        #creating a event so we can follow the click of the cursor in the list box.

        b1 = Button(text = "View all", width = 12, command = self.view_command)
        b1.grid(row = 2 , column = 3)
        #adding to the command a wrapper function to create a def that executes the command

        b2 = Button(text = "Search entry", width = 12, command = self.search_command )
        b2.grid(row = 3 , column = 3)

        b3 = Button(text = "Add entry", width = 12, command = self.add_command)
        b3.grid(row = 4 , column = 3)

        b4 = Button(text = "Update", width = 12, command = self.update_command)
        b4.grid(row = 5 , column = 3)

        b5 = Button(text = "Delete", width = 12, command = self.delete_command)
        b5.grid(row = 6 , column = 3)

        b6 = Button(text = "Close", width = 12,command = self.window.destroy)
        b6.grid(row = 7 , column = 3)

        
    def get_selected_row(self,event):
        try:

            index = self.list1.curselection()[0]
            #retrieving the index using the cursor click and getting the index from the tuple
            self.selected_tuple = self.list1.get(index)
            #returning the entry using the index from the list
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
            #when the data is selected, it will be displayed in the entry boxes
        except IndexError:
            pass
            #there was a index error, when nothing was in the listbox. using try/except to except the index error thats raised
    def view_command(self):
        self.list1.delete(0,END)
            #ensures the list is clear each time the command is pressed
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
        #using the entry box varibles and converting the stringvar using get putput a real string object        
                self.list1.insert(END , row)
    def add_command(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))
            #this is added so the data is written into the list, and the extra bracket puts the output into one line
            #instead of multiple lines

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        try:
            database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            #here we are using the values inside the stringvar within the entry text boxes. these are used to update the data values
            #selected tuple stays the same as its the index of the item in database
        except AttributeError:
            pass






window = Tk()
BookStore()
window.mainloop()
