class Freight_Booking:
    def __init__(self):
        pass

    # Reads input file containing names of cities and freight trains b/w them and generate graph
    # each row in the format train/city1/city2/.../cityN
    # eg: T1235 / Chennai / New Delhi
    def readCityTrainfile(self, inputfile):
        pass

    # Will give count on unique freight trains, cities
    # Will give list of freight trains and cities
    def showAll(self):
        pass

    # Will display the transport hub.
    # Also displays count and names of incoming freight trains
    # Is triggered when searchTransportHub tag is found in prompts file
    def displayTransportHub(self):
        pass

    #  Will display count and list of cities connected by a train
    #  triggered when searchTrain tag along with train is found in prompts file
    def displayConnectedCities(self, train):
        pass

    # displays frieght name that can be booked to send package directly from a to b.
    # triggered when searchCities tag is found in prompts file.
    # can pick the first train name found, between 2 cities.
    def displayDirectTrain(self, a, b):
        pass

    # finds if package can be sent from a to b with any number of stops/transfers
    #  triggered when ServiceAvailability tag is found in prompts file.
    def findServiceAvailable(self, a, b):
        pass