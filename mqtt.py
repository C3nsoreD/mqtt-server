'''
Test application for MQTT
'''
from flask import Flask
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

def create_app():
    app = Flask(__name__)
    mqtt = Mqtt(app)

