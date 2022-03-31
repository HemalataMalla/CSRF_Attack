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
        file=open(filename,'a')
        #paswd=convert(password)
        file.write(str(Base_accno)+'\t'+email+'\t'+username+'\t'+password+'\t'+profession+'\t'+amount+'\n')
        Base_accno=Base_accno+1
        file.close()
        return 1




#function 
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
        username = request.form['username']
        password = request.form['pwd']
        #for i in range(len(user_details)):
            #if(user_details[i][0]==email and user_details[i][1]==password):
                # print(login)
                #login=1
                #ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))    
                #cookie = str(ran)
        #if(login==0):
            #return render_template('home.html',msg="Invalid username and password")
        #return render_template('loggedin.html',email=email, password = password, login=login,cookie=cookie)
        # return redirect(url_for('loggedin',email=email, password = password, login=login,cookie=cookie) )
        # x = checklogin(username,password)
        # if x==0:
        #     return 0
        #     #login failed
        # if x==1:
        #     #login sucess
        #     ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))
        #     cookie = str(ran)
            

    if formid== 2:
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
        

    if formid==3:
        fro = request.form['from']
        to = request.form['to']
        amount = request.form['amount']

        for i in range(len(user_details)):
            if(user_details[i][0]==to):
                user_details[i][2]= int(user_details[i][2])+int(amount)
                ans1=user_details[i][2]
            if(user_details[i][0]==fro):
                user_details[i][2]=str(int(user_details[i][2])-int(amount))
                ans2=user_details[i][2]
        return render_template('transaction.html',msg="Transaction from "+fro+" to "+to+" of Rs."+amount+" is successful. Your balance is: "+ans2)

    if formid==4:
        return render_template('transaction.html')
        

# @app.route('/trans',methods=['POST'])
# def trans():
#     fro = request.form['from']
#     to = request.form['to']
#     amount = request.form['amount']

#     return render_template('pass.html',email=fro, password = to, res=amount)


if __name__ == "__main__":
    app.run(debug=True)
