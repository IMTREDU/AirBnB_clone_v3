#!/usr/bin/python3
"""Flask route that provides JSON status responses"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Endpoint that returns a status message"""
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stats():
    """Endpoint that returns the count of each class type"""
    if request.method == 'GET':
        response = {}
        CLASS_NAMES = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for class_name, plural_name in CLASS_NAMES.items():
            response[plural_name] = storage.count(class_name)
        return jsonify(response)
