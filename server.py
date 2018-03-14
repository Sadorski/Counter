from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not session.get('count'):
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html", count=session['count'])



@app.route('/1')
def add2():
    if not session.get('count'):
        session['count'] = 0
    session['count'] += 1
    return redirect('/')

@app.route('/2')
def reset():
    session['count'] = 0
    return redirect('/')

    
    

app.run(debug=True)
