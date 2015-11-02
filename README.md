# Twitter-API

Libraries used:
-geolocation-python 0.2.0 (https://pypi.python.org/pypi/geolocation-python/0.2.0)
-tweepy (https://github.com/tweepy/tweepy)

APIs used:
-Twitter API (https://dev.twitter.com/overview/documentation)
-Google Maps API (https://developers.google.com/maps/)

A python program that retrieves live streaming tweets about the top trending keyword for a given place. The coordinates for the entered place are found using 'geolocation-python' library which is based on the Google Maps Geocoding API. These coordinates are then fed to the Twitter API using 'Tweepy' as an interface. Data returned by both APIs is in JSON format. Useful information is then extracted from this data and stored to a file.

