# GeolocationApp
Python app to show Places details and directions

This project is based on API First.
That means all project was build based on an API Design strategy.
I used the swagger (2.0) framework as part of this development.

## Requirements

Two APIs:
- An API for a place. - for that I choose python language to create the API.
- A Log API. - for that I prefer to use the Amazon CloudWatch service.

## API Design


I split the development in two pieces.

- First the FrontEnd API.
    To this I wrote the code ./places-v1.yml
- Second the BackEnd API.
    For the second one I wrote the ./app.py code.
 
## Installation

- Google APIs (Place detail and directions)
  - To get started with Google APis, the first step is getting and configuring the [API Key](https://developers.google.com/maps/documentation/javascript/get-api-key).
    ** To the test work properly I hard put mine. This Key must be retrieved dynamically. **
 - Download the Dockerfile:
 
 ```console
$ docker pull thiberiofm/geolocation_app_flask
```

After the download completes, you have to run the image

 ```console
$ docker run -d -p 5000:5000 thiberiofm/geolocation_app_flask
```
 
## Run

After the docker image is running just call the API, where "place_name" value is the local to be searched:
```console
curl -X GET \
  'http://localhost:5000/places/v1/places?place_name=mexico' 
```

# Resources

The Google Cloud Plataform (GCP) APIs:

* [Google Directions API](https://developers.google.com/maps/documentation/directions) - Google Developer portal
* [Google Places Details API](https://developers.google.com/places/web-service/details) - Google Developer portal
* [Google API Key](https://developers.google.com/places/web-service/get-api-key) - Google Developer portal
* [Flask Doc](http://flask.palletsprojects.com/en/1.1.x/) - Flask framework