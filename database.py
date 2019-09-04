#Importing sqlite3 module 
import sqlite3  

#Connecting to database  
con = sqlite3.connect("complain.db")  
print("Database opened successfully")  

#Creating Table Complain inside database  
con.execute("create table Complain (UNIQUE_REF_NO INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, INVOICE_REFERENCE NUMBER INTEGER NOT NULL, INVOICE_DATE INTEGER NOT NULL, PRODUCT_NAME TEXT NOT NULL, NATURE_OF_COMPLAINT TEXT NOT NULL, STATUS_OF_COMPLAINT TEXT)")  
  
print("Table created successfully")  

#Closingthe database  
con.close()  