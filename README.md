# FlaskSerialSensor

FlaskSerialSensor is a simple example application that combines Flask for web rendering and Socket.IO for real-time communication. The application simulates a luminosity sensor reading from a serial port and updates the web page dynamically based on the received data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/seu-usuario/FlaskSerialSensor.git
   cd FlaskSerialSensor

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Flask application:
    ```bash
    python flask_app.py

This will start the Flask application on http://localhost:5000.

4. In a separate terminal, run the Socket.IO server:
    ```bash
    python socketio_server.py

This will start the Socket.IO server on http://localhost:5001.

5. Open your browser and navigate to http://localhost:5000 to see the Flask application.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License