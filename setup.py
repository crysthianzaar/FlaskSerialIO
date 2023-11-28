# setup.py
from setuptools import setup, find_packages

setup(
    name='FlaskSerialIO',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'python-socketio',
        'pyserial',
    ],
)
