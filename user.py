import mysql.connector
from flask import session

class user_operation:
    def connection(self):
        con=mysql.connector.connect(host="127.0.0.1",port="3306",user="root",password="root",database="funding")
        return con
 #---------insertion of DATA ----------------------------------------   
    def user_signup(self,name,gid,mobile,email,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into user (name,gid,mobile,email,password) values(%s,%s,%s,%s,%s)"
        record=[name,gid,mobile,email,password]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
#--------------Delete Account While Signup is Not completed  
    def user_delete(self,email):
        db=self.connection()
        mycursor=db.cursor()
        sq="delete from user where email=%s "
        record=[email]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
#-----------LOG IN details----------------------------  
    def user_login(self,email,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select name,mobile,email,password from user where email=%s and password=%s"

        record=[email,password]
        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        rc=mycursor.rowcount

        if(rc==0):
            return 0
        else:
            session['name']=row[0][0]
            session['mobile']=row[0][1]
            session['email']=row[0][2]
            session['password']=row[0][3]
            return 1
# ----------------profile pic----------------------
    def ppic(self,propic):
        db=self.connection()
        mycursor=db.cursor()
        sq="select proid,user_email from profile where user_email=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==0):
            sq= "insert into profile (propic,user_email) values(%s,%s)"
            record = [propic,session['email']]
            mycursor.execute(sq,record)
            
        else:
            sq = "update profile set propic=%s where user_email=%s"
            record = [propic,session['email']]
            mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
#---------Display pic-------------------------------
    def dppic(self): 
        db=self.connection()
        mycursor=db.cursor()
        sq="select propic,user_email from profile where user_email=%s"
        record=[session['email']]

        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        return row
#-------------data retrive to USER PROFILE---------------
    def user_profile(self): 
        db=self.connection()
        mycursor=db.cursor()
        sq="select name,gid,email,mobile from user where email=%s"
        record=[session['email']]

        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        return row
    

    
#-----------updating User Profile------------
    def user_update(self,name,mobile):
        db=self.connection()
        mycursor=db.cursor()
        sq="update user set name=%s , mobile=%s where email=%s"
        record=[name,mobile,session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        session['name']=name
        return
    
    def user_password(self,old_password,new_password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select password from user where email=%s and password=%s"
        record=[session['email'],old_password]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==1):
            sq="update user set password=%s where email=%s"
            record=[new_password,session['email']]
            mycursor.execute(sq,record)
            db.commit()
            mycursor.close()
            db.close()
            return 1
        
        return 0
    
 #---------Message sending ----------------------------------------   
    def contact(self,cname,cemail,csub,cmobile,cdesc):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into contact (cname,cemail,csub,cmobile,cdesc) values(%s,%s,%s,%s,%s)"
        record=[cname,cemail,csub,cmobile,cdesc]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
    
#-------------Case Details-----------------------------------

    def addcase(self,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into patient (pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc,user_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        record=[pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc,session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
    
# ----------------Patient Data retrive-----------------------

    def pdetail(self): 
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc from patient where user_email!=%s"
        record=[session['email']]

        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        return row
    
# ----------------------all cases--------------------
    def user_case(self): 
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc from patient where user_email=%s"
        record=[session['email']]

        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        return row
    
# ---------------------case------------------------
    def case(self,caseid): 
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc from patient where caseid=%s"
        record=[caseid]

        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        session['caseid']=row[0][0]
        return row
    # --------------retrive all data---------------------------
    def allcases(self,caseid):
        db=self.connection()
        mycursor=db.cursor()
        sq = "select caseid,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc from patient  where status=1"
        mycursor.execute(sq)
        row= mycursor.fetchall()
        session['caseid'] = row[0][0]
        return row
    # -----------complete cases---------------------------------
    def complete(self):
        db=self.connection()
        mycursor=db.cursor()
        sq = "select caseid,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc from patient where status=0"
        mycursor.execute(sq)
        row= mycursor.fetchall()
        return row
# ...........Complete case 2-----------------------------
    def complete_2(self):
        db=self.connection()
        mycursor=db.cursor()
        sq = "select caseid,pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc from patient where status=0 & user_email!=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        session['caseid'] = row[0][0]
        return row

#-------------bank details----------------------------
    def bank(self,aname,bname,account,pan,bmobile):
        db=self.connection()
        mycursor=db.cursor()
        sq = "insert into bank (aname,bname,account,pan,bmobile,user_email) values(%s,%s,%s,%s,%s,%s)"
        record = [aname,bname,account,pan,bmobile,session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return 
    # ------------retrive bank details--------------
    def bank_details(self):
        db=self.connection()
        mycursor = db.cursor()
        sq = "select aname,bname,account,pan,bmobile from bank where user_email=%s"
        record = [session['email']]
        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        return row
    # -----------------Counting----------------------
    def count1(self):
        db=self.connection()
        mycursor = db.cursor()
        sq = "select count(*),sum(amt) from patient"
        mycursor.execute(sq)
        row= mycursor.fetchall()
        return row
    
    def count2(self):
        db=self.connection()
        mycursor = db.cursor()
        sq = "select count(*),sum(payable) from fund_info"
        mycursor.execute(sq)
        row= mycursor.fetchall()
        return row


