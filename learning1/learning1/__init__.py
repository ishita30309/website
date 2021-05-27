"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import learning1.views
