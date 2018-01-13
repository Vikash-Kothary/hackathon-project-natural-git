#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
app.py - 
"""

from flask import Flask

app = Flask(__name__)


@app.route('/success')
def success():
    return 'Python is working'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)