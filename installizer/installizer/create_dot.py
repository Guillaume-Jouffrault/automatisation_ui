TAB = 4 * " "
INDENT = 2 * TAB

INDMAX = 16  # !!!!!!!!!!!!!!!!!!!!!!!! a changer


def value_key(key):
    ind = 3
    if key[:4] == 'CLIC':
        ind = 4
    # !!!!!!!!!!!!!!!!!!!!!!!! a changer
    return (key[:ind], key[ind:ind+INDMAX])


def get_list_vertices(g):
    list_vertices = []
    for key in g:
        evenmt, id = value_key(key)
        if id not in list_vertices:
            list_vertices.append(id)
        if evenmt == "CLIC":
            fen_id = str(g[key].id)[:INDMAX]
            if fen_id not in list_vertices:
                list_vertices.append(fen_id)
    return list_vertices


def get_list_edges(g, list_vertices):
    list_edges = []
    ind = 0
    for key in g:
        evenmt, id = value_key(key)

        ind = list_vertices.index(id)  # list(g.keys()).index(...)
        ind_voisin = list_vertices.index(str(g[key].id)[:INDMAX])
        # a changer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if evenmt == 'TAB':
            label = ""
        else:
            label = evenmt
        list_edges.append((ind, ind_voisin, label))
        ind += 1
    return list_edges


def string_list_vertices(list_vertices):
    s = ""
    for i in range(len(list_vertices)):
        s += INDENT+"A"+str(i)+" [label = "+r'"'+list_vertices[i]+r'"]'+"\n"
    return s


def string_list_edges(list_edges):
    s = ""
    for i in range(len(list_edges)):
        ind, ind_voisin, label = list_edges[i]
        s += INDENT+"A"+str(ind) + " -> "+"A" + \
            str(ind_voisin)+r'[label = "'+label+r'"]'+"\n"
    return s


def string_dot(list_vertices, list_edges):
    s = r'digraph "graph" {'+"\n"
    s += string_list_vertices(list_vertices)
    s += string_list_edges(list_edges)
    s += "}"
    return s


def create_dot(g, path):
    list_vertices = get_list_vertices(g)
    list_edges = get_list_edges(g, list_vertices)
    with open(path, 'w') as f:
        s = string_dot(list_vertices, list_edges)
        f.write(s)
        f.close()
