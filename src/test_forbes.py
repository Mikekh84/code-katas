FAKE_LIST = [
        {
        "name": "Person A",
        "age": 82,
        "rank": 22,
        "net_worth (USD)": 10,
        "source": "oils",
        "country": "United States"
    },
        {
        "name": "Person B",
        "age": 79,
        "rank": 22,
        "net_worth (USD)": 11,
        "source": "tech",
        "country": "United States"
    },
        {
        "name": "Person C",
        "age": 60,
        "rank": 22,
        "net_worth (USD)": 13,
        "source": "cows",
        "country": "United States"
    },
]


RESULT = 'Oldest: Person B, 11, tech || Youngest: Person C, 13, cows'

def test_get_oldest_youngest():
    from forbes import get_oldest_youngest
    assert get_oldest_youngest(FAKE_LIST) == RESULT