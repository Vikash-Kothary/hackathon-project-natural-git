#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
main.py - 
"""

from __init__ import *
from app import app


def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
