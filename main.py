from flask import Flask, render_template
import serial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_data')
def update_data():
    # Abre a porta serial e lê o valor
    with serial.Serial('COM5', 9600) as ser:
        data = ser.readline().decode('utf-8').strip()
        return {'value': data}

if __name__ == '__main__':
    app.run(debug=True)
