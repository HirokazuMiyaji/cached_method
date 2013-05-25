# coding: utf-8

import threading

_cache = threading.local()
_cache.container = {}

class cache(object):
    @classmethod
    def get(cls, key, *args):
        try:
            return _cache.container[key]
        except:
            if args:
                return args[0]
            raise

    @classmethod
    def set(cls, key, value):
        _cache.container[key] = value

    @classmethod
    def delete(cls, key):
        del _cache.container[key]
