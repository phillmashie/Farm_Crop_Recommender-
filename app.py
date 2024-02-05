# app.py
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)  # Enable CORS for all routes

# Sample data (replace with database integration)
user_profiles = {}
recommendations = {}
weather_data = {}

class UserProfileResource(Resource):
    def get(self, user_id):
        return jsonify(user_profiles.get(user_id, {}))

    def post(self, user_id):
        data = request.get_json()
        user_profiles[user_id] = data
        return jsonify(message="User profile updated successfully.")

class RecommendedCropsResource(Resource):
    def get(self, user_id):
        return jsonify(recommendations.get(user_id, []))

class WeatherDataResource(Resource):
    def get(self, location):
        return jsonify(weather_data.get(location, {}))

api.add_resource(UserProfileResource, '/api/user/profile/<string:user_id>')
api.add_resource(RecommendedCropsResource, '/api/crops/recommended/<string:user_id>')
api.add_resource(WeatherDataResource, '/api/environment/weather/<string:location>')

if __name__ == '__main__':
    app.run(debug=True)
