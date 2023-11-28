<div align="center">

![FlaskSerialIO](https://i.ibb.co/nMMmj2m/image.png)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](https://pypi.org/project/FlaskSerialIO/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/FlaskSerialIO)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/FlaskSerialIO)
![PyPI](https://img.shields.io/pypi/v/FlaskSerialIO)

</div>

# FlaskSerialIO Documentation

**FlaskSerialIO** is a Python library that simplifies the communication between a Flask web application and a serial port through Socket.IO. This documentation provides an overview of the library and demonstrates its usage with examples.

## Installation

Install FlaskSerialIO using pip:

```python
pip install FlaskSerialIO
```
## Quick Start
* Import the **FlaskSerialIO** class.
*  Create an instance, specifying the serial port and, optionally, the template name.
*  Define routes and handlers as needed.
*  Run the **FlaskSerialIO** application.
  
```python
# main.py
from flask_serial_io import FlaskSerialIO

def custom_route():
    return "Custom Route"

if __name__ == '__main__':
    # Create a FlaskSerialIO instance, specifying the serial port and optional template name.
    flask_serial_io = FlaskSerialIO(serial_port='COM5', template_name='index.html')

    # Add custom routes if needed.
    flask_serial_io.add_route('/custom', custom_route)

    # Run the FlaskSerialIO application.
    flask_serial_io.run(debug=True)
```
## Usage
### Creating an Instance
```python
flask_serial_io = FlaskSerialIO(serial_port='COM5', template_name='index.html')
```

### Adding Custom Routes
```python
def custom_route():
    return "Custom Route"

flask_serial_io.add_route('/custom', custom_route)
```

### Initializing Serial Communication
The library automatically initializes the serial communication when handling update requests. However, you can manually initialize it using:
```python
flask_serial_io.initialize_serial()
```

### Handling Update Requests
The library provides a default route (/) and an update request handler that reads data from the serial port and emits it to the connected clients.

### Running the Application
```python
flask_serial_io.run(debug=True)
```



