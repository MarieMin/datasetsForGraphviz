import json


def read_edges(edges_line):
    args = edges_line.split("	")
    if len(args) == 1:
        args = edges_line.split(" ")

    if len(args) == 2:
        return [args[0], args[1]]

    if int(args[2]) == -1:
        args[0], args[1] = args[1], args[0]

    return [args[0], args[1]]


if __name__ == '__main__':

    with open('./originalData/Task_10_000_nodes_27_000_edges.txt', 'r') as orgn, open('./dotArchives/Task_graph_10_000_nodes.dot', 'w+') as dstn:
        dstn.write('digraph {\n')

        for line in orgn.readlines():
            origin_edges = read_edges(line)
            dot_edges = '  n{} -> n{};\n'.format(int(origin_edges[0]), int(origin_edges[1]))

            dstn.write(dot_edges)

        dstn.write('}\n')

    # with open('./originalData/Task_g_5_000_n_18_000_e.txt', 'r') as orgn, open('./dotArchives/Task_graph_5_000_nodes.json', 'w+') as dstn:
    #     dstn.write('[\n')
    #
    #     for line in orgn.readlines():
    #         origin_edges = read_edges(line)
    #
    #         data_set = {"source": origin_edges[0], "target": origin_edges[1]}
    #
    #         json_dump = json.dumps(data_set)
    #
    #         dstn.write(json_dump)
    #         dstn.write(',\n')
    #
    #     dstn.write(']\n')


