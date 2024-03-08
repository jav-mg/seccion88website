from flask import *
from consultas import *

import sys                                          # necesario para mandar a imprimir prints a consola
# import logging
# logging.basicConfig(level=logging.DEBUG)

#instanciar servidor
app = Flask(__name__)
