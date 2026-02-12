"""
matrix.py

Basic matrix operations using lists of lists.
"""


def transpose(matrix):
    """
    Returns the transpose of a matrix.
    """
    return [list(row) for row in zip(*matrix)]


def matrix_add(A, B):
    """
    Returns the sum of two matrices A and B.
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have same dimensions")

    return [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def matrix_multiply(A, B):
    """
    Returns the product of matrices A and B.
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns of A must equal rows of B")

    result = [
        [0 for _ in range(len(B[0]))]
        for _ in range(len(A))
    ]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

