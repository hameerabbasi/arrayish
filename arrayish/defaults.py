import functools
import numbers

import numpy as np
import multipledispatch as md

np_namespace = {}

dispatch = functools.partial(md.dispatch, namespace=np_namespace)


@dispatch(object, object)
def dot(x, y, out=None):
    return np.dot(x, y, out=out)


@dispatch(object, object)
def tensordot(a, b, axes=2):
    return np.tensordot(a, b, axes=axes)


@dispatch(object)
def where(condition):
    return np.where(condition)


@dispatch(object, object, object)
def where(condition, x, y):
    return np.where(condition, x, y)


@dispatch(object)
def nanmin(a, axis=None, out=None, keepdims=np._NoValue):
    return np.nanmin(a, axis=axis, out=out, keepdims=keepdims)


@dispatch(object)
def nanmax(a, axis=None, out=None, keepdims=np._NoValue):
    return np.nanmax(a, axis=axis, out=out, keepdims=keepdims)


@dispatch(object)
def nansum(a, axis=None, dtype=None, out=None, keepdims=np._NoValue):
    return np.nansum(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims)


@dispatch(object)
def nanprod(a, axis=None, dtype=None, out=None, keepdims=np._NoValue):
    return np.nanprod(a, axis=axis, dtype=dtype, out=out, keepdims=keepdims)


@dispatch(object)
def transpose(a, axes=None):
    return np.transpose(a, axes=axes)


@dispatch(object, numbers.Integral)
@dispatch(object, tuple)
def broadcast_to(array, shape, subok=False):
    return np.broadcast_to(array, shape, subok=subok)
