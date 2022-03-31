from distutils.log import debug
from flask import Flask, make_response, request, render_template, url_for, redirect
from array import *
import string    
import random
# from flask import Flask


app = Flask(__name__,template_folder='templates', static_folder='static')
user_details=[[]]
login=0
cookie="none"
token="none"
size=25
user_details[0]=["email","password","balance","profession","last_trans"] #to+balance

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    global login
    global cookie
    global size
    global token
    formid = request.args.get('formid', 1, type=int)
    if formid==1:
        email = request.form['email']
        password = request.form['pwd']
        for i in range(len(user_details)):
            if(user_details[i][0]==email and user_details[i][1]==password):
                login=1
                ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))    
                cookie = str(ran)
        if(login==0):
            resp = make_response(render_template('home.html',msg="Invalid username and password"))
            # resp.set_cookie('cookie', cookie)

            # resp.set_cookie('same-site-cookie', 'foo', samesite='Lax') # same-site cookie
            # resp.set_cookie('cross-site-cookie', 'bar', samesite='Lax', secure=True)

            return render_template('home.html',msg="Invalid username and password")
        else:

            resp = make_response(render_template('loggedin.html',email=email, password = password, login=login,cookie=cookie))
            resp.set_cookie('cookie', cookie)

            # resp.set_cookie('same-site-cookie', cookie, samesite='Lax') #Same-site cookie
            # resp.set_cookie('cross-site-cookie', cookie, samesite='Lax', secure=True)
            return resp
          
    if formid== 2:
        email = request.form['email']
        password = request.form['pwd']
        profession= request.form['prof']
        i= len(user_details)
        user_details.insert(i,[email,password,"1000",profession,""])

        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))    
        token = str(ran)
        
        return render_template('pass.html',email=email, password = password, res=user_details[1][0],token=token)

    
@app.route('/trans')
def trans():
    return render_template("transaction.html",cookie=cookie,token=token)


@app.route('/transaction',methods=['GET', 'POST'])
def transaction():
    fro = request.form['from']
    to = request.form['to']
    amount = request.form['amount']
    client_cookie = request.cookies.get('cookie')
    
    # client_cookie = request.cookies.get('cross-site-cookie') #same-site cookie solution

    # client_token = request.form['token'] #Synchronized Tokens

    if(client_cookie == cookie ):
        # if(client_token==token): # check for Synchronized token
            for i in range(len(user_details)):
                if(user_details[i][0]==to):
                    user_details[i][2]= int(user_details[i][2])+int(amount)
                    ans1=user_details[i][2]
                if(user_details[i][0]==fro):
                    user_details[i][2]=str(int(user_details[i][2])-int(amount))
                    ans2=user_details[i][2]
            return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your balance is: "+ans2,cookie=client_cookie)

            # return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your balance is: "+ans2,cookie=client_cookie,token=token,client_token=client_token)
    else:   
        return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is not successful.",cookie=client_cookie)
 
        # return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is not successful.",cookie=client_cookie,token=token, client_token=client_token)


if __name__ == "__main__":
    app.run(debug=True)