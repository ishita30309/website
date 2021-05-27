"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from learning1 import app
import json
import ast

items=[]
texts=[]
def write_file(filename,items):
    f=open(filename,"w")
    f.write(str(items))
    f.close()
def read_file(filename):
   
    f=open(filename,"r")
    content=f.read()
    f.close()
    return content

@app.route('/',methods=["POST","GET"])
@app.route('/home',methods=["POST","GET"])
def home():
    """Renders the home page."""
    
    
    global items

    
    if not items:
        #items=[{'FirstName':'ishita','LastName':'goyal','PhoneNumber':'7696330309','EmailID':'ishita30309@gmail.com','Username':'ishita','Password':'Ishita@2002','ConfirmPassword':'Ishita@2002'}]
        content=read_file("user_details.txt")
        if content=="":
            content="[]"
        items = ast.literal_eval(content)
    global texts
    if not texts:
        texts=[{'EmailID':'ishita30309@gmail.com','Username':'ishita','Password':'Ishita@2002','ConfirmPassword':'Ishita@2002'}]
    if request.method=="POST":
        
        user=request.form["username"]
        pwd=request.form["pwd"]
        for item in items:
            if item["Username"]==user:
                return render_template('dashboard.html',title=user,year=datetime.now().year,item=items)
        return render_template('index.html',title='Ishita',year=datetime.now().year)
    else:
        return render_template('index.html',title='Ishita',year=datetime.now().year)

@app.route('/signup',methods=["POST","GET"])
def signup():
    lstcountry=read_file("country.txt")
    lstcountry=(lstcountry.splitlines())
    lststate=read_file("state.txt")
    lststate=(lststate.splitlines())
  
    if request.method=="POST":
        items.append({'FirstName':request.form["fname"],'LastName':request.form["lname"],'PhoneNumber':request.form["phone"],'EmailID':request.form["email"],'Username':request.form["username"],'Password':request.form["password"],'ConfirmPassword':request.form["confirmpassword"]})
        write_file("user_details.txt",items)
        return render_template('index.html',title='Ishita',year=datetime.now().year)
    return render_template(
        'signup.html',
        title='Signup',
        year=datetime.now().year,
        message='Your Signup page.',item=items,country=lstcountry,state=lststate
        
    )

@app.route('/ForgetPassword',methods=["POST","GET"])
def ForgetPassword():
    """Renders the ForgetPassword page."""
    if request.method=="POST":
       texts.append({'EmailID':request.form["email"],'Username':request.form["username"],'Password':request.form["password"],'ConfirmPassword':request.form["confirmpassword"]})
       for i in items:
           if i["Username"]==request.form["username"]:
               i["Password"]=request.form["password"]
       return render_template('index.html',title='Ishita',year=datetime.now().year)
    else:
        return render_template(
        'ForgetPassword.html',
        
        title='ForgetPassword',
        year=datetime.now().year,
        message='Your ForgetPassword page.',text=texts
    )
@app.route('/dashboard',methods=["POST","GET"])
def dashboard():
    
    
    return render_template(
        'dashboard.html',
        align="right",
        title='dashboard',
        year=datetime.now().year,
        message='Your dashboard page.',item=items
    )
@app.route('/logout',methods=["POST","GET"])
def logout():
    """Renders the ForgetPassword page."""
    return render_template(
        'index.html',
        align="right",
        title='dashboard',
        year=datetime.now().year,
        message='Your dashboard page.'
    )

