
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/windesheim')
def windesheim():
    return render_template('windesheim.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/swaanen')
def zwanen():
    return render_template('swaanen.html')

@app.route('/brabant')
def brabant():
    return render_template('brabant.html')

@app.route('/kleine_verschil')
def kleine_verschil():
    return render_template('kleine_verschil.html')

@app.route('/baby_sitting')
def baby_sitting():
    return render_template('baby_sitting.html')

@app.route('/onsz')
def onsz():
    return render_template('onsz.html')

@app.route('/pepperminds')
def pepperminds():
    return render_template('pepperminds.html')

@app.route('/vinea')
def vinea():
    return render_template('vinea.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
