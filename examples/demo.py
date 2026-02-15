from algorithms import (
    add,
    subtract,
    multiply,
    divide,
    multiply_matrices,
    Graph,
    derivative,
    integrate
)


def run_demo():
    print("=== Algebra ===")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))

    print("\n=== Matrix ===")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("Matrix Multiply:", multiply_matrices(A, B))

    print("\n=== Graph ===")
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    print("DFS:", g.dfs(1))
    print("BFS:", g.bfs(1))

    print("\n=== Calculus ===")
    f = lambda x: x**2
    print("Derivative at x=3:", derivative(f, 3))
    print("Integral of x from 0 to 1:", integrate(lambda x: x, 0, 1))


if __name__ == "__main__":
    run_demo()

