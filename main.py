class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'Start': 1,
            'Vanderbilt_44': 1,
            'Vanderbilt_43': 1,
            'Vanderbilt_42': 1,
            'Park_42': 1,
            'Park_41': 1,
            'Park_40': 1,
            'Madison_45': 1,
            'Madison_44': 1,
            'Madison_43': 1,
            'Madison_42': 1,
            'Madison_41': 1,
            'Madison_40': 1,
            'Madison_39': 1,
            '5_45': 1,
            '5_44': 1,
            '5_43': 1,
            '5_42': 1,
            '5_41': 1,
            '5_40': 1,
            '5_39': 1,
            '5_38': 1,
            'Americas_38': 1,
            'Americas_40': 1,
            'Americas_41': 1,
            'Americas_42': 1,
            'Goal': 1
        }

        return H[n]

        # heuristic function with equal values for all nodes

    def h2(self, n):
        H = {
            'Start': 1,
            'Vanderbilt_44': 1,
            'Vanderbilt_43': 1,
            'Vanderbilt_42': 4,
            'Park_42': 4,
            'Park_41': 1,
            'Park_40': 1,
            'Madison_45': 1,
            'Madison_44': 1,
            'Madison_43': 4,
            'Madison_42': 1,
            'Madison_41': 1,
            'Madison_40': 1,
            'Madison_39': 6,
            '5_45': 4,
            '5_44': 4,
            '5_43': 40,
            '5_42': 4,
            '5_41': 4,
            '5_40': 4,
            '5_39': 6,
            '5_38': 4,
            'Americas_38': 1,
            'Americas_40': 1,
            'Americas_41': 1,
            'Americas_42': 4,
            'Goal': 6
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node, answer):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            if answer == 'no':
                for v in open_list:
                    if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                        n = v
            else:
                for v in open_list:
                    if n is None or g[v] + self.h2(v) < g[n] + self.h2(n):
                        n = v

            if n is None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructing the path from it to the start_node
            if n == stop_node:
                recreate_path = []

                while parents[n] != n:
                    recreate_path.append(n)

                    n = parents[n]

                recreate_path.append(start_node)

                recreate_path.reverse()

                print('Path found: {}'.format(recreate_path))
                return recreate_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    'Start': [('Vanderbilt_44', 1), ('Madison_45', 1)],
    'Vanderbilt_44': [('Vanderbilt_43', 1)],
    'Vanderbilt_43': [('Madison_43', 1), ('Vanderbilt_42', 1)],
    'Vanderbilt_42': [('Madison_42', 1)],
    'Park_42': [('Vanderbilt_42', 1)],
    'Park_41': [('Park_42', 1)],
    'Park_40': [('Park_41', 1)],
    'Madison_45': [('5_45', 2)],
    'Madison_44': [('Vanderbilt_44', 1), ('Madison_45', 1)],
    'Madison_43': [('5_43', 1), ('Madison_44', 1)],
    'Madison_42': [('Madison_43', 1), ('5_42', 2)],
    'Madison_41': [('Park_41', 2), ('Madison_42', 1)],
    'Madison_40': [('Park_40', 2), ('Madison_41', 1)],
    'Madison_39': [('5_39', 2), ('Madison_40', 1)],
    '5_45': [('5_44', 1)],
    '5_44': [('5_43', 1), ('Madison_44', 2)],
    '5_43': [('5_42', 1), ('Madison_43', 2)],
    '5_42': [('5_41', 1), ('Americas_42', 3)],
    '5_41': [('5_40', 1), ('Madison_41', 2)],
    '5_40': [('5_39', 1), ('Madison_40', 2)],
    '5_39': [('5_38', 1), ('Goal', 3)],
    '5_38': [],
    'Americas_38': [('5_39', 3)],
    'Americas_40': [('Americas_41', 1), ('5_40', 3)],
    'Americas_41': [('Americas_42', 1)],
    'Americas_42': [],
    'Goal': [('Americas_40', 1)],
}

print("Is the time between 2pm and 7pm? Answer 'yes' or 'no'")
answer = input()
g1 = Graph(adjacency_list)
print('Not Between 2pm and 7pm:')
g1.a_star_algorithm('Start', 'Goal', answer)
print("Is the time between 2pm and 7pm? Answer 'yes' or 'no'")
answer2 = input()
g2 = Graph(adjacency_list)
print('Between 2pm and 7pm:')
g2.a_star_algorithm('Start', 'Goal', answer2)
