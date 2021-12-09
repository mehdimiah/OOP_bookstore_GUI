import sqlite3


class Database:


    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT,author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):

        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()


    def view(self):

        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        #dont need a commit method as we are only just viewing the data in the database
        return rows

    def search(self,title = "", author = "" , year = "", isbn=""):
        #if the user pass only author name, we use empty strings as default values. allows SQL to search with empty title

        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        #dont need a commit method as we are only just viewing the data in the database
        return rows


    def delete(self,id):

        self.cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.conn.commit()
        

    def update(self,id, title, author, year, isbn):

        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn,id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
        #del runs when the instance is deleted from the script
        #this happens when the script is exited

#connect dosnt need to be called upon, because init is doing it right away
