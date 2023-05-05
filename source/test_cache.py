import pytest
from cache import LRUCache


def test_LRUCache():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    assert cache.get('Jesse') == 'James'
    cache.rem('Walter')
    assert cache.get('Walter') == ''
