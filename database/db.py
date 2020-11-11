import sqlite3
import datetime as dt
import pandas as pd


class MyDatabase:
    def __init__(self, mydb):
        try:
            self.conn = sqlite3.connect(mydb)
            self.cur = self.conn.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username text NOT NULL)")
            self.cur.execute("CREATE TABLE IF NOT EXISTS categories(cat_id INTEGER PRIMARY KEY, category_name text NOT NULL, cat_type text)")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
                expense_id INTEGER PRIMARY KEY, 
                value real NOT NULL, 
                date text NOT NULL,
                cat_id  INTEGER,
                user_id INTEGER,
                CONSTRAINT fk_users
                    FOREIGN KEY(user_id) 
                    REFERENCES users(user_id)
                    ON DELETE SET NULL
                CONSTRAINT fk_categories
                    FOREIGN KEY(cat_id) REFERENCES 
                    categories(cat_id)
                    ON DELETE SET NULL
                )""")
            self.conn.commit() 
        except Exception as e:
            print(e)
        finally:
            self.conn.close


    #Returns Connection pbject    
    def getConnection(self):
        return self.conn
    
    def insertUsers(self, username):    
        self.cur.execute("INSERT INTO users VALUES (null, ?)",(username,))
        self.conn.commit()

    def insertCategories(self, category_name, cat_type):
        self.cur.execute("INSERT INTO categories VALUES (null, ?, ?)",(category_name,cat_type))
        self.conn.commit()

    def insertExpenses(self,  value, date, cat_id, user_id):
        self.cur.execute("INSERT INTO expenses VALUES (null, ?, ?, ?, ?)",(value, date, cat_id, user_id))
        self.conn.commit()

    def getAllExpenses(self):
        try:
            q="""SELECT expenses.expense_id, expenses.date, expenses.value, categories.category_name, users.username 
                                FROM expenses
                                INNER JOIN users ON expenses.user_id=users.user_id
                                INNER JOIN categories ON expenses.cat_id=categories.cat_id
                                order by strftime('%Y',date), strftime('%m',date), strftime('%d',date) """
            pddata = pd.read_sql_query(q, self.conn)
            # print(len(pddata.index))
            # pddata=self.appendBtns(pddata)
            pddata['Edit'] = '  Edit  '
            pddata['Delete'] = '  Delete  '
            return pddata
        except Exception as e:
            print(e)

    def getAllMonths(self):
        try:
            q=("""SELECT DISTINCT strftime('%m-%Y',date) as Months
                    FROM expenses
                    order by strftime('%Y',date), strftime('%m',date)""")
            pddata = pd.read_sql_query(q, self.conn)
            pddata.loc[-1] = "" # adding a row
            pddata.index = pddata.index + 1  # shifting index
            pddata = pddata.sort_index()  # sorting by index
            #print(pddata['Months'])
            return pddata
        except Exception as e:
            print(e)
    
    def getAllCategories(self):
        try:
            q=("""SELECT category_name 
                    FROM categories""")
            pddata = pd.read_sql_query(q, self.conn)
            pddata.loc[-1] = "" # adding a row
            pddata.index = pddata.index + 1  # shifting index
            pddata = pddata.sort_index()  # sorting by index
            return pddata
        except Exception as e:
            print(e)
    
    def getAllUsers(self):
        try:
            q=("""SELECT username 
                    FROM users""")
            pddata = pd.read_sql_query(q, self.conn)
            pddata.loc[-1] = "" # adding a row
            pddata.index = pddata.index + 1  # shifting index
            pddata = pddata.sort_index()  # sorting by index
            return pddata
        except Exception as e:
            print(e)

    def deleteExpense(self, idx):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM expenses WHERE expense_id=?",(idx,))
            self.conn.commit()
            cur.close()  
            #Gets the data from the database in order to update the view
            self.data = self.getAllExpenses()        
        except Exception as e:
            print(e) 

# db = MyDatabase('expenses.db')
# #TEST DATA
# db.insertUsers("Tester 1")
# db.insertUsers("Tester 2")
# db.insertUsers("Tester 3")
# db.insertCategories("Gas","Personal")
# db.insertCategories("Supemarket","Home")
# db.insertCategories("Food","Personal")
# db.insertCategories("Rent","Home")

# db.insertExpenses(18.90, "2020-04-04", 1,2)
# db.insertExpenses(50.90, "2020-04-04",3,2)
# db.insertExpenses(18.90, "2020-04-05",2,1)
# db.insertExpenses(18.90, "2020-03-31",2,2)
# db.insertExpenses(350, "2020-01-14", 4,2)
# db.insertExpenses(26.90, "2019-10-09",3,2)
# db.insertExpenses(18.90, "2020-12-15",2,1)
# db.insertExpenses(340, "2019-11-26",4,2)