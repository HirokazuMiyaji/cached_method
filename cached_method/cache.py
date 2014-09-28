# coding: utf-8
from __future__ import absolute_import, unicode_literals

import threading

_cache = threading.local()


class Cache(object):

    def __init__(self, name="data"):
        self.name = name
        setattr(_cache, self.name, {})

    def get(self, key, default=None):
        try:
            return getattr(_cache, self.name)[key]
        except KeyError:
            return default

    def set(self, key, value):
        getattr(_cache, self.name)[key] = value

    def delete(self, key):
        try:
            del getattr(_cache, self.name)[key]
        except:
            pass

    def clear(self):
        setattr(_cache, self.name, {})


cache = Cache()
