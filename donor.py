import mysql.connector
from flask import session
from datetime import date

class donor_operation:
    def connection(self):
        con=mysql.connector.connect(host="127.0.0.1",port="3306",user="root",password="root",database="funding")
        return con
    
       # ------------------donor details insertion------------------
    def donor_info(self,dname,demail,dpan,damt):
        db=self.connection()
        mycursor=db.cursor()
        sq = "insert into donor (dname,demail,dpan,damt,caseid) values(%s,%s,%s,%s,%s)"
        record = [dname,demail,dpan,damt,session['caseid']]
        mycursor.execute(sq,record)
        db.commit()
        #retrive donor id
        sq = "select did from donor order by did desc limit 1"
        mycursor.execute(sq)
        row=mycursor.fetchall()
        session['did']=row[0][0]
        mycursor.close()
        db.close()
        return
    
    # def detail(self):
    #     db=self.connection()
    #     mycursor = db.cursor()
    #     sq = " select did,dname,demail,dpan,damt,caseid from donor where caseid=%s"
    #     record = [session['caseid']]
    #     mycursor.execute(sq,record)
    #     db.commit()
    #     row= mycursor.fetchall()
    #     mycursor.close()
    #     db.close()
    #     session['did']= row[0][0]
    #     return


    def payment(self,pay_id,ord_id):
        db=self.connection()
        mycursor=db.cursor()
        sq="select damt from donor where did=%s"
        record=[session['did']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        amt = row[0][0]
        payable = amt - (amt * .1)
        
        sq="insert into fund_info(case_id,pay_id,ord_id,fund_amt,payable,donor_id,pay_date) values(%s,%s,%s,%s,%s,%s,%s)"
        record=[session['caseid'],pay_id,ord_id,amt,payable,session['did'],date.today()]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return
    
    def pay_sum(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select sum(payable) from fund_info where case_id=%s"
        record=[session['caseid']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        a = row[0][0]
        if (a==None):
            return 0
        else:
        # for r in row:
        #     a = float(r[0])
            return a
    
    def receipt(self,pay_id):
        db=self.connection()
        mycursor=db.cursor()
        sq="select dname,demail,dpan,pay_id,fund_amt,pay_date from donor d,fund_info f where d.did=f.donor_id and f.pay_id=%s"
        record=[pay_id]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        return row