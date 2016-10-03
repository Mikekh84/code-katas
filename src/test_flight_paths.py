FAKE_JSON = [

    {
        u'airport': u'Goma International Airport',
        u'city': u'Goma',
        u'connection_urls': [u'https://en.wikipedia.org/wiki/Kindu_Airport',
        u'https://en.wikipedia.org/wiki/Bangoka_International_Airport',
        u'https://en.wikipedia.org/wiki/N%27djili_Airport',
        u'https://en.wikipedia.org/wiki/Addis_Ababa_Bole_International_Airport'],
        u'country': u'Democratic Republic of the Congo',
        u'destination_airports': [u"N'djili Airport",
        u'Bangoka International Airport',
        u'Addis Ababa Bole International Airport'],
        # u'destination_cities': [u'Kinshasa', u'Kisangani', u'Addis Ababa'],
        u'destination_cities': ['Kisangani'],
        # u'lat_lon': [-1.669889, 29.238278],
        u'lat_lon': [0, 0],
        u'url': u'https://en.wikipedia.org/wiki/Goma_International_Airport'
    },
    {
        u'airport': u'Bangoka International Airport',
        u'city': u'Kisangani',
        u'connection_urls': [u'https://en.wikipedia.org/wiki/Goma_International_Airport',
        u'https://en.wikipedia.org/wiki/Kindu_Airport',
        u'https://en.wikipedia.org/wiki/N%27djili_Airport'],
        u'country': u'Democratic Republic of the Congo',
        u'destination_airports': [u'Goma International Airport', u"N'djili Airport"],
        u'destination_cities': [u'Goma'],
        # u'lat_lon': [0.48167, 25.33806],
        u'lat_lon': [0, 0],
        u'url': u'https://en.wikipedia.org/wiki/Bangoka_International_Airport'
    },
]

CITIES = {
    'Goma': [0, 0],
    'Kisangani': [0, 0],
}


def test_make_points():
    """Make a diction of cities and lat lons."""
    from flight_paths import make_points
    cities = make_points(FAKE_JSON)
    assert cities['Goma'] == [0, 0]


def test_make_graph():
    """Test make a graph from JSON."""
    from flight_paths import make_graph
    graph = make_graph(FAKE_JSON, CITIES)
    assert graph.neighbors('Goma') == ['Kisangani']

def test_get_shortest_connection():
    """Test getting shortest connection."""
    from flight_paths import get_shortest_connection, make_graph
    graph = make_graph(FAKE_JSON, CITIES)
    assert get_shortest_connection(graph, 'Goma', 'Kisangani') == (0.0, ['Goma'])