from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in range(12):
        graph.add_vertex(i)

    for elem in ancestors:
        graph.add_edge(elem[1], elem[0])
    s = Stack()

    s.push(starting_node)
    visited_path = []

    while s.size() > 0:
        depoped = s.pop()
        for items in sorted(graph.vertices[depoped]):
            s.push(items)

        if depoped not in visited_path and depoped != starting_node:
            visited_path.append(depoped)

    if len(visited_path) < 1:
        return -1
    elif len(visited_path) == 1:
        for elem in visited_path:
            return elem
    return visited_path[len(visited_path) - 1]


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6),
                         (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8))
