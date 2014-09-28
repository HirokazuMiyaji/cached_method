# coding: utf-8
from __future__ import absolute_import, unicode_literals

from .cache import Cache
from .key import gen

_cache = Cache("request")


try:
    from django.core import signals

    def _init(sender, **kwargs):
        _cache.clear()

    def _clear(sender, **kwargs):
        _cache.clear()

    signals.request_started.connect(_init)
    signals.request_finished.connect(_clear)
except ImportError:
    pass


def cached_method_per_request(method):
    def decorator(obj, *args, **kwargs):
        key = gen(obj, method, *args, **kwargs)
        result = _cache.get(key)
        if not result:
            result = method(obj, *args, **kwargs)
            if result:
                _cache.set(key, result)
        return result
    return decrator


def delete_cache_per_request(obj, method, *args, **kwargs):
    key = gen(obj, method, *args, **kwargs)
    _cache.delete(key)
