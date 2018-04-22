import numpy as np
import pytest

import arrayish as ai

na = np.array([[1, 0], [0, 1]], dtype=np.float32)


class CustomArray(object):
    pass


ca = CustomArray()


@pytest.mark.parametrize('signature, args', [
    ((CustomArray, CustomArray), (ca, ca)),
    ((CustomArray, np.ndarray), (ca, na)),
    ((np.ndarray, CustomArray), (na, ca))
])
def test_dot(signature, args):
    def dot(a, b):
        return 'pass'

    ai.dot.add(signature, dot)
    assert ai.dot(*args) == 'pass'


def test_dot_orig():
    expected = np.dot(na, na)
    actual = ai.dot(na, na)

    assert isinstance(actual, np.ndarray)
    assert np.array_equal(expected, actual)
