Berechnet den minimalen Spanning Tree eines Graphen über ein Zufallsprinzip. Es handelt sich um eine Konsolenanwendung. Programmiert wurde in python.

Einrichtung: 
	1. pip install -r requirements.txt
	2. main.py ausführen mit gewünschten Parametern (siehe unten).

Der Graph wird in Form einer txt-Datei eingelesen. Der Name der Datei entspricht dem Namen des Graphen im Programm. Die Syntax dieser Datei sieht folgendermaßen aus:
	1. Knoten: 
	   <Knoten-Name> = <Knoten-ID>;
	
	2. Kante:
	   <Knoten-Name_1> - <Knoten-Name_2> : <Kosten>;

	3. Kommentare:
	   // <Kommentar>

	Beispiel:
	A = 5;
 	B = 1;
 	C = 3;
 	D = 7;
 	E = 6;
	F = 4;

	A - B : 10;
 	A - C : 10;
 	B - D : 15;
 	B - E : 10;
 	C - D : 3;
 	C - E : 10;
 	D - E : 2;
 	D - F : 10;
 	E - F : 2;

Dabei gelten folgende Regeln:
	1. Die Knotennamen bestehen aus alphanumerischen Zeichen.
	2. Kanten- und Knotendefinitionen dürfen beliebig vermischt sein.
	3. Leerzeilen, führende Tabs oder Blanks werden ignoriert.
	4. Kosten dürfen keine Werte <= 0 annehmen.
	5. Die kleinste Konten-ID (also die Root-ID) darf nur einmal im Graphen vorkommen.
	6. Kanten dürfen einen Knoten nicht mit sich selbst verbinden.
	7. Es darf keine losen Knoten geben. Jeder Knoten braucht mindestens eine Kanten zum Graphen.

Folgende Parameter stehen dem Benutzer zur Verfügung:
--help: Zeigt die Hilfe an.
--file <Dateipfad>: Pfad zur Graph-Datei.
--verbose: Nach jedem Berechnungsschritt wird der aktuelle Graph angezeigt und der Benutzer muss das Programm manuell fortsetzen.
--minimum <Schritte>: Minimale Anzahl an versendeten Nachrichten pro Knoten. Default = 0 => Anzahl an Knoten.
 