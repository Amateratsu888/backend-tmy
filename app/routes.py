"""This module will serve the api request."""

from app.tmyValidator import SchemaValidator
from flask import Flask, Response, request, jsonify
from app.dictToYml import dict_to_yaml_and_upload
from config import client
from bson.json_util import dumps
from bson.objectid import ObjectId
from app import app
from os import environ
from flask_cors import CORS, cross_origin




# Select the database
db = client.tmyDB
# Select the collection
tmyModel = db.tmyCollection

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Create a tmy
@app.route('/api/tmy', methods=['POST'])
def create_tmy():
    try:
        tmy_data = request.json
        # Implement validation for tmy_data here
        _instance  = SchemaValidator(response=tmy_data)
        response = _instance.isTrue()
        if len(response) > 0:
            _ = {
                    "status":"error",
                    "message":response
                },403
            return _
        dict_to_yaml_and_upload(tmy_data,tmy_data['project_name'],environ.get("S3_BUCKET_NAME"),"tmy-files/")
        

        # Insert the tmy document into the collection
        result = tmyModel.insert_one(tmy_data)
        return jsonify({"message": "TMY created successfully", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"error": str(e)})

# Get all tmy
@app.route('/api/tmy', methods=['GET'])
@cross_origin()
def get_all_tmy():
    try:
        tmy_list = list(tmyModel.find())
        return Response(response=dumps(tmy_list), status=200, mimetype="application/json")
    except Exception as e:
        return jsonify({"error": str(e)})

# Find one tmy by ID
@app.route('/api/tmy/<string:tmy_id>', methods=['GET'])
def get_tmy_by_id(tmy_id):
    try:
        tmy = tmyModel.find_one({"_id": ObjectId(tmy_id)})
        if tmy:
            return Response(response=dumps(tmy), status=200, mimetype="application/json")
        else:
            return jsonify({"message": "TMY not found"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Update one tmy by ID
@app.route('/api/tmy/<string:tmy_id>', methods=['PUT'])
def update_tmy_by_id(tmy_id):
    try:
        tmy_data = request.json

        result = tmyModel.update_one({"_id": ObjectId(tmy_id)}, {"$set": tmy_data})
        if result.modified_count > 0:
            return jsonify({"message": "TMY updated successfully"})
        else:
            return jsonify({"message": "TMY not found"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Delete one tmy by ID
@app.route('/api/tmy/<string:tmy_id>', methods=['DELETE'])
def delete_tmy_by_id(tmy_id):
    try:
        result = tmyModel.delete_one({"_id": ObjectId(tmy_id)})
        if result.deleted_count > 0:
            return jsonify({"message": "TMY deleted successfully"})
        else:
            return jsonify({"message": "TMY not found"})
    except Exception as e:
        return jsonify({"error": str(e)})
