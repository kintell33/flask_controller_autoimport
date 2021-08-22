from __main__ import app
from decorators.api_base import api
from flask import jsonify

print("controller_base imported")

@app.route('/api/health', methods=['GET'])
@api.exception
def index():
    return jsonify({"status": "OK"}), 200
