Arrayish
========

A library for downstream compatibility of Numpy-compatible arrays.

Usage
-----

For an alternative array implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import numpy as np
   import arrayish as ai


   class CustomArray(object):
       """Your custom ``ndarray`` compatible implementation."""
       pass


   def dot(a, b, out=None)
       """ Your custom implementation of ``np.dot``. """
       pass


   # Between your own arrays
   ai.dot.add((CustomArray, CustomArray), dot)

   # With Numpy Arrays, if you'd like. Can also pass another function
   ai.dot.add((np.ndarray, CustomArray), dot)
   ai.dot.add((CustomArray, np.ndarray), dot)

For a downstream library willing to support alternative arrays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import arrayish as ai
   import numpy as np

   # Instead of this:
   np.dot(a, b)

   # Do this:
   ai.dot(a, b)
