from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tyres')
def tyres():
    return render_template('tyres.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/length')
def length():
    return render_template('length.html')

@app.route('/final_strategy')
def final_strategy():
    return render_template('final_strategy.html')

@app.route('/downforce')
def downforce():
    return render_template('downforce.html')

@app.route('/corners')
def corners():
    return render_template('corners.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
