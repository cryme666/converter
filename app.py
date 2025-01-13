from flask import Flask, render_template, request

app = Flask('Test app')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    user_input = request.form.get('user_input')
    print(dict(request.form))

    print('-'*100)

    return f'Your wrote {user_input}'


app.run(debug=True)