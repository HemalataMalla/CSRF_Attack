from distutils.log import debug
from flask import Flask, make_response, request, render_template, url_for, redirect
from array import *
import string    
import random
# from flask import Flask
from distutils.log import debug
from flask import Flask, request, render_template, url_for, redirect
from array import *
import string    
import random
Base_accno=1000
amount='100000'
filename='data.txt'
data=[]
usernames=[]
username_login=""
user_details=[]
balance=100000

#function to get all values from the file
def readfile():
    global data
    data.clear()
    global usernames
    usernames.clear()
    file=open(filename,'r')
    line=file.readline().strip()
    while line:
        values=line.split('\t')    
        data.append(values)
        usernames.append(values[2])
        line=file.readline().strip()
    print(data)
    print(usernames)
    file.close()
    
#check for username

def check(username):
    temp=1
    readfile()
    print(usernames)
    for name in usernames:
        if name==username:
            temp=0
    return temp

#function for storing data in to the file
def signin(email,username,password,profession):
    global Base_accno
    c=check(username)
    if c==0:
        print("user already exist")
        
        return 0
    else:
        readfile()
        l=len(data)
        file=open(filename,'a')
        #paswd=convert(password)
        file.write(str(Base_accno+l)+'\t'+email+'\t'+username+'\t'+password+'\t'+profession+'\t'+amount+'\n')
        file.close()
        return 1
#function for login
def checklogin(username,password):
    readfile()
    temp=0
    for row in data:
        if row[2]==username and row[3]==password:
            temp=1
    return temp

#get user details
def getdetails(username):
    global user_details
    user_details.clear()
    global username_login
    readfile()
    for row in data:
        if row[2]==username:
            user_details=row.copy()

#check balance
def check_balance(fro,amount):
    readfile()
    for row in data:
        if row[2]==fro:
            if int(row[5]) < amount:
                return 0
    return 1
#transfer money
def amount_transfer(fro,to,amount):
    global balance
    readfile()
    ch=check_balance(fro,amount)
    if ch ==1 :
        for row in data:
            if row[2]==fro:
                row[5]=str(int(row[5])-amount)
                balance=str(row[5])
            if row[2]==to:
                row[5]=str(int(row[5])+amount)
        file=open(filename,'w')
        for row in data:
            file.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\n')
        file.close()
        return 1
    else:
        return 0

#
def getbalance(username):
    readfile()
    for row in data:
        if row[2]==username:
            return row[5]
    return ""

    
    

app = Flask(__name__,template_folder='templates', static_folder='static')
login=0
cookie="none"
token="none"
resp=""
size=25

# user_details[0]=["email","password","balance","profession","last_trans"] #to+balance

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    global login
    global cookie
    global size
    global token
    global username_login
    global resp
    formid = request.args.get('formid', 1, type=int)
    if formid==1:
        username = request.form['username']
        password = request.form['pwd']
        # for i in range(len(user_details)):
        #     if(user_details[i][0]==email and user_details[i][1]==password):
        #         login=1
        #         ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))    
        #         cookie = str(ran)
        # if(login==0):
        #     resp = make_response(render_template('home.html',msg="Invalid username and password"))
        #     # resp.set_cookie('cookie', cookie)

        #     # resp.set_cookie('same-site-cookie', 'foo', samesite='Lax') # same-site cookie
        #     # resp.set_cookie('cross-site-cookie', 'bar', samesite='Lax', secure=True)

        #     return render_template('home.html',msg="Invalid username and password")
        # else:

        #     resp = make_response(render_template('loggedin.html',email=email, password = password, login=login,cookie=cookie))
        #     resp.set_cookie('cookie', cookie)

        #     # resp.set_cookie('same-site-cookie', cookie, samesite='Lax') #Same-site cookie
        #     # resp.set_cookie('cross-site-cookie', cookie, samesite='Lax', secure=True)
        #     return resp
        x = checklogin(username,password)
        if x==0:
            #login failed
            return render_template('faillogin.html')
        if x==1:
            #login sucess
            username_login=username
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))
            cookie = str(ran)
            resp = make_response(render_template('loggedin.html',username_login=username_login, password = password, login=login,cookie=cookie))
            resp.set_cookie('cookie', cookie)

            # resp.set_cookie('same-site-cookie', cookie, samesite='Lax') #Same-site cookie
            # resp.set_cookie('cross-site-cookie', cookie, samesite='Lax', secure=True)
            return resp
            # return render_template('loggedin.html',email=username, password = password,cookie=cookie)

          
    if formid== 2:
        # email = request.form['email']
        # password = request.form['pwd']
        # profession= request.form['prof']
        # i= len(user_details)
        # user_details.insert(i,[email,password,"1000",profession,""])

        # ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))    
        # token = str(ran)
        
        # return render_template('pass.html',email=email, password = password, res=user_details[1][0],token=token)

        email = request.form['email']
        password = request.form['pwd']
        profession= request.form['prof']
        username = request.form['username']
        #i= len(user_details)
        #user_details.insert(i,[email,password,"1000",profession,""])
        x = signin(email,username,password,profession)
        if x==1:
            print('login sucessful')
            return render_template('pass.html',email=email, password = password, res=password)
        else:
            print('login failed')
            return render_template('fail.html',email=email, password = password, res=password)
        
    
@app.route('/home')
def homepage():
    global username_login
    return render_template("loggedin.html",username_login=username_login,cookie=cookie,token=token)

@app.route('/trans')
def trans():
    global username_login
    return render_template("transaction.html",username_login=username_login, cookie=cookie,token=token)

@app.route('/MyAccount')
def MyAccount():
    getdetails(username_login)
    return render_template("MyAccount.html",accno=user_details[0],email=user_details[1],username=user_details[2],profession=user_details[4],balance=user_details[5])

@app.route('/logout')
def logout():
    # global resp
    # resp.delete_cookie('cookie')
    resp = make_response(render_template('home.html'))
    resp.set_cookie('cookie', cookie)
    return render_template("home.html")


@app.route('/transaction',methods=['GET', 'POST'])
def transaction():
    global username_login
    global cookie
    # fro = request.form['from']
    fro=username_login
    to = request.form['to']
    amount = request.form['amount']
    client_cookie = request.cookies.get('cookie')
    
    # client_cookie = request.cookies.get('cross-site-cookie') #same-site cookie solution

    # client_token = request.form['token'] #Synchronized Tokens
    c=check(to)
    if(c == 1):
        return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is not successful because to user details are not correct",cookie=client_cookie)
    elif(client_cookie == cookie ):
    # elif(1 == 1 ):
        # if(client_token==token): # check for Synchronized token
            # for i in range(len(user_details)):
            #     if(user_details[i][0]==to):
            #         user_details[i][2]= int(user_details[i][2])+int(amount)
            #         ans1=user_details[i][2]
            #     if(user_details[i][0]==fro):
            #         user_details[i][2]=str(int(user_details[i][2])-int(amount))
            #         ans2=user_details[i][2]
            # return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your Balance is: "+ans2,cookie=client_cookie)

            # return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your Balance is: "+ans2,cookie=client_cookie,token=token,client_token=client_token)

            x = amount_transfer(fro,to,int(amount))
            if x== 1:
                return '', 204
                # return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your balance is:"+balance,cookie=client_cookie)
            else:   
                return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is not successful"+balance,cookie=client_cookie)
 
        # return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is not successful.",cookie=client_cookie,token=token, client_token=client_token)
    else:
        return ""
if __name__ == "__main__":
    app.run(debug=True)
