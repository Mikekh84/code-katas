def test_sort_cards():
    """Intial test of cards."""
    from cards import sort_cards
    assert sort_cards(["A",'5','8','9','3',"J","T"]) == ["A", '3', '5', '8', '9', "T", "J"]


def test_kata_code1():
    """Test kata test 1."""
    from cards import sort_cards
    result = list('A23456789TJQK')
    assert sort_cards(list('39A5T824Q7J6K')) == result


def test_kata_code2():
    """Test kata test 2."""
    from cards import sort_cards
    result = list('A23456789TJQK')
    assert sort_cards(list('Q286JK395A47T')) == result


def test_kata_code3():
    """Test kata test 3."""
    from cards import sort_cards
    result = list('A23456789TJQK')
    assert sort_cards(list('54TQKJ69327A8')) == result
