# -*- coding: utf-8 -*-
"""
REST API
"""
from flask import jsonify, abort, make_response, url_for
from cp_validator import app, postals


@app.before_first_request
def public_urls():
    for codigo, data in postals.items():
        postals[codigo] = {'uri': url_for('get_cp',
                                          codigo=codigo,
                                          _external=True),
                           'data': data}
    return None


@app.route('/cp/api/v1.0/codigos', methods=['GET'])
def get_postals():
    return jsonify({'codigos': postals})


@app.route('/cp/api/v1.0/codigos/<codigo>', methods=['GET'])
def get_cp(codigo):
    if codigo not in postals:
        abort(404)
    return jsonify({codigo: postals[codigo]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'CP no encontrado'}), 404)
