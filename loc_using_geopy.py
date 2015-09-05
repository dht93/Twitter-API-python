from geopy.geocoders import Nominatim

def coordinates(address):
    geolocator=Nominatim()
    location=geolocator.geocode(address)
    coord=[]
    coord.append(round(location.latitude,2))
    coord.append(round(location.longitude,2))
    return coord
