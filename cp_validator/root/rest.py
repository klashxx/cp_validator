#!flask/bin/python
"""
RESTful API
"""
from flask import Flask, jsonify, abort
from cp_validator.root.extractor import get_postal

postals = get_postal()

app = Flask(__name__)

@app.route('/cp/api/v1.0/codigos', methods=['GET'])
def get_postals():
    return jsonify(postals)

@app.route('/cp/api/v1.0/codigos/<codigo>', methods=['GET'])
def get_cp(codigo):
    if codigo not in postals:
        abort(404)
    return jsonify({codigo: postals[codigo]})

if __name__ == '__main__':
    app.run(debug=True)
