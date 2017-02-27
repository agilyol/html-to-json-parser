from flask import Flask
import os

UPLOAD_FOLDER = ''
app = Flask(__name__)
app.config.from_object('config')

UPLOAD_FOLD = '/htmlfi'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views
