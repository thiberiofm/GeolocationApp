import requests
from flask import Flask, jsonify, make_response, request

from key import key

app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"


@app.errorhandler(404)
def not_found(error):
    """ Function to Not Found response """
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route("/places/v1/places", methods=['GET'])
def list_places():
    """
       Function to receive the places infos to search at Googlemaps.
       """
    {
        "timestamp": "2018-08-20T15:00:00Z",
        "error_code": "Z001",
        "message": "Required fields",
        "details": [
            "field_one",
            "field_two"
        ]
    }
    if not (len(request.args) > 0 ) or (key == "key"):
        return make_response(jsonify({'timestamp': '2018-08-20T15:00:00', 'error_code':'ABC-System Lorem', 'message' : 'You shall not pass', 'details':[
            'field_one',
        'field_two']
        }), 400)

    query_parameters = request.args
    place_name = query_parameters.get('place_name')

    query = place_name

    search_payload = {"key": key, "query": query}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    google_response_place_id = search_json["results"][0]["place_id"]
    google_response_place_name = search_json["results"][0]["name"]

    details_payload = {"key": key, "placeid": google_response_place_id}
    details_resp = requests.get(details_url, params=details_payload)
    details_json = details_resp.json()

    google_response_formatted_address = details_json["result"]["formatted_address"]
    google_response_geometry_location_lat = details_json["result"]["geometry"]["location"]["lat"]
    google_response_geometry_location_lng = details_json["result"]["geometry"]["location"]["lng"]
    """
Mocking the distance API due time to complete
       """
    google_response_routes_travel_mode = "driving"
    google_response_routes_distance_text = "39km"
    google_response_routes_distance_value = 3900
    google_response_routes_duration_text = "51 mins"
    google_response_routes_duration_value = 3062
    google_response_routes_end_address = "Guarulhos"
    google_response_routes_end_location_lat = 34.1330949
    google_response_routes_end_location_lng = 34.1330949
    google_response_routes_start_address = "Osasco"
    google_response_routes_start_location_lat = 34.1330949
    google_response_routes_start_location_lng = 34.1330949

    return jsonify({
        "data": [
            {"place_id": google_response_place_id,
             "place_name": google_response_place_name,
             "place_details": {
                 "formatted_address": google_response_formatted_address,
                 "formatted_phone_number": google_response_formatted_address,
                 "geometry": {
                     "location": {
                         "lat": google_response_geometry_location_lat,
                         "lng": google_response_geometry_location_lng
                     }
                 }

             },
             "routes": [{
                 "travel_mode": google_response_routes_travel_mode,
                 "distance": {
                     "text": google_response_routes_distance_text,
                     "value": google_response_routes_distance_value
                 },
                 "duration": {
                     "text": google_response_routes_duration_text,
                     "value": google_response_routes_duration_value

                 },
                 "end_address": google_response_routes_end_address,
                 "end_location": {
                     "lat": google_response_routes_end_location_lat,
                     "lng": google_response_routes_end_location_lng
                 },
                 "start_address": google_response_routes_start_address,
                 "start_location": {
                     "lat": google_response_routes_start_location_lat,
                     "lng": google_response_routes_start_location_lng
                 }

             }
             ]
             }
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
