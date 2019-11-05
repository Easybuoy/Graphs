from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    for elem in ancestors:
        graph.add_edge(elem[1], elem[0])

    # print(graph.vertices)
    # print(graph.vertices[starting_node])
    s = Stack()

    s.push(starting_node)
    visited_path = set()

    while s.size() > 0:
        depoped = s.pop()
        print(depoped, 'depp')
        if depoped not in visited_path:
            print(depoped)
            visited_path.add(depoped)

            for items in graph.vertices[depoped]:
                s.push(items)
    print(visited_path)
    if len(visited_path) <= 1:
        return -1
    return list(visited_path)[len(visited_path) - 1]

    # if len(graph.vertices[starting_node]) == 0:
    #     return -1
    # while len(graph.vertices[starting_node]) > 0:
    #     if (len(graph.vertices[starting_node]) == 1):
    #         for item in graph.vertices[starting_node]:
    #             return item
    #     elif len(graph.vertices[starting_node]) > 1:

    # for item in graph.vertices[starting_node]:
    #     print(item)
    # while len(graph.vertices[item]) > 0:
    #     print(graph.vertices[item])
    #     for item2 in graph.vertices[item]:
    #         return item2
    #     if len(graph.vertices[item])
    #     print(graph.vertices[item])
    # return -1

    # print(graph.vertices[starting_node])

    # for item in graph.vertices:
    #     if item == starting_node:
    #     print(item)


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6),
                         (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 3))
