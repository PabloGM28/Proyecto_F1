from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('downforce.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
