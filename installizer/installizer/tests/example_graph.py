from installizer.fenetre import Fenetre
from installizer.shortest_path import shortest_path
from installizer.create_dot import create_dot

number_of_buttons_a = 2
fen_a1 = Fenetre(11, 0, number_of_buttons_a)
fen_a2 = Fenetre(12, 1, number_of_buttons_a)

number_of_buttons_b = 2
fen_b1 = Fenetre(21, 0, number_of_buttons_b)
fen_b2 = Fenetre(22, 1, number_of_buttons_b)

number_of_buttons_c = 2
fen_c1 = Fenetre(31, 0, number_of_buttons_c)
fen_c2 = Fenetre(32, 1, number_of_buttons_c)

number_of_buttons_d = 2
fen_d1 = Fenetre(41, 0, number_of_buttons_d)
fen_d2 = Fenetre(42, 1, number_of_buttons_d)

number_of_buttons_e = 2
fen_e1 = Fenetre(51, 0, number_of_buttons_e)
fen_e2 = Fenetre(52, 1, number_of_buttons_e)

g = {}
g[fen_a1.get_key("TAB")] = fen_a2
g[fen_a2.get_key("TAB")] = fen_a1
g[fen_b1.get_key("TAB")] = fen_b2
g[fen_b2.get_key("TAB")] = fen_b1
g[fen_c1.get_key("TAB")] = fen_c2
g[fen_c2.get_key("TAB")] = fen_c1
g[fen_d1.get_key("TAB")] = fen_d2
g[fen_d2.get_key("TAB")] = fen_d1
g[fen_e1.get_key("TAB")] = fen_e2
g[fen_e2.get_key("TAB")] = fen_e1

g[fen_a1.get_key("CLIC")] = fen_b1
g[fen_a2.get_key("CLIC")] = fen_e1
g[fen_b1.get_key("CLIC")] = fen_c1
g[fen_b2.get_key("CLIC")] = fen_d1

# --------------------------------------------------------

print(45*"-")

fen_start = fen_a1
fen_goal = fen_e1
l = shortest_path(g, fen_start, fen_goal)

print(45*"-")

for fen, evemt in l:
    print(fen.id, evemt)

print(45*"x")

# --------------------------------------------------------
PATH = 'c:\\Users\\lhs\\Documents\\installizer\\installizer\\output.dot'
# list_vertices = list(g.keys())
# print(list_vertices.index('22'))

create_dot(g, PATH)
