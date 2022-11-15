from flask import Flask
app=Flask(__name__)
app.secret_key="rootroot" 
#this is the signature of the cookie for session
#to use session there must be a secret key here