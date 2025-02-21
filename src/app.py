"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


# create the jackson family object
jackson_family = FamilyStructure('Jackson')


jackson_family.add_member({
    'name': 'William',
    'age': 17,
    'lucky_number': [3,6,9]
})
jackson_family.add_member({
    'name': 'John',
    'age': 33,
    'lucky_number': [7, 13, 22]
})
jackson_family.add_member({
    'name': 'Jane',
    'age': 35,
    'lucky_number': [10, 14, 3]
})
jackson_family.add_member({
    'name': 'Jimmy',
    'age': 5,
    'lucky_number': [1]
})


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "los_jackson": members,
    }
    return jsonify(response_body), 200



@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    # this is how you can use the Family datastructure by calling its methods
   
    response = jackson_family.delete_member(id)
    return jsonify(response), 200



@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    # this is how you can use the Family datastructure by calling its methods
   
    response = jackson_family.get_member(id)
    return jsonify(response), 200



@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    if 'name' not in data or 'age' not in data or 'lucky_number' not in data:
        return jsonify({"msg": "No encontramos todos los datos"}), 400
    response = jackson_family.add_member(data)
    return jsonify({'msg': response})


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
