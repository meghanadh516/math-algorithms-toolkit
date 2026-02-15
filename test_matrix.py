from algorithms import (
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose
)


def test_add_matrices():
    assert add_matrices([[1,2],[3,4]], [[5,6],[7,8]]) == [[6,8],[10,12]]


def test_subtract_matrices():
    assert subtract_matrices([[5,6],[7,8]], [[1,2],[3,4]]) == [[4,4],[4,4]]


def test_multiply_matrices():
    assert multiply_matrices([[1,2],[3,4]], [[5,6],[7,8]]) == [[19,22],[43,50]]


def test_transpose():
    assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]

