from pathlib import Path

import click

from Scanner import Scanner
from Parser import Parser


@click.command()
@click.option("--file", default="beispiel_2.txt", help="Pfad zur Graph-Datei.")
@click.option("--verbose", default=False, is_flag=True, help="Nach jedem Berechnungsschritt wird der aktuelle Graph angezeigt und der Benutzer muss das Programm manuell fortsetzen.")
@click.option("--minimum", default=0, help="Minimale Anzahl an versendeten Nachrichten pro Knoten. Default = 0 => Anzahl an Knoten.")
def main(file, verbose, minimum):
    file = Path(file).resolve()
    if not file.exists():
        print("Die angegebene Datei: " + str(file) + " existiert nicht.")
        return
    if minimum < 0:
        print("Minimum muss >= 0 sein.")
        return

    with open(str(file), "r") as f:
        scanner = Scanner(f.read())
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        graph = parser.parse()
        if graph == None or not parser.check_graph():
            print("Error occured.")
            return
        print_graph(file.stem, graph)
        

def print_graph(name, graph):
    print("Graph " + name + " {\n// NODES:")
    for node in graph:
        print(F"\t{node.name}: {node.identifier}")
    print("\n// EDGES:")
    for node in graph:
        for n in node.neighbors:
            print(F"\t{node.name} -> {n.name}")
    print("}")

        
if __name__ == "__main__":
    main()