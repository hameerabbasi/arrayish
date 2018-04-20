import numpy as np
import multipledispatch as md

dot = md.Dispatcher('dot')
dot.add((object, object), np.dot)

tensordot = md.Dispatcher('tensordot')
tensordot.add((object, object), np.tensordot)

where = md.Dispatcher('where')
where.add((object,), np.where)
where.add((object, object, object), np.where)

nanmin = md.Dispatcher('nanmin')
nanmin.add((object,), np.nanmin)

nanmax = md.Dispatcher('nanmax')
nanmax.add((object,), np.nanmax)

nansum = md.Dispatcher('nansum')
nansum.add((object,), np.nansum)

nanprod = md.Dispatcher('nanprod')
nanprod.add((object,), np.nanprod)

transpose = md.Dispatcher('transpose')
transpose.add((object,), np.transpose)

broadcast_to = md.Dispatcher('broadcast_to')
broadcast_to.add((object,), np.broadcast_to)
