from flask import Flask

app = Flask(__name__) #__name__ variable especial

from app import routes
