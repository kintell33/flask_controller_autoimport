from __main__ import app
from decorators.api_base import api
from flask import jsonify

print("controller_test imported")

@app.route('/api/test', methods=['GET'])
@api.exception
def test():
    return jsonify({"status": "OK 2"}), 200
