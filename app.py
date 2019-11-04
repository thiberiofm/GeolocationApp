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

    if not len(request.args) > 0:
        return make_response(jsonify({'error': 'Bad Request'}), 400)

    query_parameters = request.args
    place_name = query_parameters.get('place_name')

    query = place_name

    search_payload = {"key":key, "query":query}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    place_id = search_json["results"][0]["place_id"]

    details_payload = {"key":key, "placeid":place_id}
    details_resp = requests.get(details_url, params=details_payload)
    details_json = details_resp.json()

    url = details_json["result"]["url"]
    return jsonify({'data':{ 'url' : url }})

if __name__ == "__main__":
    app.run(debug=True)
