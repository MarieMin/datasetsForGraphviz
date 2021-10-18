
def read_edges(edges_line):
    args = edges_line.split("	")

    if len(args) == 2:
        return [args[0], args[1]]

    if int(args[2]) == -1:
        args[0], args[1] = args[1], args[0]

    return [args[0], args[1]]


if __name__ == '__main__':

    with open('./originalData/DAG_685_000_nodes.txt', 'r') as orgn, open('./dotData/DAG_685_000_nodes.dot', 'w+') as dstn:
        dstn.write('digraph {\n')

        for line in orgn.readlines():
            origin_edges = read_edges(line)
            dot_edges = '  n{} -> n{};\n'.format(int(origin_edges[0]), int(origin_edges[1]))

            dstn.write(dot_edges)

        dstn.write('}\n')


