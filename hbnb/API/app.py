from config import app, db, jwt
from service.amenity_service import AmenityService
from service.place_service import PlaceService
from service.user_service import UserService
from service.country_service import CountryService
from service.city_service import CityService
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

def is_admin():
    claims = get_jwt()
    return claims.get('is_admin', False)

@app.route('/user', methods=["GET"])
def user():
    users = UserService.get_all_user()
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)

@app.route('/user', methods=['POST'])
@jwt_required()
def create_user():
    if not is_admin():
        return jsonify({"msg": "Only administrators can create users"})
    data = request.get_json()
    new_user = UserService.create_user(data['email'], data['first_name'],
                                        data['last_name'],
                                        data['password'],
                                        data['is_admin'])
    return jsonify(new_user.to_dict())

@app.route('/user/<user_id>', methods=["GET"])
def manage_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user: 
        return jsonify(user.to_dict())
    return jsonify({"error": "User Not Found"}), 404

@app.route('/user/<user_id>', methods=["PUT"])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()
    
    if not user:
        return jsonify({"error": "User Not Found"}), 404

    if user_id != current_user and not is_admin():
        return jsonify({"msg": "You are not authorize to change this user"})

    data = request.get_json()
    update_user = UserService.update_user(user_id, 
                                            data.get('email'),
                                            data.get('first_name'),
                                            data.get('last_name'))
    if update_user:
        return jsonify(update_user.to_dict())

@app.route('/user/<user_id>', methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()

    if not user:
        return jsonify({"error": "User Not Found"}), 404

    if user_id != current_user and not is_admin():
        return jsonify({"msg": "You are not authorize to delete this user"})

    succes = UserService.delete_user(user_id)
    if succes:
        return jsonify({"message": "User delete successfully"})


@app.route('/countries', methods=["GET"])
def countries():
    countries = CountryService.get_all_countries()
    countries_dict = [country.to_dict() for country in countries]
    return jsonify(countries_dict)

@app.route('/countries', methods=["POST"])
def create_countries():
    data = request.get_json()
    new_country = CountryService.create_country(data['name'],
                                                data['code'])
    return jsonify({"code": new_country.code,
                    "name": new_country.name})
@app.route('/countries/<code>', methods=["GET"])
def manage_country(code):
    country = CountryService.get_country_by_code(code)
    if country:
        return jsonify(country.to_dict())
    return jsonify({"error": "Country Not Found"}), 404

@app.route('/countries/<countries_id>', methods=["PUT"])
def update_countries(countries_id):
    data = request.get_json()
    updated_country = CountryService.update_country(code, data.get('name',
                                                        data.get('code')))
    if updated_country:
            return jsonify(updated_country.to_dict())
    return jsonify({"error": "Country Not Found"}), 404

@app.route('/countries/<countries_id>', methods=["DELETE"])
def delete_country(countries_id):
    success = CountryService.delete_country(code)
    if success:
        return jsonify({"message": "Country delete succesfully"})
    return jsonify({"error": "Country Not Found"}), 404

@app.route('/cities', methods=["GET"])
def cities():
    cities = CityService.get_all_cities()
    cities_dict = [city.to_dict() for city in cities]
    return jsonify(cities_dict)

@app.route('/cities', methods=["POST"])
def create_city():
    data = request.get_json()
    new_city = CityService.create_city(data['name'], data['country_code'])
    return jsonify(new_city.to_dict())

@app.route('/cities/<city_id>', methods=["GET"])
def manage_city(city_id):
    city = CityService.get_city_by_id(city_id)
    if city:
        return jsonify(city.to_ditc())
    return jsonify({"error": "City Not Found"}), 404
@app.route('/cities/<city_id>', methods=["PUT"])
def update_city(city_id):
    data = request.get_json()
    updated_city = CityService.update_city(city_id,
                                            data.get('name'),
                                            data.get('country_code'))
    if updated_city:
        return jsonify(updated_city.to_dict())
    return jsonify({"error": "City Not Found"}), 404
@app.route('/cities/<city_id>', methods=["DELETE"])
def delete_city(city_id):
    success = CityService.delete_city(city_id)
    if success:
        return jsonify({"message": "City delete successfully"})
    return jsonify({"error": "City Not Found"}), 404

@app.route('/places', methods=["GET"])
def place():
    places = PlaceService.get_all_place()
    place_dict = [place.to_dict() for place in places]
    return jsonify(place_dict)

@app.route('/places', methods=["POST"])
def create_place():
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

@app.route('/places/<place_id>', methods=["GET"])
def manage_place(place_id):
    place = PlaceService.get_place_by_id(place_id)
    if place:
        return jsonify(place.to_dict())
    return jsonify({"error": "Place Not Found"}), 404

@app.route('/places/<place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    current_user = get_jwt_identity()
    place = PlaceService.get_place_by_id(place_id)

    if not place:
        return jsonify({"error": "Place Not Found"}), 404
    if place.host_id != current_user and not is_admin():
        return jsonify({"message": "You are not authorize to update this place"})

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

@app.route('/places/<place_id>', methods=['DELETE'])
@jwt_required()
def delete_place(place_id):
    current_user = get_jwt_identity()
    place = PlaceService.get_place_by_id(place_id)

    if not place:
        return jsonify({"error": "Place Not Found"}), 404
    if place.host_id != current_user and not is_admin():
        return jsonify({"message": "You are not authorize to delete this place"})
    success = PlaceService.delete_place(place_id)
    if success:
        return jsonify({"message": "Place delete successfully"})

@app.route('/amenities', methods=["GET"])
def amenity():
    amenities = AmenityService.get_all_amenity()
    a_dict = [a.to_dict() for a in amenities]
    return jsonify(a_dict)
@app.route('/amenities', methods=['POST'])
def create_amenities():
    data = request.get_json()
    new_a = AmenityService.create_amenity(data['name'])
    return jsonify(new_a.to_dict())

@app.route('/amenities/<amenity_id>', methods=["GET"])
def manage_amenity(amenity_id):
    a = AmenityService.get_amenity_by_id(amenity_id)
    if a:
        return jsonify(a.to_dict())
    return jsonify({"error": "Amenity Not Found"}), 404

@app.route('/amenities/<amenity_id>', methods=["PUT"])
def update_amenity(amenity_id):
    data = request.get_json()
    updated_a = AmenityService.update_amenity(amenity_id, data.get('name'))
    return jsonify(updated_a.to_dict())

@app.route('/amenities/<amenity_id>', methods=["DELETE"])
def delete_amenity(amenity_id):
    success = AmenityService.delete_amenity(amenity_id)
    if success:
        return jsonify({"message": "Amenity delte successfully"})
    return jsonify({"error": "Amenity Not Found"}), 404

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    user = UserService.filter_user_by_email(email)
    user.set_password(password)
    if user and user.check_password(password):
        additional_claims = {"is_admin": user.is_admin}
        access_token = create_access_token(identity=email,\
                additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "User Not match"}), 401

@app.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/admin/data', methods=['POST', 'DELETE'])
@jwt_required()
def admin_data():
    claims = get_jwt()
    if  not claims.get('is_admin'):
        return jsonify({"message": "Administration rights required"})
    return jsonify({"message": "Eres un KatangaMaster"})



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
