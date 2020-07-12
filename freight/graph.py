import logging
import sys

logging.basicConfig(stream=sys.stdout, level="INFO")

class Vertex:
    def __init__(self, name, type):
        self.name = name
        self.color = "red"    # Red --> unvisited; Blue --> visited
        self.neighbours = []
        self.__add_type(type)   # Attribute to identify train or city

    def add_neighbour(self, v):
        n_set = set(self.neighbours)
        if v not in n_set:
            self.neighbours.append(v)
            self.neighbours.sort()

    def __add_type(self, type):
        if type == "train" or type == "city":
            self.type = type
        else:
            logging.error("Invalid vertix type.")

class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, v, u):
        if v in self.vertices and u in self.vertices:
            for key, value in self.vertices.items():
                if key == v:
                    value.add_neighbour(u)
                elif key == u:
                    value.add_neighbour(v)

    def print(self):
        for key in sorted(self.vertices.keys()):
            print(key + " " + str(self.vertices[key].neighbours))

    def find_path(self, src, dest):
        route_array = []
        vertex_list = []
        self.vertices[src].color = "blue"
        vertex_list.append(src)
        while vertex_list:
            traversing = False
            curr_vertex = vertex_list.pop()
            route_array.append(curr_vertex)
            if curr_vertex == dest:
                return route_array
            for v in self.vertices[curr_vertex].neighbours:
                if self.vertices[v].color == "red":
                    traversing = True
                    self.vertices[v].color = "blue"
                    vertex_list.append(v)
            if not traversing:
                route_array.pop()
        self.__clear_status()
        return route_array

    def __clear_status(self):
        for _, vertex in self.vertices.items():
            vertex.color = "red"

