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
        # Add a defaultly disabled neighbor to the neighbors dict
        self.neighbors[node] = {"cost": cost, "enabled": False}

    def has_neighbor(self, node):
        # Check if this node has the given node as neighbor
        return node in self.neighbors.keys()

    def communicate(self):
        # Send a message to every neighbor
        for node in self.neighbors.keys():
            node.send_message_to(self)
            self.messages += 1

    def send_message_to(self, node):
        # If the identifier of node is less then self.identifier, updates self
        if node.identifier < self.identifier:
            self.update(node)
        # If the identifiers are equal, update self if the costs are less
        elif node.identifier == self.identifier:
            if self.cost > self.get_cost(node) + node.cost:
                self.update(node)
        # Else disable the edge to node
        else:
            self.enable_edge(node, False)

    def update(self, node):
        # Update the internal state of the node and its edges depending on node
        self.identifier = node.identifier 
        self.cost = self.get_cost(node) + node.cost
        self.enable_edge(node, True)
        self.root = node.root

    def enable_edge(self, node, value):
        # Set the value of 'enabled' of the edge to node to value
        self.neighbors[node]["enabled"] = value
        for n in self.neighbors:
            if n == node:
                n.neighbors[self]["enabled"] = value
            else:
                n.neighbors[self]["enabled"] = not value
                self.neighbors[n]["enabled"] = not value

    def get_cost(self, node):
        # Get the cost of the neighbor node
        return self.neighbors[node]["cost"]

    def __str__(self):
        # String representation of the node
        s = F"<Node name={self.name} id={self.identifier}>\nAnd my neighbors are: "
        for k, v in self.neighbors.items():
            s += k.name + F"<{v['cost']}> "
        return s