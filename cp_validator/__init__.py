# -*- coding: utf-8 -*-

import os
import sys

__author__ = 'Juan Diego Godoy Robles'
__version__ = '0.1'
__ppath__ = os.path.dirname(os.path.realpath(__file__))
if __ppath__ not in sys.path:
    sys.path.append(os.path.dirname(__ppath__))

from flask import Flask
app = Flask(__name__)

from cp_validator import extractor
postals = extractor.get_postal()

import cp_validator.views
