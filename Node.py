class Node:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.neighbors = {}

    def add_neighbor(self, node, cost):
        self.neighbors[node] = cost

    def has_neighbor(self, name):
        ret = False
        for k in self.neighbors.keys():
            if k.name == name:
                ret = True
        return ret

    def __str__(self):
        s = F"<Node name={self.name} id={self.identifier}>\nAnd my neighbors are: "
        for k, v in self.neighbors.items():
            s += k.name + F"<{v}> "
        return s