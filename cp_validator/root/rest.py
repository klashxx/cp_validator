#!flask/bin/python
"""
RESTful API
"""
from flask import Flask, jsonify
from cp_validator.root.extractor import get_postal

postals = get_postal()

app = Flask(__name__)

@app.route('/cp/api/v1.0/codigos', methods=['GET'])
def get_tasks():
    return jsonify(postals)

if __name__ == '__main__':
    app.run(debug=True)
