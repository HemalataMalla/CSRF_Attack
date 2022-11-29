# CSRF_attack Implementation and Preventions techiniques

Cross-Site Request Forgery (CSRF) is the vulnerability in which the attacker forges a request to the server via an authorized user of the server.

Here, when a user accesses the server and requests any action, the server will check if the user is loggedin or not. If the user is authorized then if the server performs the action requested by none or solely using the user's cookies then the server is vulnerable to CSRF attack. The attacker if somehow makes the user click the malicious link, the same action request is sent to server leading to the attack.

In our implementation we have 3 folders. Attcak, Synchronizer tokens, same-site cookies. 

Requirements:
    Python: sudo apt install python3.8
    flask: pip install Flask

Command needed to run the code:
    python3 CSRF.py

//Above command for each folder should be run inside the respective folders.

# The Attack
Attack: 
This folder is the implementation of the CSRF attack. The static folder consists of style part and image files, templates folder consists the html files. CSRF.py is the server file.

Steps:
1. Run the CSRF.py file using the above command. Once the server starts, it will provide a link/localhost to the Banking server. The user can register and login and perform transaction operation.
The balance of the account can be seen in MyAccount page.

2. Now if the user clicks on the attacker.html file, "Click here" image, then the balance in the account can be seen decreased.

# Preventions
Synchronizer tokens:
This contains the prevention technique called Synchronizer tokens or Anti-CSRF tokens. In this, the server will maintain a randomly generated token for each user. While submitting any request the token will be submitted hiddenly to the server and server will match the token. The attacker won't be able to identify the token associated with the user thus the attack is prevented. 
The static folder consists of style part and image files, templates folder consists the html files. CSRF.py is the server file.

Steps:
1. Run the CSRF.py file using the above command. Once the server starts, it will provide a link/localhost to the Banking server. The user can register and login and perform transaction operation.
The balance of the account can be seen in MyAccount page.

2. Now if the user clicks on the attacker.html file, "Click here" image, then we can see no change  in the balance of the user.

same-site cookie:
This folder contains the prevention technique called same-site cookie. In this, the cookies sent to the user will be valid only for one browser. If the user accesses the malicious link from another site, it won't be able to trigger the required action as the attacker can't tell whether cookies are used or same-site cookies. 
The static folder consists of style part and image files, templates folder consists the html files. CSRF.py is the server file.

Steps:
1. Run the CSRF.py file using the above command. Once the server starts, it will provide a link/localhost to the Banking server. The user can register and login and perform transaction operation.
The balance of the account can be seen in MyAccount page.

2. Now if the user clicks on the attacker.html file, "Click here" image, then we can see no change  in the balance of the user.
