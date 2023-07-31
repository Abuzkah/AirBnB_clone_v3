#!/usr/bin/python3
"""module for index route"""

from api.v1.views import app_views
from flask import jsonify
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """index route"""
    status = {"status": "OK"}
    return jsonify(status), 200


@app_views.route('/stats', methods=['GET'])
def stats():
    """index route"""
    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)}), 200
