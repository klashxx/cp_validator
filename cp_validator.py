#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Estructura de los ficheros:


POSTAL.txt

id_registro:        8
cod_localidad:      4
cod_ine:            16 (5 primeros municipo)
cod_via:            3 (Vacio = calle)
nombre_via:         79
impar_inferior:     4
inf_impar_inferior: 3
impar_superior:     4
inf_impar_superior: 3
par_inferior:       4
inf_par_inferior:   3
par_superior:       4
inf_par_superior:   3
cod_postal:         5

CODCIU.txt
cod_localidad:      4
nombre_localidad:   50

CODVIA.txt
cod_via:            3
descripcion_via:    20
"""

import os

__ppath__ = os.path.dirname(os.path.realpath(__file__))

DIR_FILES = '{0}/files'.format(__ppath__)
POSTAL_FILE = '{0}/POSTAL-t_0.txt'.format(DIR_FILES)
VIA_FILE = '{0}/CODVIA_0.txt'.format(DIR_FILES)
CIU_FILE = '{0}/CODCIU_0.txt'.format(DIR_FILES)

def load_ciu():
    """Carga la información relativa a localidad"""
    cius = {}
    with open(CIU_FILE) as ciu_handler:
        for line in ciu_handler:
            cod_localidad = line[:4]
            nombre_localidad = line[4:54].rstrip()
            cius[cod_localidad] = nombre_localidad

    return cius

def main():
    """Controlador"""
    cius = load_ciu()


if __name__ == '__main__':
    main()
