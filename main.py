from pathlib import Path

import click

from Scanner import Scanner
from Parser import Parser
from Graph import Graph


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
        parsed_graph = parser.parse()
        if parsed_graph == None or not parser.check_graph():
            print("Error occured.")
            return
        graph = Graph(file.stem, parsed_graph)
        # print(graph)
        graph.run(verbose, minimum)
        
if __name__ == "__main__":
    main()