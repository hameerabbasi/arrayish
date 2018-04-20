from .defaults import (
    dot, tensordot,
    where,
    nanmin, nanmax, nansum, nanprod,
    transpose,
    broadcast_to
)


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
