from TokenType import TokenType
from Token import Token
from Rules import Rules
from Node import Node


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.had_error = False
        self.rules = Rules()
        self.graph = []

    def parse(self):
        while not self.is_at_end() and not self.had_error:
            self.parse_block()
        if self.had_error:
            return None
        return self.graph

    def parse_block(self):
        token = self.advance()
        if token.t == TokenType.EQUAL:
           if self.check_rule(self.rules.DECLARATION_RULE):
               self.add_node()

        elif token.t == TokenType.MINUS:
            if self.check_rule(self.rules.EDGE_RULE):
                self.add_neighbor()

    def check_rule(self, rule):
        ret = True
        for k, v in rule.items():
            if self.peek(k).t != v["expected"]:
                self.error(v["error"])
                self.had_error = True
                ret = False
        return ret

    def add_node(self, name=None, id=-1):
        if name == None:
            name = self.peek(-2).literal
        if id == -1:
            id = self.peek(0).literal
        
        check = self.get_node(name)
        if check == None:
            node = Node(name, id)
            self.graph.append(node)
            return node
        else:
            if check.identifier == None:
                check.identifier = id
            else:
                self.error("Node is already initialized.")

    def add_neighbor(self):
        left = self.get_node(self.peek(-2).literal)
        right = self.get_node(self.peek(0).literal)
        cost = self.peek(2).literal

        if left == None:
            left = self.add_node(self.peek(-2).literal, None)
        
        if right == None:
            right = self.add_node(self.peek(0).literal, None)

        if not left.has_neighbor(right.name):
            left.add_neighbor(right, cost)
        else:
            self.error("Edge already exists.")

        if not right.has_neighbor(left.name):
            right.add_neighbor(left, cost)
        else:
            self.error("Edge already exists.")
        
    def get_node(self, name):
        for node in self.graph:
            if node.name == name:
                return node
        return None

    def peek(self, x):
        pos = self.current + x
        if (pos < 0) or (pos >= len(self.tokens)):
            return None
        return self.tokens[pos]

    def advance(self):
        self.current += 1
        return self.tokens[self.current - 1]

    def is_at_end(self):
        return self.current >= len(self.tokens)

    def error(self, message, details=[]):
        self.had_error = True
        print(F"Parser: ERROR <line: {self.tokens[self.current - 1].line}>\t{message}")
        if len(details) > 0:
            s = "DETAILS: "
            for v in details:
                s += F"'{v}' "
            print(s)

    def check_graph(self):
        ret = True
        if len(self.graph) == 0:
            self.error("Pretty empty.")
            return False
        elif len(self.graph) == 1:
            self.error(F"Just one node.")
            ret = False
        m = self.graph[0].identifier
        for node in self.graph:
            if node.identifier != None and node.identifier < m:
                m = node.identifier
            if node.identifier == None:
                self.error(F"<node: {node.name}> No id.")
                ret = False
            if len(node.neighbors.keys()) == 0:
                self.error(F"<node: {node.name}> Not connected.")
                ret = False
        c = 0
        for node in self.graph:
            if node.identifier == m:
                c += 1
        if c != 1:
            self.error("At least two nodes have the lowest identifier.")
            ret = False
        return ret