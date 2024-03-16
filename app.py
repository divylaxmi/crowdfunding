from flask import Flask,render_template,request,redirect,url_for,flash,session,send_file
from user import user_operation
from donor import donor_operation
from admin import admin_operation
from encryption import Encryption
from myrandom import randomalphanum,randomnum
from myemail import Email
import razorpay
from datetime import datetime



app = Flask(__name__)
app.secret_key='bahdrbhgfyyanmsjsb'
client = razorpay.Client(auth=("rzp_test_Su8JlfzLV6VozD","Fn9CfeRDBMhwRL34xGm74N6m"))
m= Email(app)


@app.route('/')
def index():
    if("email" in session):
        session.clear()
        return render_template("index.html")
    else:
        caseid = request.args.get('caseid')
        ob = user_operation()
        record = ob.complete()
        data = ob.allcases(caseid)
        a = ob.count1()
        b = ob.count2()
        return render_template("index.html",record=record,data=data,a=a,b=b)

@app.route("/error")
def error():
    return render_template("error.html")

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if(request.method=='GET'):
        return render_template("user_signup.html")
    elif(request.method=='POST'):
        name = request.form['name']
        gid = request.form['gid']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']
        #-------Password encryption----------------
        e=Encryption()
        password= e.convert(password)
        #---insertion-------------------
        ob = user_operation() # object create
        ob.user_signup(name,gid,mobile,email,password)
        #----------Mailing--------------
        global otp
        otp = randomnum()
        subject="Verification Code for LogIn"
        message="Hi"+name+"\n Your OTP is:"+str(otp)+"\n Thank You"+"\n Regards Mentor"
        m.compose_mail(subject,email,message)
        

        return render_template("user_email_verify.html",email=email)
    else:    
        return render_template("error.html")

@app.route('/user_email_verify',methods=['GET','POST'])
def user_email_verify():
    if(request.method=="POST"):
        if(str(otp)==request.form['otp']):
            flash("Your Email is Verified... You can Login Now!!")
            return render_template("user_login.html")
        else:
            email=request.form['email']
            ob = user_operation()
            ob.user_delete(email)
            flash("Invalid OTP...Your Email is not verified.. Try Again to Register!!")
            return redirect(url_for('user_signup'))
    else:
        return render_template("error.html")



@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if(request.method=='GET'):
        return render_template('user_login.html')
    
    elif(request.method=='POST'):
        email = request.form['email']
        password = request.form['password']
        #-----Password Encryption----------
        e=Encryption()
        password= e.convert(password)

        ob = user_operation()
        rc=ob.user_login(email,password)
        if(rc==0):
            flash("invalid email or password!!")
            return redirect(url_for('user_login'))
        else:
            return redirect(url_for('user_dashboard'))
            #return session['name']
    else:
         return render_template("error.html")
    

@app.route('/user_logout', methods=['GET','POST'])
def user_logout():
    if('email' in session):
        if(request.method=='GET'):
            session.clear()
            flash("Log Out Successfully")
            return redirect(url_for('index'))
        else:
            flash("You are not login yet! please Login first")
            return redirect(url_for('user_login'))   
    else:
        return render_template("error.html")

    
@app.route('/user_dashboard',methods=['GET','POST'])
def user_dashboard():
    if('email' in session):
        if(request.method=='GET'):
            ob = user_operation()
            record=ob.pdetail()
            return render_template("user_dashboard.html",record=record)
        else:
            flash("You are not login yet, Login Now")
            return redirect(url_for('user_login'))
    else:
        return render_template("error.html")
    
@app.route('/ppic',methods=['GET','POST'])
def ppic():
    if('email' in session):
        if (request.method=='POST'):
            upic = request.files['upic']  
            propic = upic.filename
            upic.save("static/photo/"+ propic)

            ob= user_operation()
            ob.ppic(propic)
            

            return redirect(url_for('user_profile'))
        else:
            return render_template("error.html")



@app.route('/user_profile',methods=['GET','POST'])
def user_profile(): 
    if('email' in session):
        if(request.method=='GET'):
            ob = user_operation()
            record= ob.user_profile()
            r =  ob.dppic()
            return render_template('user_profile.html',record=record,r=r)
        else:
            name = request.form['name']
            mobile = request.form['mobile']
            

            
            #------updating profile info------------
            ob = user_operation() # object create
            ob.user_update(name,mobile)
            flash("Your Account Details Are Updated Successfully")
            return redirect(url_for('user_profile'))
    else:
        flash("Please Login First")
        return redirect(url_for('user_login'))
    
@app.route('/user_password',methods=['GET','POST'])
def user_password():
    if('email' in session):
        if(request.method=='GET'):
            return render_template("user_password.html")
        else:
            old_password = request.form['old_password']
            new_password = request.form['new_password']
            
            #-- password encryption---------
            e = Encryption()
            old_password = e.convert(old_password)
            new_password = e.convert(new_password)

            ob = user_operation()
            r=ob.user_password(old_password,new_password)
            if(r==1):
                session.clear()
                flash("your password is updated successfully!!")
                return redirect(url_for('user_login'))
            else:
                flash("your old password is invalid...")
                return redirect(url_for('user_password'))
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))
    


@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='GET'):
        return render_template('contact.html')
        
    elif(request.method=='POST'):

        cname = request.form['cname']
        cemail = request.form['cemail']
        csub = request.form['csub']
        cmobile  = request.form['cmobile']
        cdesc = request.form['cdesc']
        #---insertion-------------------
        ob = user_operation() # object create
        ob.contact(cname,cemail,csub,cmobile,cdesc)
        flash("Message Sent!! We'll get in touch with you soon")
        return render_template("contact.html")
    else:    
        return redirect(url_for('user_login'))
    

@app.route('/contact_2',methods=['GET','POST'])
def contact_2():
    if(request.method=='GET'):
        return render_template('contact_2.html')
        
    elif(request.method=='POST'):

        cname = request.form['cname']
        cemail = request.form['cemail']
        csub = request.form['csub']
        cmobile  = request.form['cmobile']
        cdesc = request.form['cdesc']
        #---insertion-------------------
        ob = user_operation() # object create
        ob.contact(cname,cemail,csub,cmobile,cdesc)
        flash("Message Sent!! We'll get in touch with you soon")
        return render_template("contact_2.html")
    else:    
        return render_template("error.html")
    
    
@app.route('/addcase',methods=['GET','POST'])
def addcase():
    if('email' in session):
        if(request.method=='GET'):
            return render_template('addcase.html')
        elif(request.method=='POST'):
            pname = request.form['pname']
            pid = request.form['pid']
            gender = request.form['gender']
            age = request.form['age']
            blood = request.form['blood']
            cdetails = request.form['cdetails']
            paddress = request.form['paddress']
            hname = request.form['hname']
            haddress = request.form['haddress']
            amt = request.form['amt']
            p1=request.files['p1']
            p2=request.files['p2']
            p3=request.files['p3']

            photoa = p1.filename
            photob = p2.filename
            photoc = p3.filename
            d = datetime.now() # current date time
            t = int(round(d.timestamp()))
            photoa = str(t)+"a."+photoa.split(".")[-1]
            photob = str(t)+"b."+photob.split(".")[-1]
            photoc = str(t)+"c."+photoc.split(".")[-1]
            p1.save("static/patient/"+ photoa)
            p2.save("static/patient/"+ photob)
            p3.save("static/patient/"+ photoc)
            ob = user_operation() #create object
            ob.addcase(pname,pid,gender,age,blood,cdetails,paddress,hname,haddress,amt,photoa,photob,photoc)
            return redirect (url_for('bank'))
        else:
            flash("You are not login yet, Login Now")
            return redirect(url_for('user_login'))
    else:
        return render_template("error.html")
    

@app.route("/user_case",methods=['GET','POST'])
def case_detail():
    if("email" in session):
        if(request.method=='GET'):
            ob = user_operation()
            record=ob.user_case()
            return render_template("user_case.html",record=record)
        else:
            flash("You are not login yet, Login Now")
            return redirect(url_for('user_login'))
    else:
        return redirect(url_for('error'))
    
@app.route("/case",methods=['GET','POST'])
def case():
        if("email" in session):
            if(request.method=='GET'):
                caseid = request.args.get('caseid')
                ob = user_operation()
                record=ob.case(caseid)
                amount= int(record[0][-4])
                obj = donor_operation()
                d=obj.pay_sum()
                b=int(d)
                a = int(b*100/amount)
                return render_template("case.html",record=record,data=a)
            elif(request.method=='POST'):
                caseid = request.args.get('caseid')
                ob = user_operation()
                record=ob.case(caseid)
                return render_template("donate.html",record=record)     
        else:
            return render_template('error.html')
    
@app.route("/case_2",methods=['GET','POST'])
def case_2():
        if(request.method=='GET'):
            caseid = request.args.get('caseid')
            ob = user_operation()
            r=ob.case(caseid)
            amount= int(r[0][-4])
            obj = donor_operation()
            d=obj.pay_sum()
            a = (d*100/amount)
            c=int(a)
            return render_template("case_2.html",record=r,data=c)
        elif(request.method=='POST'):
                caseid = request.args.get('caseid')
                ob = user_operation()
                record=ob.case(caseid)
                return render_template("donate_2.html",record=record)
        else:
            return render_template('error.html')
@app.route("/cc_detail2",methods=['GET','POST'])
def cc_detail2():
        if(request.method=='GET'):
            caseid = request.args.get('caseid')
            ob = user_operation()
            r=ob.case(caseid)

            return render_template("cc_detail2.html",record=r)
        else:
            return render_template('error.html')
        
@app.route("/cc_detail",methods=['GET','POST'])
def cc_detail():
        if("email" in session):
            if(request.method=='GET'):
                caseid = request.args.get('caseid')
                ob = user_operation()
                r=ob.case(caseid)
                return render_template("cc_detail.html",record=r)
        elif():
            flash("You are not Login Yet!!! Please login first !!!")
            return render_template('user_login.html')
        else:
            return ("error.html")

@app.route("/case_details")
def case_details():
    if("email" in session):
            caseid = request.args.get('caseid')
            ob = user_operation()
            r=ob.case(caseid)
            amount= int(r[0][-4])
            obj = donor_operation()
            d=obj.pay_sum()            
            a = (d*100/amount)
            c=int(a)
                
            return render_template("case_details.html",record=r,data=c)
    else:
            flash("You are not login yet, Login Now")
            return redirect(url_for('user_login'))
    
@app.route('/allcases')
def allcases():
    caseid = request.args.get('caseid')
    ob = user_operation()
    record = ob.allcases(caseid)
    return render_template("allcases.html",record= record)

@app.route('/complete_case2')
def complete_case2():
    # caseid = request.args.get('caseid')
    ob = user_operation()
    record = ob.complete()
    return render_template("complete_case2.html",record= record)

@app.route('/complete_case')
def complete_case():
    if('email' in session):
        # caseid = request.args.get('caseid')
        ob = user_operation()
        record = ob.complete_2()
        return render_template("complete_case.html",record= record)
    else:
        flash("You are Not Login yet!! Please login first!!!")
        return render_template("user_login.html")


    
@app.route('/bank',methods=['GET','POST'])
def bank():
    if('email' in session):
        if(request.method=='GET'):
            return render_template("bank.html")
        elif(request.method=='POST'):
            aname = request.form['aname']
            bname =  request.form['bname']
            account = request.form['account']
            pan = request.form['pan']
            bmobile = request.form['bmobile']
            ob=user_operation()
            ob.bank(aname,bname,account,pan,bmobile)
            flash("Bank Details Updated Successfully")
            return redirect(url_for('user_dashboard'))
        else:
            flash("You are not login yet, Login Now")
            return redirect(url_for('user_login'))
    else:
        return redirect(url_for('error'))
    
@app.route("/bank_details")
def bank_details():
    if("email" in session):
        ob = user_operation()
        record=ob.bank_details()
        return render_template("/bank_details.html",record=record)
    else:
        flash("You are not login yet, Login Now")
        return redirect(url_for('user_login'))
        


@app.route('/donation_box',methods=['GET','POST'])
def donation_box():
    if('caseid' in session):
        if(request.method=='POST'): 
            caseid= request.args.get('caseid')
            amt = request.form['damt']
            return render_template("donor.html",damt=amt,caseid=caseid)
            # return redirect(url_for("/donor",damt=amt))
        else:
            return render_template("error.html")

@app.route('/donation_box_2',methods=['GET','POST'])
def donation_box_2():
    if('caseid' in session):
        if(request.method=='POST'): 
            caseid= request.args.get('caseid')
            amt = request.form['damt']
            return render_template("donor_2.html",damt=amt,caseid=caseid)
            # return redirect(url_for("/donor",damt=amt))
        else:
            return render_template("error.html")

@app.route('/donor_info',methods=['POST'])
def donor_info():
    if('caseid' in session):
        if(request.method=='POST'):
            dname = request.form['dname']
            demail = request.form['demail']
            dpan = request.form['dpan']
            damt = int(request.form['damt'])
        # ------------donor---------------------
            ob = donor_operation()
            ob.donor_info(dname,demail,dpan,damt)
            
            data = {"amount": damt*100,"currency":"INR","receipt":"order_rcptid_11"}
            payment = client.order.create(data=data)
            pdata=[damt*100,payment["id"]]
            return render_template("pay.html",pdata=pdata)
    else:
        return redirect(url_for('error'))

@app.route('/success', methods=["POST"])
def success():
    if('email' in session):
        if(request.method=='POST'):
            pay_id=request.form.get("razorpay_payment_id")
            ord_id=request.form.get("razorpay_order_id")
            sign=request.form.get("razorpay_signature")
            # created_at=request.form.get("razorpay_created_at")
            params={
            'razorpay_order_id': ord_id,
            'razorpay_payment_id': pay_id,
            'razorpay_signature': sign
            }
            final=client.utility.verify_payment_signature(params)
            if final == True:
                
                ob = donor_operation()
                ob.payment(pay_id,ord_id)
                r = ob.receipt(pay_id)
                
                # flash("Payment Done Successfully!! payment ID is "+str(pay_id))
                return render_template("receipt.html",record=r)
            return "Something Went Wrong Please Try Again"
    elif('caseid' in session):
        if(request.method=='POST'):
            pay_id=request.form.get("razorpay_payment_id")
            ord_id=request.form.get("razorpay_order_id")
            sign=request.form.get("razorpay_signature")
            # created_at=request.form.get("razorpay_created_at")
            params={
            'razorpay_order_id': ord_id,
            'razorpay_payment_id': pay_id,
            'razorpay_signature': sign
            }
            final=client.utility.verify_payment_signature(params)
            if final == True:
                
                ob = donor_operation()
                ob.payment(pay_id,ord_id)
                r=ob.receipt(pay_id)
                
                # flash("Payment Done Successfully!! payment ID is "+str(pay_id))
                return render_template("receipt_2.html",record=r)
            return "Something Went Wrong Please Try Again"
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('error'))
        

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/about_2')
def about_2():
    return render_template("about_2.html")

@app.route('/admin_login',methods=['GET','POST'])
def admin():
        if(request.method=='GET'):
            return render_template('admin_login.html')
        elif(request.method=='POST'):
            user = request.form['user']
            password = request.form['password']
            ob = admin_operation()
            rc=ob.admin_login(user,password)
            if(rc==0):
                flash("invalid email or password!!")
                return redirect(url_for('admin_login'))
            else:
                return redirect(url_for("admin_dashboard"))
            #return session['name']
        else:
            return render_template("error.html")
        
@app.route('/admin_logout', methods=['GET','POST'])
def admin_logout():
    if('user' in session):
        if(request.method=='GET'):
            session.clear()
            flash("Log Out Successfully")
            return redirect(url_for('index'))
        else:
            flash("You are not login yet! please Login first")
            return redirect(url_for('admin_login'))   
    else:
        return render_template("error.html")

@app.route("/admin_dashboard",methods=['GET','POST'])
def admin_dashboard():
    if("user in session"):
        if(request.method=='GET'):
            ob = admin_operation()
            record = ob.admin_info()
            a=ob.status_info()
            return render_template("admin_dashboard.html",record=record,a=a)
        elif(request.method==['POST']):
            ob = admin_operation()
            record = ob.admin_info()
            a=ob.status_info()
            return render_template("admin_dashboard.html",record=record,a=a)
        else:
            return "error"

@app.route("/status",methods=['POST'])
def status():
    if (request.method=='POST'):
        ob = admin_operation()
        record=ob.admin_info()
        caseid = request.args.get('case_id')
        ob.status_update(caseid)
        flash("status updated successfully")
        return redirect(url_for("admin_dashboard",record=record))




if __name__==("__main__"):
    app.run(debug=True)