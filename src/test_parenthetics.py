import pytest

TEST_PAREN = [
    ("(spme(oth)ing)", 0),
    ("has() and openeing)", -1),
    ("(absd) (slk) slkjf(fsj", 1),
    (")))(((", -1),
    ("1(2(12(3(sldkjfls)asd)aasda)asd)", 0),
    ("(", 1),
    (")", -1),
    ("()", 0),
    ("))", -1),
    ("((", 1),
    ("no parents", 0),
    ("(slkdjfs)sldj)fskj(skjdf)", -1)
]


def test_paren_good(good_parens):
    """Test Parenthetics is balanced."""
    from parenthetics import parens
    assert parens(good_parens) == 0


def test_paren_open(bad_open):
    """Test parenthetics is open."""
    from parenthetics import parens
    assert parens(bad_open) == 1


def test_paren_broken(bad_broken):
    """Test parenthetics is broken."""
    from parenthetics import parens
    assert parens(bad_broken) == -1


@pytest.mark.parametrize("string, result", TEST_PAREN)
def test_paren_param(string, result):
    """Test with parametrize."""
    from parenthetics import parens
    assert parens(string) == result
