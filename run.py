#!flask/bin/python
import sqlite3
from flask import Flask
from flask import render_template,flash, redirect
from flask.ext.login import LoginManager
app= Flask(__name__)
app.config.from_object('config')

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required,user_logged_in

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,PasswordField, validators,TextField,TextAreaField,IntegerField
from wtforms.validators import DataRequired
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Message, Mail
from werkzeug import generate_password_hash,check_password_hash
from datetime import datetime
class URLForm(Form):
	url = StringField('url', validators=[DataRequired()])

@app.route('/home', methods=['GET', 'POST'])
def home():
	try:
        	c=sqlite3.connect('test.db')
        	c.execute('CREATE TABLE RECORD(ID INTEGER PRIMARY KEY,URL TEXT, STURL TEXT)');
		c.commit()
        	c.close()
	except:
        	None
	
	form= URLForm()
	d=[]
	c=sqlite3.connect('test.db')
	new=c.execute("SELECT * FROM RECORD");
	for i in new:
		d.append(i[2])
	e=[]
	if len(d)>0:
		e=d[-1]
	if form.validate_on_submit():
		c="1q2w3e4r5t6y7u8i9o0p1a2s3d4f5g6h7j8k9l0z1x2c3v4b5n6m"
		sign="/+-="
		url=form.url.data
		p = sqlite3.connect('test.db')
		a="127.0.0.1:5000/"
		b=0
		for u in url:
			b+=1
			if u in sign:
				a+=c[b]
				b=0			
		p.execute("INSERT INTO RECORD(URL,STURL) VALUES(?,?)",[url,a]);	
		p.commit()
		p.close()
		return redirect('/home')	
	return render_template('home.html',form=form,e=e)

@app.route('/<msg>')
def capture_value(msg):
	b=[]
	a="127.0.0.1:5000/"
	a+="%s" % (msg)
	c = sqlite3.connect('test.db')
  	url=c.execute("SELECT * FROM RECORD WHERE STURL = ?",[a]);
	for u in url:
		b.append(u[1])		
	if len(b)>0:
  		return redirect(b[0])
	#c.commit()
	#c.close() 
  	return render_template('h.html',url=url)



app.run(debug=True)



