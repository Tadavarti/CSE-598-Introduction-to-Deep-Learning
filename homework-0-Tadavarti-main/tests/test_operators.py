from hypothesis.strategies import integers, lists
from hypothesis import given

from operators import add, sort


@given(integers(), integers())
def test_add(a, b):
    # Check same as system add
    assert add(a, b) == a + b
    # Check that order doesn't matter
    assert add(a, b) == add(b, a)


@given(lists(integers()))
def test_sort(a):
    sorted_a = sort(a)
    # Check that the sorted list has the same elements
    import collections
    assert collections.Counter(a) == collections.Counter(sorted_a)
    # Check that the sorted list is sorted
    current = float('-inf')
    for elem in sorted_a:
        assert elem >= current
        current = elem
