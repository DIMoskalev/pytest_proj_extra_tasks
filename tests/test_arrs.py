import pytest

from utils import arrs

ARRAY = [1, 2, 3, 4]
@pytest.fixture
def list_test():
    return ARRAY

def test_get(list_test):
    assert arrs.get(list_test, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(list_test):
    assert arrs.my_slice(list_test, 1, 3) == [2, 3]
    assert arrs.my_slice(list_test, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(list_test) == [1, 2, 3, 4]
