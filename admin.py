import mysql.connector
from flask import session

class admin_operation:
    def connection(self):
        con=mysql.connector.connect(host="127.0.0.1",port="3306",user="root",password="root",database="funding")
        return con
    
    def admin_login(self,user,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select user,password from admin where user=%s and password=%s"

        record=[user,password]
        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        rc=mycursor.rowcount

        if(rc==0):
            return 0
        else:
            session['user']=row[0][0]
            session['password']=row[0][1]
            return 1
        # ---------admin info( data retrival)--------------------
    def admin_info(self):
        db = self.connection()
        mycursor = db.cursor()
        sq = "select pname,gender,cdetails,f.case_id,amt,sum(payable),status from fund_info f,patient p where p.caseid=f.case_id group by f.case_id"
        mycursor.execute(sq)
        row = mycursor.fetchall()
        return row
    
        # -------------status-----------------

    def status_update(self,caseid):
        db=self.connection()
        mycursor=db.cursor()
        sq="update patient set status=0  where caseid=%s"
        record=[caseid]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return 
    
    def status_info(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select status from patient"
        mycursor.execute(sq)
        row = mycursor.fetchall()
        return row