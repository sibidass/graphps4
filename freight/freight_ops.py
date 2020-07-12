from helpers.reader import file_reader, file_writer
from helpers.tmpl import loaded_templates
from .graph import Graph, Vertex
import configparser

config = configparser.ConfigParser()
config.read("../helpers/templates.ini")


class Freight_Booking:
    def __init__(self, **kwargs):
        self.g = Graph()
        self.op_file = kwargs.pop("output_file", "outputPS4.txt")

    def readCityTrainfile(self, inputfile):
        train_data = file_reader(inputfile)
        for train in train_data:
            self.g.add_vertex(Vertex(train, "train"))
            cities = train_data[train]
            for city in cities:
                self.g.add_vertex(Vertex(city, "city"))
                self.g.add_edge(train, city)

    def showAll(self):
        vertices = self.g.vertices
        train_list = []
        city_list = []
        for name, vertex in vertices.items():
            if vertex.type == "train":
                train_list.append(name)
            elif vertex.type == "city":
                city_list.append(name)
        text_train_data = loaded_templates.show("show_all", tcount=len(train_list), ccount=len(city_list),
                                         train_list="\n".join(train_list), city_list="\n".join(city_list))
        text_section = section_header("showAll")
        file_writer(self.op_file, text_section, text_train_data)

    def displayTransportHub(self):
        train_count = 0
        hub = "Not Found"
        trains = []
        for name, vertex in self.g.vertices.items():
            if vertex.type == "city" and len(vertex.neighbours) > train_count:
                trains = vertex.neighbours
                train_count = len(vertex.neighbours)
                hub = vertex.name

        text_hub_data = loaded_templates.show("t_hub", hub=hub, tcount=train_count, train_list="\n".join(trains))
        text_section = section_header("displayTransportHub")
        file_writer(self.op_file, text_section, text_hub_data)

    def displayConnectedCities(self, train):
        text_section = section_header("displayConnectedCities")
        if train not in self.g.vertices:
            msg = "Train {} not found".format(train)
            file_writer(self.op_file, text_section, msg)
            return
        for name in self.g.vertices:
            if name == train:
                vertex = self.g.vertices[name]
                cities_connected = vertex.neighbours
                count = len(cities_connected)
        text_cities_data = loaded_templates.show("cc", train_no=train, ccount=count,
                                                 city_list="\n".join(cities_connected))
        file_writer(self.op_file, text_section, text_cities_data)

    def displayDirectTrain(self, a, b):
        src = a
        dest = b
        src_vertex = self.g.vertices[src]
        text_section = section_header("displayDirectTrain")
        result_text = "No direct train found between above cities"
        for train in src_vertex.neighbours:
            train_vertex = self.g.vertices[train]
            if dest in train_vertex.neighbours:
                train_no = train
                result_text = "Package can be sent directly: Yes, {}".format(train_no)
                break
        text_transit_data = loaded_templates.show("d_transit", src=src, dest=dest, msg=result_text)
        file_writer(self.op_file, text_section, text_transit_data)

    def findServiceAvailable(self, a, b):
        text_section = section_header("findServiceAvailable")
        path = self.g.find_path(a, b)  # Path finder
        if len(path) >= 2:
            path_details = ">".join(path)
            msg = "Can the package be sent: Yes, " + path_details
        else:
            msg = "Package cannot be sent from {} to {} due to lack of service connecting these cities".format(a, b)
        text_transit_data = loaded_templates.show("d_transit", src=a, dest=b, msg=msg)
        print(text_transit_data)
        file_writer(self.op_file, text_section, text_transit_data)

def section_header(section_name):
    return loaded_templates.show("section_header", func=section_name)