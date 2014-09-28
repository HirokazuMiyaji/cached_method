# coding: utf-8
from __future__ import absolute_import, unicode_literals

from .key import gen

try:
    from django.core.cache import cache
except:
    from .cache import cache


def cached_method(method):
    def decorator(obj, *args, **kwargs):
        key = gen(obj, method, *args, **kwargs)
        result = cache.get(key)
        if not result:
            result = method(obj, *args, **kwargs)
            if result:
                cache.set(key, result)
        return result
    return decorator


def delete_cache(obj, method, *args, **kwargs):
    key = gen(obj, method, *args, **kwargs)
    cache.delete(key)
