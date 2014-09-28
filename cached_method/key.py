# coding: utf-8
from __future__ import absolute_import, unicode_literals

import hashlib


def gen(obj, method, *args, **kwargs):
    name = obj.__name__ if hasattr(obj, "__name__") else id(obj)

    key = "{}:{}:{}:{}:{}".format(
        obj.__module__,
        name,
        method.__name__,
        "".join(args),
        "".join(["{}{}".format(k, v) for k, v in kwargs.iteritems()]),
    )

    key = hashlib.md5(key).hexdigest()
    return key
