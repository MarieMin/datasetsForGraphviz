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

def handle_dot_file():
    with open('./dotArchives/Task_graph_35_000_nodes.dot', 'r') as orgn, open('./dotArchives/Task_graph_35_000_nodes_optim.dot', 'w+') as dstn:
        orgn.readline()
        dstn.write('digraph {\n')

        for line in orgn.readlines():
            line = line[2:]
            if len(line) < 1 :
                continue
            args = line.split(" ", maxsplit=4)
            if (args[1])[0] == '[':
                continue
            dot_edges = '  n{} -> n{};\n'.format(int(args[0]), int(args[2]))
            dstn.write(dot_edges)

        dstn.write('}\n')

if __name__ == '__main__':

    # with open('./originalData/Task_graph_20_000_nodes.txt', 'r') as orgn, open('./dotArchives/Task_graph_20_000_nodes.dot', 'w+') as dstn:
    #     dstn.write('digraph {\n')
    #
    #     for line in orgn.readlines():
    #         origin_edges = read_edges(line)
    #         dot_edges = '  n{} -> n{};\n'.format(int(origin_edges[0]), int(origin_edges[1]))
    #
    #         dstn.write(dot_edges)
    #
    #     dstn.write('}\n')

    handle_dot_file()




