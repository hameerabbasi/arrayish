import functools
import numbers
import collections

import numpy as np
import multipledispatch as md

np_namespace = {}

dispatch = functools.partial(md.dispatch, namespace=np_namespace)


@dispatch(object, object)
def dot(x, y, **kwargs):
    return np.dot(x, y, **kwargs)


@dispatch(object, object)
def tensordot(a, b, **kwargs):
    return np.tensordot(a, b, **kwargs)


@dispatch(object)
def where(condition):
    return np.where(condition)


@dispatch(object, object, object)
def where(condition, x, y):
    return np.where(condition, x, y)


@dispatch(object)
def nanmin(a, **kwargs):
    return np.nanmin(a, **kwargs)


@dispatch(object)
def nanmax(a, **kwargs):
    return np.nanmax(a, **kwargs)


@dispatch(object)
def nansum(a, **kwargs):
    return np.nansum(a, **kwargs)


@dispatch(object)
def nanprod(a, **kwargs):
    return np.nanprod(a, **kwargs)


@dispatch(object)
def transpose(a, **kwargs):
    return np.transpose(a, **kwargs)


@dispatch(object, (numbers.Integral, collections.Iterable))
def broadcast_to(array, shape, **kwargs):
    return np.broadcast_to(array, shape, **kwargs)
