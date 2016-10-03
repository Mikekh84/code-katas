def test_auto_complete_empty():
    """Test auto complete on empty."""
    from autocomplete import AutoCompleter
    lst = []
    test_auto = AutoCompleter(lst)
    assert test_auto('f') == []

def test_auto_complete_single():
    """Test auto complete with singele."""
    from autocomplete import AutoCompleter
    lst = ['final', 'geo', 'something']
    test_auto = AutoCompleter(lst)
    assert test_auto('f') == ['final']

def test_auto_compete_max_iter():
    """Test auto with a small max."""
    from autocomplete import AutoCompleter
    lst = ['final', 'fox', 'figment', 'foo', 'Fellows']
    test_auto = AutoCompleter(lst, max_completions=2)
    assert len(test_auto('f')) == 2

def test_auto_compete_no_viable():
    """Test auto with a small max."""
    from autocomplete import AutoCompleter
    lst = ['final', 'fox', 'figment', 'foo', 'Fellows']
    test_auto = AutoCompleter(lst, max_completions=2)
    assert test_auto('g') == []