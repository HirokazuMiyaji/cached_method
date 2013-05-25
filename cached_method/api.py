# coding: utf-8

import hashlib
try:
    from django.core.cache import cache
except:
    from .cache import cache


def _create_key(obj, method, *args, **kwargs):
    obj_name = ''
    if hasattr(obj, '__name__'):
        # cls
        obj_name = obj.__name__
    else:
        # instance
        obj_name = id(obj)
    key = '{}:{}:{}:{}:{}'.format(obj.__module__,
                                  obj_name,
                                  method.__name__,
                                  str(args),
                                  str(kwargs))
    key = hashlib.md5(key).hexdigest()
    return key


def cached_method(method):
    def decorator(obj, *args, **kwargs):
        key = _create_key(obj, method, *args, **kwargs)
        result = cache.get(key, None)
        if not result:
            result = method(obj, *args, **kwargs)
            if result:
                cache.set(key, result)
        return result
    return decorator


def delete_cache(obj, method, *args, **kwargs):
    key = _create_key(obj, method, *args, **kwargs)
    cache.delete(key) 
