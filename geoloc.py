from geolocation.google_maps import GoogleMaps

key='your_google_maps_api_key'  #enter your google maps api key
def coordinates(address):
    coord=[]
    google_maps=GoogleMaps(api_key=key)
    location=google_maps.search(location=address)
    my_location=location.first()
    coord.append(my_location.lat)
    coord.append(my_location.lng)
    return coord
