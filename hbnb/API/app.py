import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb/service")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb")
from config import app, db
from amenity_service import AmenityService
from place_service import PlaceService
from user_service import UserService
from country_service import CountryService
from city_service import CityService
from flask import request, jsonify
@app.route('/user', methods=["GET", "POST"])
def user():
    if request.method == "GET":
        users = UserService.get_all_user()
        users_dict = [user.to_dict() for user in users]
        return jsonify(users_dict)
    if request.method == "POST":
        data = request.get_json()
        new_user = UserService.create_user(data['email'], data['first_name'],
                                           data['last_name'])
        return jsonify({"id": new_user.id, "email": new_user.email,
                       "first_name": new_user.first_name,
                       "last_name": new_user.last_name})
@app.route('/user/<user_id>', methods=["GET", "PUT", "DELETE"])
def manage_user(user_id):
    if request.method == "GET":
        user = UserService.get_user_by_id(user_id)
        if user: 
            return jsonify(user.to_dict())
        return jsonify({"error": "User Not Found"}), 404
    elif request.method == "PUT":
        data = request.get_json()
        update_user = UserService.update_user(user_id, 
                                              data.get('email'),
                                              data.get('first_name'),
                                              data.get('last_name'))
        if update_user:
            return jsonify(update_user.to_dict())
        return jsonify({"error": "User Not Found"}), 404
    
    elif request.method == "DELETE":
        succes = UserService.delete_user(user_id)
        if succes:
            return jsonify({"message": "User delete successfully"})
        return jsonify({"error": "User Not Found"}), 404



@app.route('/countries', methods=["GET", "POST"])
def countries():
    if request.method == "GET":
        countries = CountryService.get_all_countries()
        countries_dict = [country.to_dict() for country in countries]
        return jsonify(countries_dict)
    if request.method == "POST":
        data = request.get_json()
        new_country = CountryService.create_country(data['name'],
                                                    data['code'])
        return jsonify({"code": new_country.code,
                        "name": new_country.name})
@app.route('/countries/<code>', methods=["GET", "PUT", "DELETE"])
def manage_country(code):
    if request.method == "GET":
        country = CountryService.get_country_by_code(code)
        if country:
            return jsonify(country.to_dict())
        return jsonify({"error": "Country Not Found"}), 404

    elif request.method == "PUT":
        data = request.get_json()
        updated_country = CountryService.update_country(code, data.get('name',
                                                            data.get('code')))
        if updated_country:
            return jsonify(updated_country.to_dict())
        return jsonify({"error": "Country Not Found"}), 404

    elif request.method == "DELETE":
        success = CountryService.delete_country(code)
        if success:
            return jsonify({"message": "Country delete succesfully"})
        return jsonify({"error": "Country Not Found"}), 404

@app.route('/cities', methods=["GET", "POST"])
def cities():
    if request.method == "GET":
        cities = CityService.get_all_cities()
        cities_dict = [city.to_dict() for city in cities]
        return jsonify(cities_dict)
    if request.method == "POST":
        data = request.get_json()
        new_city = CityService.create_city(data['name'], data['country_code'])
        return jsonify(new_city.to_dict())
@app.route('/cities/<city_id>', methods=["GET", "PUT", "DELETE"])
def manage_city(city_id):
    if request.method == "GET":
        city = CityService.get_city_by_id(city_id)
        if city:
            return jsonify(city.to_ditc())
        return jsonify({"error": "City Not Found"}), 404
    elif request.method == "PUT":
        data = request.get_json()
        updated_city = CityService.update_city(city_id,
                                               data.get('name'),
                                               data.get('country_code'))
        if updated_city:
            return jsonify(updated_city.to_dict())
        return jsonify({"error": "City Not Found"}), 404
    elif request.method == "DELETE":
        success = CityService.delete_city(city_id)
        if success:
            return jsonify({"message": "City delete successfully"})
        return jsonify({"error": "City Not Found"}), 404

@app.route('/places', methods=["GET", "POST"])
def place():
    if request.method == "GET":
        places = PlaceService.get_all_place()
        place_dict = [place.to_dict() for place in places]
        return jsonify(place_dict)
    if request.method == "POST":
        data = request.get_json()
        new_place = PlaceService.create_place(data['name'],
                                              data['description'],
                                              data['number_of_rooms'],
                                              data['number_of_bathrooms'],
                                              data['max_guest'],
                                              data['price_per_night'],
                                              data['latitude'],
                                              data['longitude'],
                                              data['host_id'],
                                              data['city_id'])
        return jsonify(new_place.to_dict())
@app.route('/places/<place_id>', methods=["GET", "PUT", "DELETE"])
def manage_place(place_id):
    if request.method == "GET":
        place = PlaceService.get_place_by_id(place_id)
        if place:
            return jsonify(place.to_dict())
        return jsonify({"error": "Place Not Found"}), 404
    elif request.method == "PUT":
        data = request.get_json()
        updated_place = PlaceService.update_place(place_id,
                                            data.get('name'),
                                            data.get('description'),
                                            data.get('number_of_rooms'),
                                            data.get('number_of_bathrooms'),
                                            data.get('max_guest'),
                                            data.get('price_per_night'),
                                            data.get('latitude'),
                                            data.get('longitude'),
                                            data.get('host_id'),
                                            data.get('city_id'))
        if updated_place:
            return jsonify(updated_place.to_dict())
        return jsonify({"error": "Place Not Found"}), 404
    elif request.method == "DELETE":
        success = PlaceService.delete_place(place_id)
        if success:
            return jsonify({"message": "Place delete successfully"})
        return jsonify({"error": "Place Not Found"}), 404
@app.route('/amenities', methods=["GET", "POST"])
def amenity():
    if request.method == "GET":
        amenities = AmenityService.get_all_amenity()
        a_dict = [a.to_dict() for a in amenities]
        return jsonify(a_dict)
    if request.method == "POST":
        data = request.get_json()
        new_a = AmenityService.create_amenity(data['name'])
        return jsonify(new_a.to_dict())

@app.route('/amenities/<amenity_id>', methods=["GET", "PUT", "DELETE"])
def manage_amenity(amenity_id):
    if request.method == "GET":
        a = AmenityService.get_amenity_by_id(amenity_id)
        if a:
            return jsonify(a.to_dict())
        return jsonify({"error": "Amenity Not Found"}), 404
    elif request.method == "PUT":
        data = request.get_json()
        updated_a = AmenityService.update_amenity(amenity_id, data.get('name'))
        return jsonify(updated_a.to_dict())
    elif request.method == "DELETE":
        success = AmenityService.delete_amenity(amenity_id)
        if success:
            return jsonify({"message": "Amenity delte successfully"})
        return jsonify({"error": "Amenity Not Found"}), 404



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
