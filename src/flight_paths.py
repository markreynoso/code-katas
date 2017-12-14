"""Find path between airports."""
import json
import urllib.request


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles


def find_path_between_cities(city1, city2):
    """Return path and distance between two cities."""
    url = ('https://codefellows.github.io/sea-python-401d6'
           '/_downloads/cities_with_airports.json')
    jsonurl = urllib.request.urlopen(url)
    data_list = json.loads(jsonurl.read().decode())
    data = {}
    for city in data_list:
        data.setdefault(city['city'], city)
    stack = [city1]
    connections = {}
    distances = {city1: 0}
    while stack:
        route = stack.pop(0)
        try:
            lat_lon1 = data[route]['lat_lon']
            for city in data[route]['destination_cities']:
                stack.append(city)
                # for location in data:
                lat_lon2 = data[city]['lat_lon']
                distance = calculate_distance(lat_lon1, lat_lon2)\
                    + distances[route]
                if city not in distances or distances[city] > distance:
                    distances[city] = distance
                    connections[city] = route
                if city == city2:
                    current = city
                    path = [city1]
                    while current != city1:
                        path.insert(1, current)
                        current = connections[current]
                    return path, distances[city2]
        except KeyError:
            continue
    return 'There is no path between these cities'
