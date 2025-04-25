from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_tempo', methods=['POST'])
def calcular_tempo():
    try:
        km = float(request.form['km'])
        km_h = float(request.form['km_h'])

        horas = int(km // km_h)
        minutos = int(((km / km_h) - horas)*60)

        if minutos == 0:
            minutos = "00"

        return render_template('index.html', horas = horas, minutos=minutos)
    except Exception as e:
        horas = f'Ocorreu um erro inesperado {e}'
        minutos = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html', horas = horas, minutos=minutos)

if __name__ == '__main__':
    app.run(debug=True)
