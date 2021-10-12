def creategraph():  # static graph
    # node structure = Tuple('node_name', 'node_heuristic-value')
    graph = {('h', 120): [('g', 100), ('s', 70), ('b', 80)],
             ('s', 70): [('po', 110), ('rs', 20)],
             ('g', 100): [('rs', 20)],
             ('b', 80): [('ps', 26)],
             ('rs', 20): [('u', 0)],
             ('ps', 26): [('u', 0)]
             }
    goal = ('u', 0)
    return graph, goal


def sort(openlist):
    return sorted(openlist, key=lambda x: x[1])


def bestFirstSearch(graph, goal):
    openlist = []
    closelist = []
    closelist.append(list(graph.keys())[0])
    openlist.extend(list(graph.values())[0])
    while True:
        if closelist[-1] == goal:
            return closelist, goal
        openlist = sort(openlist)
        closelist.append(openlist[0])
        openlist.pop(0)
        temp = graph.get(closelist[-1])
        if temp is not None:
            openlist.extend(temp)
        else:
            continue

    return closelist, goal


def main():
    graph, goal = creategraph()
    output, goal = bestFirstSearch(graph, goal)
    print("For the goal '{}' the path found is {}".format(goal[0], output))


main()
