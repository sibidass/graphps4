import random
import string

class FreightEdge:
    def __init__(self, name, src_vertex, dest_vertex):
        self.feright_name = name
        self.source_vertex = src_vertex
        self.destination_vertex = dest_vertex
        self.__set_vertex_att()

    def __get_end_vertices(self):
        return (self.source_vertex, self.destination_vertex)

    def __set_vertex_att(self):
        self.destination_vertex.set_in_adjacent_vertex(self.source_vertex)
        self.destination_vertex.set_in_incident_edge(self.__str__())
        self.source_vertex.set_out_adjacent_vertex(self.destination_vertex)
        self.destination_vertex.set_out_incident_edge(self.__str__())

    def __str__(self):
        return self.feright_name

class CityNode:
    def __init__(self, name):
        self.city_name = name
        self.adjacent_vertices = []
        self.visited = False
        self.in_adjacent_vertices = []
        self.out_adjacent_vertices = []
        self.in_incident_edges = []
        self.out_incident_edges = []

    def __set_adjacent_vertices(self, node_list):
        self.adjacent_vertices.extend(node_list)

    def _get_in_degree(self):
        pass

    def _out_degree(self):
        pass

    def get_in_vertices_count(self):
        return len(self.in_adjacent_vertices)

    def get_out_vertices_count(self):
        return len(self.out_adjacent_vertices)

    def set_in_adjacent_vertex(self, vertex):
        self.in_adjacent_vertices.append(vertex)

    def set_out_adjacent_vertex(self, vertex):
        self.out_adjacent_vertices.append(vertex)

    def set_in_incident_edge(self, edge):
        self.in_incident_edges.append(edge)

    def set_out_incident_edge(self, edge):
        self.out_incident_edges.append(edge)

    def _is_visited(self):
        pass

def create_nodes(name_list):
    nodes = []
    for node in name_list:
        nodes.append(CityNode(node))
    return nodes

def link_nodes(link_name, src, dest):
    return FreightEdge(link_name, src, dest)

def dfs(source, dest):
    # find out all out_incident_edges of source.
    # if end vertices of any of these out_incident_edges is dest
    # then return that route
    # for each out_incident_edge
    # find the
    pass

if __name__ == '__main__':
    edges_obj = []
    node_input_list = ["a", "b", "c", "d", "e", "f"]
    nodes = create_nodes(node_input_list)
    edges = ["".join(["T"+random.choice(string.digits) for i in range(2)]) for i in range(7)]
    print("Trains:",edges)
    edges_obj.append(link_nodes(edges[0], nodes[0], nodes[1]))
    edges_obj.append(link_nodes(edges[1], nodes[0], nodes[3]))
    edges_obj.append(link_nodes(edges[2], nodes[0], nodes[4]))
    edges_obj.append(link_nodes(edges[3], nodes[0], nodes[5]))
    edges_obj.append(link_nodes(edges[4], nodes[1], nodes[4]))
    edges_obj.append(link_nodes(edges[5], nodes[2], nodes[4]))
    edges_obj.append(link_nodes(edges[6], nodes[5], nodes[2]))

    for node in nodes:
        print("inAdjacentVertices count of {}:{}".format(node.city_name, node.get_in_vertices_count()))
        print("outAdjacentVertices count of {}:{}".format(node.city_name, node.get_out_vertices_count()))
