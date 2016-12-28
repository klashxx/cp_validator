# -*- coding: utf-8 -*-
"""
Estructura de los ficheros:

POSTAL.txt
==========

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
==========

cod_localidad:      4
nombre_localidad:   50

CODVIA.txt
==========

cod_via:            3
descripcion_via:    20
"""

from cp_validator.conf.settings import CIU_FILE, VIA_FILE, POSTAL_FILE

def load_cius():
    """Carga la información relativa a localidad"""

    cius = {}
    with open(CIU_FILE) as ciu_handler:
        for reg in ciu_handler:
            cius[reg[:4]] = reg[4:54].rstrip()

    return cius

def load_vias():
    """Carga la información relativa a vias"""

    vias = {}
    with open(VIA_FILE) as via_handler:
        for reg in via_handler:
            vias[reg[:3]] = reg[3:23].rstrip()

    return vias


def get_postal():
    """Carga la información relativa a CP"""

    cius = load_cius()
    vias = load_vias()

    postal = {}
    with open(POSTAL_FILE) as postal_handler:
        for reg in postal_handler:

            cod_via = reg[29:32].rstrip()
            cod_via = 'CAL' if not cod_via else cod_via
            try:
                tipo_via = vias[cod_via]
            except KeyError:
                tipo_via = 'SIN_DATOS'

            cod_localidad = reg[8:12]
            try:
                localidad = cius[cod_localidad]
            except KeyError:
                localidad = 'SIN_DATOS'

            post = {'id_registro': reg[:8],
                    'cod_localidad': reg[8:12],
                    'localidad': localidad,
                    'cod_municipio': reg[13:18],
                    'cod_ine': reg[13:29],
                    'tipo_via': tipo_via,
                    'nombre_via': reg[32:111].rstrip(),
                    'impar_inferior': (None if not reg[111:115].rstrip()
                                       else reg[111:115].rstrip()),
                    'inf_impar_inferior': (None if not reg[115:118].rstrip()
                                           else reg[115:118].rstrip()),
                    'impar_superior': (None if not reg[118:122].rstrip()
                                       else reg[118:122].rstrip()),
                    'inf_impar_superior':  (None if not reg[122:125].rstrip()
                                            else reg[122:125].rstrip()),
                    'par_inferior': (None if not reg[125:129].rstrip()
                                     else reg[125:129].rstrip()),
                    'inf_par_inferior': (None if not reg[129:132].rstrip()
                                         else reg[129:132].rstrip()),
                    'par_superior': (None if not reg[132:136].rstrip()
                                     else reg[132:136].rstrip()),
                    'inf_par_superior': (None if not reg[136:139].rstrip()
                                         else reg[136:139].rstrip()),
                    'estado': reg[144:145].rstrip()}

            cod_postal = reg[139:144]
            if cod_postal not in postal:
                postal[cod_postal] = [post]
            else:
                postal[cod_postal].append(post)

    return postal
