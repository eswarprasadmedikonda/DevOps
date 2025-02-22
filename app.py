
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return "welcome to the Flask App1go to /register"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
       
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        return render_template('./success.html', name=name, email=email)
    

    return render_template('./reg2.html')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=5000)