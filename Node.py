class Node:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.cost = 0
        self.root = self
        self.messages = 0
        self.neighbors = {}
        self.ways = []

    def add_neighbor(self, node, cost):
        self.neighbors[node] = {"cost": cost, "enabled": False}

    def has_neighbor(self, name):
        ret = False
        for k in self.neighbors.keys():
            if k.name == name:
                ret = True
        return ret

    def communicate(self):
        for node in self.neighbors.keys():
            node.send_message_to(self)
            self.messages += 1

    def send_message_to(self, node):
        if node.identifier < self.identifier:
            self.update(node)
        elif node.identifier == self.identifier:
            if self.cost > self.get_cost(node) + node.cost:
                self.update(node)
        else:
            self.enable_edge(node, False)

    def update(self, node):
        self.identifier = node.identifier 
        self.cost = self.get_cost(node) + node.cost
        self.enable_edge(node, True)
        self.root = node.root

    def enable_edge(self, node, value):
        self.neighbors[node]["enabled"] = value
        for n in self.neighbors:
            if n == node:
                n.neighbors[self]["enabled"] = value
            else:
                n.neighbors[self]["enabled"] = not value
                self.neighbors[n]["enabled"] = not value

    def get_cost(self, node):
        return self.neighbors[node]["cost"]

    def __str__(self):
        s = F"<Node name={self.name} id={self.identifier}>\nAnd my neighbors are: "
        for k, v in self.neighbors.items():
            s += k.name + F"<{v['cost']}>"
        return s