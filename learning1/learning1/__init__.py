"""
The flask application package.
"""

from flask import Flask,session
app = Flask(__name__)
app.secret_key = "abc"

import learning1.views
