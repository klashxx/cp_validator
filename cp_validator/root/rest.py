#!flask/bin/python
"""
RESTful API
"""
from flask import Flask, jsonify, abort, make_response, url_for
from cp_validator.root.extractor import get_postal

postals = get_postal()
app = Flask(__name__)


@app.route('/cp/api/v1.0/codigos', methods=['GET'])
def get_postals():
    return jsonify({'codigos': public_urls(postals)})


@app.route('/cp/api/v1.0/codigos/<codigo>', methods=['GET'])
def get_cp(codigo):
    if codigo not in postals:
        abort(404)
    return jsonify({codigo: postals[codigo]})


def public_urls(postals):
    for codigo, data in postals.items():
        postals[codigo] = {'uri': url_for('get_cp',
                                          codigo=codigo,
                                          _external=True),
                           'data': data}
    return postals


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'CP no encontrado'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
