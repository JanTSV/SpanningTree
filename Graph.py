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

        while not self.check_messages_sent():
            node = random.choice(self.graph)
            if self.verbose:
                print(node)
                input("ENTER for next step.")
                node.communicate()
                print(self)
                continue
                
            node.communicate()

        if self.verbose:
            print(self)

        print("\nRESULT")
        print("================================")
        self.result()

    def result(self):
        # Roots
        roots = []
        for node in self.graph:
            if node.root not in roots:
                roots.append(node.root)
        for r in roots:
            print(F"{r.name} -> Root")
        print("")
        for node in self.graph:
            for k in node.neighbors.keys():
                if node.neighbors[k]["enabled"]:
                    print(F"{node.name} -> {k.name}")

    def check_messages_sent(self):
        ret = 0
        for node in self.graph:
            if node.messages >= self.minimum:
                ret += 1
        return ret >= len(self.graph)

    def __str__(self):
        ret = "Graph " + self.name + " {\n// NODES:"
        for node in self.graph:
            ret += F"\n\t{node.name}: {node.identifier} <{node.cost}> <root='{node.root.name}'>"
        ret += "\n// EDGES:"
        for node in self.graph:
            for n, c in node.neighbors.items():
                ret += F"\n\t{node.name} -> {n.name} <{c['cost']}> <{c['enabled']}>"
        ret += "\n}"
        return ret