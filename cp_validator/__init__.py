# -*- coding: utf-8 -*-
"""
Inicialización
"""

import os
import sys

__author__ = 'Juan Diego Godoy Robles'
__version__ = '0.1'
__args__ = sys.argv[1:]
__ppath__ = os.path.dirname(os.path.realpath(__file__))

if __ppath__ not in sys.path:
    sys.path.append(os.path.dirname(__ppath__))
