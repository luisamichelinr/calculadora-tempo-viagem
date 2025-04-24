from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_tempo', methods=['POST'])
def calcular_tempo():
    km = float(request.form['km'])
    km_h = float(request.form['km_h'])

    horas = round(km / km_h, 2)

    return render_template('index.html', horas = horas)

if __name__ == '__main__':
    app.run(debug=True)