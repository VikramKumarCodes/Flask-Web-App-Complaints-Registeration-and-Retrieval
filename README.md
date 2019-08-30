# Flask-Web-App-Complaints-Registration-and-Retrieval

<h2>Business case:</h2>

<h4>Business units are receiving complaints from its customers through sources of call centre, mails, paper mode, each branch offices, retail offices, back operation offices . It is very difficult to manage these complaints and process feedback to business for corrections and improvement.</h4>

A web based application can be used to log and process all the complaints in a single database. 
Benefits to the customers:
1.	Customers can log their complaints in a single window without making any calls, direct contact with company.
2.	They can log the complaints through their mobiles, laptops, tablets.
Benefits to the companies:
1.	All the complaints are logged in a single database and accessible from any location to all authenticated users without any hassles.
2.	Reduced workload on the employees receiving complaints at various channels.
3.	The complaints stored in database can be used to perform analytics and provide feedback to company managers to increase the customer satisfaction, operation efficiency, boosting sales.

<h2>Proposed Solution:</h2>

I.	Web page for submission of complaints about the products/services delivery
        
The web page will take the following inputs from the customer<br>
a.  Name of the customer <br>
b. Delivery consignment/invoice reference<br>
c. Invoice/Consignment date<br>
d. Product name<br>
e. Nature of the complaints<br>

After submitting the complaint, a reference number should be generated and returned to customer for future reference.

II.	Web page for search for updates on the complaints
  The web page will provide search option based on the following inputs:<br>

a. Complaint reference number or invoice reference number
  
b.After submitting the complaint reference number or invoice reference number generated, the system should fetch the relevant updates     and display on the web page.

III.	Web service provider to launch the web pages on the domain

IV.	Database to store complaints

V.	Modules to register and retrieve complaints to or from the database

VI.	Configuration scripts to create tables, start webservice, authentication

<h2>Instructions for Use:</h2>
1.Ensure all required HTML files are present inside templates folder<br>2.Firstly run database.py which will automamtically create a database complain.db<br>3.Now execute main.py which will initiate your web app and you can visit it at http://127.0.0.1:5000/ <br>4.User will click on Submit your Complaints and register his/her details.<br>5.User will be provided a Unique Reference Number.<br>6.Now you can update the status of complaint in the database<br>7.Next time when user will input his/her unique reference number,all his comlplaints details will be fetched
along with the status of the complaint.

<h2>Softwares Requirements:</h2>
1.	Python 3.7.x<br>2.	Sqlite 3<br>3.	Flask 1.1.1<br>

<h2>Acknowledgements:</h2>

1.	I would like to thank my organization Value C Consulting Services Pvt. Ltd for facilitating the implementation.
2.	I would like to thank my mentor KRISHNA PRAKASH KK (krishna.prakash.kk@gmail.com) , a senior AI professional for providing me an opportunity, all round guidance and encouragement to implement and publish this project.
3.	I take this opportunity to thank all open source community for their contributions in open forums that helped me to solve many technical issues.

<h2>Contacts:</h2>
For any queries regarding this solution, please contact the following
<h4>1.	Vikram kumar Srivatsava (vikram999sri@gmail.com)<h4>


