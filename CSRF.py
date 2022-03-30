# from flask import Flask 
# from flask import request 
 
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['pwd']
#         print(email, password)
		 
# 		# code that uses the data you've got 
# 		# in our case, checking if the user exists 
# 		# and logs them in, if not redirect to sign up
# 
# 
from distutils.log import debug
from flask import Flask, request, render_template, url_for, redirect
from array import *
import string    
import random
# from flask import Flask


app = Flask(__name__,template_folder='templates', static_folder='static')
user_details=[[]]
login=0
cookie="none"
size=25
user_details[0]=["email","password","balance","profession","last_trans"] #to+balance

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST'])
# def my_form_post():
#     email = request.form['email']
#     password = request.form['pwd']
#     email = request.form['email']
#     password = request.form['pwd']

#     return render_template('pass.html',email=email, password = password)

@app.route('/index', methods=['GET', 'POST'])
# @app.route('/trans.html')
def index():
    global login
    global cookie
    global size
    formid = request.args.get('formid', 1, type=int)
    if formid==1:
        email = request.form['email']
        password = request.form['pwd']
        for i in range(len(user_details)):
            if(user_details[i][0]==email and user_details[i][1]==password):
                # print(login)
                login=1
                ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))    
                cookie = str(ran)
        if(login==0):
            return render_template('home.html',msg="Invalid username and password")
        return render_template('loggedin.html',email=email, password = password, login=login,cookie=cookie)
        # return redirect(url_for('loggedin',email=email, password = password, login=login,cookie=cookie) )

    if formid== 2:
        email = request.form['email']
        password = request.form['pwd']
        profession= request.form['prof']
        i= len(user_details)
        user_details.insert(i,[email,password,"1000",profession,""])
        
        return render_template('pass.html',email=email, password = password, res=user_details[1][0])

    if formid==3:
        fro = request.form['from']
        to = request.form['to']
        amount = request.form['amount']
        client_cookie = request.form['cookie']

        if(client_cookie == cookie):
            for i in range(len(user_details)):
                if(user_details[i][0]==to):
                    user_details[i][2]= int(user_details[i][2])+int(amount)
                    ans1=user_details[i][2]
                if(user_details[i][0]==fro):
                    user_details[i][2]=str(int(user_details[i][2])-int(amount))
                    ans2=user_details[i][2]
            return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your balance is: "+ans2,cookie=client_cookie)
        else:    
            return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is not successful.",cookie=client_cookie)

    if formid==4:
        client_cookie = request.form['cookie']
        return render_template('transaction.html',cookie=client_cookie)
        

# @app.route('/trans',methods=['POST'])
# def trans():
#     fro = request.form['from']
#     to = request.form['to']
#     amount = request.form['amount']

#     return render_template('pass.html',email=fro, password = to, res=amount)


if __name__ == "__main__":
    app.run(debug=True)