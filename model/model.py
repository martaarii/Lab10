import networkx as nx
from copy import deepcopy, copy
from database.DAO import Contiguity_dao
from database.DAO import State_dao


class Model:

    def __init__(self):

        self.idMap = {}
        self.grafo = nx.MultiGraph()

    def get_grafo(self, anno):
        self.grafo.clear()
        collegamenti = Contiguity_dao.get_connesioni(Contiguity_dao, anno)
        stati = State_dao.get_stati(State_dao, anno)
        for stato in stati:
            self.idMap[stato.CCode] = stato.StateNme
        for stato in self.idMap:
            self.grafo.add_node(self.idMap[stato])
        for collegamento in collegamenti:
            if (self.grafo.has_edge(self.idMap[collegamento.state2no], self.idMap[collegamento.state1no])):
                print("già presente")
            else:
                self.grafo.add_edge(self.idMap[collegamento.state1no], self.idMap[collegamento.state2no])
        print(len(self.grafo))
        print(len(self.grafo.edges))



    def get_stati_connessi(self):

        result = ""
        for nodo in self.grafo.nodes:
            result += f"{nodo} -- {int(self.grafo.degree[nodo])} vicini \n"
        return result

    def get_num_nodi(self):
        nodi_connessi = 0
        for element in self.grafo:
            if self.grafo.degree[element] > 0:
                nodi_connessi += 1
        return nodi_connessi

    def get_stati_raggiungibili(self, stato):
        stati = ""
        nodi_conf = nx.bfs_tree(self.grafo, stato).nodes()
        for nodo in nodi_conf:
            stati += f"{nodo} \n"
        return stati

    def get_all_stati(self):
        stati = State_dao.get_all_stati(State_dao)
        for stato in self.idMap:
            stati.append(self.idMap[stato])
        return stati

    def connesse(self):
        return nx.number_connected_components(self.grafo)
