from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
import threading

app = Flask(__name__)
socketio = SocketIO(app, reconnection=True, reconnection_attempts=3)


ser_lock = threading.Lock()
ser_instance = None


def initialize_serial():
    global ser_instance
    with ser_lock:
        if ser_instance is None:
            ser_instance = serial.Serial('COM5', 9600)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('update_request')
def handle_update_request():
    initialize_serial()  # Garante que a porta serial está inicializada
    with ser_lock:
        if ser_instance is not None:
            try:
                data = ser_instance.readline().decode('utf-8').strip()
                if data:
                    print('valor enviado via Socket.IO:', data)
                    socketio.emit('update_data', {'value': data})
            except Exception as e:
                print('Erro na leitura serial:', e)


if __name__ == '__main__':

    # Inicia o servidor Flask-SocketIO
    socketio.run(app, debug=True)
