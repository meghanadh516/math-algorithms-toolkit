from algorithms import Graph


def test_graph_dfs():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    dfs_result = g.dfs(1)
    assert dfs_result == [1, 2, 4, 3]


def test_graph_bfs():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    bfs_result = g.bfs(1)
    assert bfs_result == [1, 2, 3, 4]

