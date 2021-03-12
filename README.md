Berechnet den minimalen Spanning Tree eines Graphen mithilfe eines Zufallsprinzips. Es handelt sich um eine Konsolenanwendung. Programmiert wurde in python.

Einrichtung: 
	<ul>
		<li>pip install -r requirements.txt </li>
		<li>main.py ausführen mit gewünschten Parametern (siehe unten) </li>
	</ul>

Der Graph wird in Form einer txt-Datei eingelesen. Der Name der Datei entspricht dem Namen des Graphen im Programm. Die Syntax dieser Datei sieht folgendermaßen aus:
	<ul>
		<li>Knoten:<br> `<Knoten-Name> = <Knoten-ID>;` </li>
		<li>Kante:<br> `<Knoten-Name_1> - <Knoten-Name_2> : <Kosten>;` </li>
		<li>Kommentare:<br> `// <Kommentar>` </li>
	</ul>


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
	<ul>
		<li> Die Knotennamen bestehen aus alphanumerischen Zeichen + Unterstrich. </li>
		<li> Kanten- und Knotendefinitionen dürfen beliebig vermischt sein. </li>
		<li> Leerzeilen, führende Tabs oder Blanks werden ignoriert. </li>
		<li> Kosten dürfen keine Werte <= 0 annehmen. </li>
		<li> Die kleinste Konten-ID (also die Root-ID) darf nur einmal im Graphen vorkommen. </li>
		<li> Kanten dürfen einen Knoten nicht mit sich selbst verbinden. </li>
		<li> Es darf keine losen Knoten geben. Jeder Knoten braucht mindestens eine Kante zum Graphen. </li>
	</ul>

Folgende Parameter stehen dem Benutzer zur Verfügung:
	<ul>
		<li> `--help`: Zeigt die Hilfe an. </li>
		<li> `--file <Dateipfad>:` Pfad zur Graph-Datei. Default: beispiel_2.txt </li>
		<li> `--verbose`: Nach jedem Berechnungsschritt wird der aktuelle Graph angezeigt und der/die Benutzer/in muss das Programm manuell fortsetzen. </li>
		<li> `--minimum <Schritte>`: Minimale Anzahl an versendeten Nachrichten pro Knoten. Default = 0 => Anzahl an Knoten. </li>
	</ul>
 