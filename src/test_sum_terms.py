def test_series_sum_0():
    """Test Series sum with 0."""
    from sum_terms import series_sum
    assert series_sum(0) == '0.00'


def test_series_sum_1():
    """Test sum_series with 1."""
    from sum_terms import series_sum
    assert series_sum(1) == '1.00'


def test_series_sum_3():
    """Test sum series with 3."""
    from sum_terms import series_sum
    assert series_sum(3) == '1.39'


def test_series_sum6():
    """Test sum_series with 6."""
    from sum_terms import series_sum
    assert series_sum(6) == '1.63'


def test_series_sum10():
    """Test sum series with 10."""
    from sum_terms import series_sum
    assert series_sum(10) == '1.81'
