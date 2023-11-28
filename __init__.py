from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
import threading


class FlaskSerialIO:
    def __init__(self, serial_port, template_name='index.html'):
        self.app = Flask(__name__)
        self.socket_io = SocketIO(self.app, reconnection=True, reconnection_attempts=3)
        self.serial_port = serial_port
        self.template_name = template_name
        self.serial_lock = threading.Lock()
        self.serial_instance = None

        @self.app.route('/')
        def home():
            return render_template(self.template_name)

        @self.socket_io.on('update_request')
        def handle_update_request():
            self.initialize_serial()
            with self.serial_lock:
                if self.serial_instance is not None:
                    try:
                        data = self.serial_instance.readline().decode('utf-8').strip()
                        if data:
                            self.socket_io.emit('update_data', {'value': data})
                    except Exception as e:
                        print('Error reading serial:', e)

    def initialize_serial(self):
        with self.serial_lock:
            if self.serial_instance is None:
                self.serial_instance = serial.Serial(self.serial_port, 9600)

    def add_route(self, route, view_function):
        self.app.add_url_rule(route, view_func=view_function)

    def run(self, debug=True):
        self.socket_io.run(self.app, debug=debug)
