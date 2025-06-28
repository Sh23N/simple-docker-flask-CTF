from flask import Flask, request, render_template
import os

app=Flask(__name__)

@app.route('/',methods=['GET','POST']) # run this function when user is in /
def register():
	message="please enter your name :"
	result=''
	if request.method=='POST':
		username=request.form.get('username')
		result=os.popen(f"echo {username}").read() # this vulnerble line leads to command injection
		message=f"hello {username}, you must finde flag ;)"
	return render_template(f"form.html",message=message,result=result)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)
