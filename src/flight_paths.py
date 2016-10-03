import math
from simple_graph import SimpleGraph

def make_points(json):
    """Make a dictionary of city lat_lon pairings."""
    cities = {}
    for info in json:
        cities[info['city']] = info['lat_lon']
    return cities


def convert_to_radians(degrees):
    return degrees * math.pi / 180


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """

    radius_earth = 6.371E3
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles


def make_graph(json, cities_dict):
    """Make a graph of the cities."""
    city_graph = SimpleGraph()
    for info in json:
        for dest in info['destination_cities']:
            city1 = cities_dict[info['city']]
            city2 = cities_dict[dest]
            dist = calculate_distance(city1, city2)
            city_graph.add_edge(info['city'], dest, dist)
    return city_graph

def get_shortest_connection(graph, city1, city2):
    """Test the shortest path for two given cities."""
    shortest_path_dict = graph.shortest_path(city1)
    distance = shortest_path_dict[0][city2]
    path = shortest_path_dict[1][city2]
    return distance, path