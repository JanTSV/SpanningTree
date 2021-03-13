import random


class Graph:
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph
        self.verbose = False
        self.minimum = 0

    def run(self, verbose, minimum):
        self.verbose = verbose
        self.minimum = minimum
        if self.minimum == 0:
            self.minimum = len(self.graph)

        # Simulation loop
        while not self.check_messages_sent():
            # Pick a random node
            node = random.choice(self.graph)
            
            # Print extra information if verbose mode is activated
            if self.verbose:
                print(node)
                input("ENTER for next step.")
                node.communicate()
                print(self)
                continue

            # Let the randomly picked node send a message    
            node.communicate()

        # Print the last state of the graph if verbose
        if self.verbose:
            print(self)

        # Print the result of the graph
        print("\nRESULT")
        print("================================")
        self.result()

    def result(self):
        # Get all the roots of the graph. If enough messages have been sent, there should be only 1 root
        roots = []
        for node in self.graph:
            if node.root not in roots:
                roots.append(node.root)
        for r in roots:
            print(F"{r.name} -> Root")
        print("")

        # Print all the enabled edges to a root
        for node in self.graph:
            for k in node.neighbors.keys():
                if node.neighbors[k]["enabled"]:
                    print(F"{node.name} -> {k.name}")

    def check_messages_sent(self):
        # Check if every node in the graph has sent the minimum amount of messanges
        ret = 0
        for node in self.graph:
            if node.messages >= self.minimum:
                ret += 1
        return ret >= len(self.graph)

    def __str__(self):
        # String representation of the graph
        ret = "Graph " + self.name + " {\n// NODES:"
        for node in self.graph:
            ret += F"\n\t{node.name}: {node.identifier} <{node.cost}> <root='{node.root.name}'>"
        ret += "\n// EDGES:"
        for node in self.graph:
            for n, c in node.neighbors.items():
                ret += F"\n\t{node.name} -> {n.name} <{c['cost']}> <{c['enabled']}>"
        ret += "\n}"
        return ret