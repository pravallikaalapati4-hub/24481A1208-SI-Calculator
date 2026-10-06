from unittest import result

from flask import Flask,redirect, render_template, url_for,request
app = Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to Flaskapp<=>routing"
@app.route('/greet/<username>')
def greet(username):
    return f"Good morning, {username}!"
'''
@app.route('/delete/<int:roll>')
def delete_user(roll):
    return redirect(url_for('greet'))
'''
@app.route('/calculate', methods=['GET', 'POST'])
def Si():
    if request.method=='POST':
        P = float(request.form['p'])
        R = float(request.form['r'])
        T = float(request.form['t'])
        si = (P*R*T)/100
        total=P+result
        return render_template('index.html', result=result, total=total,p=P,t=T,r=R)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True, port=3500)
