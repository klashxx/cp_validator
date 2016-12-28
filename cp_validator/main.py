#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Validador de Códigos Postales
"""
from __future__ import print_function

from docopt import docopt, DocoptExit
from schema import Schema, SchemaError
from cp_validator.root.controlador import main


def cli():
    cli_docs = """cp_validator™ ... validación de códigos postales.
Usage:
  cp_validator <codigo> [options] ...

Options:
  --version            muestra la versión del programa y sale
  -h, --help           muestra la ayuda y sale
  """

    schema = Schema({'<codigo>': str,
                     '--help': int,
                     '--version': int})

    args = docopt(cli_docs)
    try:
        schema.validate(args)
    except SchemaError:
        raise DocoptExit

    try:
        response = main(args['<codigo>'])
    except Exception as error:
        raise DocoptExit('falla cp_validator: {0}'.format(str(error)))

    if response is None:
        print('No se han encontrado resultados')
    else:
        print(response)

    return None


if __name__ == '__main__':
    cli()
