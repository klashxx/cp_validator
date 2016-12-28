#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Validador de Códigos Postales
"""


from cp_validator.lib.extractor import get_postal



def main():
    """Controlador"""

    postals = get_postal()

    return None

if __name__ == '__main__':
    main()
