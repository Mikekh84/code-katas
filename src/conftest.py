import pytest


@pytest.fixture()
def good_parens():
    """Return a good string."""
    return u"((something))"


@pytest.fixture()
def bad_open():
    """Return an open string."""
    return u"(something bad"


@pytest.fixture()
def bad_broken():
    """Return a broken string."""
    return u"something this is not good)"
