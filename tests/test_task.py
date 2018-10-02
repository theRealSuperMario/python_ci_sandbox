"""Test the Task data type."""
from tasks import Task
import pytest


def test_member_access():
    t = Task('do something', 'Brian', True, 12)
    assert (t.summary, t.owner, t.done, t.id) == \
           ('do something', 'Brian', True, 12)


def test_defaults():
    t = Task()
    assert (t.summary, t.owner, t.done, t.id) == \
           (None, None, None, None)


def test_equal():  # id isn't used for equality
    t1 = Task('do something', 'Brian', True, 1)
    t2 = Task('do something', 'Brian', True, 456)
    assert t1 == t2

@pytest.mark.parametrize("another", [
    Task('do something', 'Not Brian', False, 1),
    Task('do something', 'sandy', True, 1),
    Task('just sit', 'Not Brian', True, 1),
], ids=repr)

def test_unequal(another):
    t1 = Task('do something', 'Brian', True, 1)
    assert t1 != another

#parameter stacking

@pytest.mark.parametrize("y", [4, 5, 6])
@pytest.mark.parametrize("x", [1, 2, 3])
def test_foo(x, y):
    pass

def test_to_dict():
    t = Task('do something', 'Brian', True, 1)
    d = t.to_dict()
    expected = {'summary': 'do something',
                'owner': 'Brian', 'done': True, 'id': 1}
    assert expected == d


def test_from_dict():
    expected = Task('do something', 'Brian', True, 12)
    d = {'summary': 'do something',
         'owner': 'Brian', 'done': True, 'id': 12}
    t = Task.from_dict(d)
    assert expected == t
    assert expected.id == t.id
