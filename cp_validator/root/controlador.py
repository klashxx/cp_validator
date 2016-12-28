# -*- coding: utf-8 -*-
"""Modulo controlador"""

from cp_validator.root.extractor import get_postal

def main(codigo):
    postals = get_postal()

    if codigo not in postals:
        return None

    import json
    return json.dumps({codigo: postals[codigo]},
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
