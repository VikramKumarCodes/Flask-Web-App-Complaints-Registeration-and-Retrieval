"""THIS PYTHON FILE INSERTS THE INPUT DATA INTO DATABASE,
   GENERATE A UNIQUE ID AND THEN DISPLAY THE RELEVANT DETAILS
   ON INPUT OF PROVIDED ID"""
   
#LIST OF MODULES IMPORTED
from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
#HOME PAGE
@app.route("/")  
def index():  
    return render_template("index.html");  

#ADD FUNCTION TO RENDER ADD_COMPLAIN.HTML FILE
@app.route("/add")  
def add():  
    return render_template("add_complain.html")  

#ADDCOMPLAIN FUNCTION TO RETRIEVE DETAILS FROM USER AND INSERT INTO DATABASE 
@app.route("/addcomplain",methods = ["POST"])  
def addcomplain():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            #ASSIGNING VARIABLES TO VALUE RECEIVED FROM ADD.HTML
            NAME = request.form["name"]  
            INVOICE_REFERENCE = request.form["invref"]  
            INVOICE_DATE = request.form["invdate"]  
            PRODUCT_NAME = request.form["pname"]  
            NATURE_OF_COMPLAINT = request.form["nature"]  
            #CONNECTING TO THE DATABASE
            with sqlite3.connect("complain.db") as con:  
                cur = con.cursor()  
                #INSERTING VALUES TO THE DATABASE
                cur.execute("INSERT into Complain (NAME, INVOICE_REFERENCE, INVOICE_DATE, PRODUCT_NAME, NATURE_OF_COMPLAINT) values (?,?,?,?,?)",(NAME, INVOICE_REFERENCE, INVOICE_DATE, PRODUCT_NAME, NATURE_OF_COMPLAINT))  
                con.commit()
                msg = "Complaint successfully Added" 
                #METHOD TO RETRIEVE UNIQUE REGISTERATION NUMBER AND DISPLAY TO THE USER
                k=(cur.lastrowid)
                cur.execute('SELECT * from Complain WHERE UNIQUE_REF_NO=?',(k,))
                row1 = cur.fetchone()
                cur.close()
                return render_template("success_page.html",row1=row1)  
              
        except:  
            con.rollback()  
            msg = "Complaint not Registered"  
        finally:  
            print("Successfully Registered")  
          
#INPUT_ID FUNCTION TO RENDER VIEW.HTML FILE WHICH WILL TAKE REFERENCE NUMBER
@app.route("/input_id")  
def input_id():  
    return render_template("input_unique_id.html")  

#OUTPUT_ID FUNCTION WILL USE THAT REFERENCE NUMBER TO RETRIEVE DETAILS OF THE USER
@app.route("/output_id",methods = ["POST"])  
def output_id():  
    if request.method == "POST":  
           unir = request.form["uniref"]  
           con = sqlite3.connect("Complain.db")  
           con.row_factory = sqlite3.Row  
           cur = con.cursor()  
           #METHOD TO DISPLAY ONLY THAT ROW WHICH MATCHES UNIQUE REFERENCE NUMBER
           cur.execute('SELECT * from Complain WHERE UNIQUE_REF_NO=?',(unir,))
           rows = cur.fetchone() 
           cur.close()
           #METHOD TO DISPLAY NO MATCH FOUND IF USER INPUTS INVALID REFERENCE NUMBER
           if not rows:
              return render_template("no_match_found.html",rows=rows)
           else:
              return render_template("retrieve_unique_id.html",rows=rows)  
           
    
if __name__ == "__main__":  
    app.run()  