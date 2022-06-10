
def is_fen_containing_clic_edge(g, fen):
    key = fen.get_key("CLIC")
    return (key in g)

# g = dictionnaire = evenement+str(id_fen) -> fen
# Fenetre(id, button_number, number_of_buttons)


def shortest_path(g, fen_start, fen_goal):  # parcours en profondeur

    stack = [(fen_start, "start")]
    explored = []  # id of fen explored
    path = []

    while (len(stack) != 0):
        fen, evenmt = stack.pop(-1)
        print(fen.id)
        if fen.id in explored:
            print("explored : "+str(fen.id))
            all_neigbors_explored = True
            fen_tab = fen
            for _ in range(fen.number_of_buttons-1):
                fen_tab = g[fen_tab.get_key("TAB")]
                if fen_tab.id not in explored:
                    all_neigbors_explored = False
            if all_neigbors_explored:
                print("full_explored : "+str(fen.id))
                if len(path) == 0:
                    print("error0")
                    return []
                if len(path) == 1:
                    print("error1")
                    return []
                path.pop(-1)
                stack.append(path[-1])
        else:
            explored.append(fen.id)
            path.append((fen, evenmt))

            if fen.id == fen_goal.id:
                return path

            # stack_ids = list(map(lambda fen: fen.id, stack))
            fen_tab = fen
            nb_voisins_unexplored = 0
            l_voisins_unexplored = []

            for _ in range(fen.number_of_buttons-1):
                fen_tab = g[fen_tab.get_key("TAB")]
                if fen_tab.id == fen_goal.id:
                    return path+[(fen_goal, "TAB")]
                # a window that hasn't been clicked yet and isnt't fen_goal is useless
                elif (fen_tab.id not in explored):
                    l_voisins_unexplored.append((fen_tab, "TAB"))

            l_voisins_unexplored.reverse()
            stack = stack + l_voisins_unexplored

            nb_voisins_unexplored = len(l_voisins_unexplored)

            if is_fen_containing_clic_edge(g, fen):
                stack.append((g[fen.get_key("CLIC")], "CLIC"))
            elif nb_voisins_unexplored == 0:
                finish = False
                while(not(finish)):
                    fen, evenmt = path.pop(-1)
                    if evenmt == "CLIC":
                        finish = True
                stack.append(path[-1])
    return []
