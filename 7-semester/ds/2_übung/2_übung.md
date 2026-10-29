# Übung 2 - Datenverständnis

## Aufgabe 1

### Aufgabenstellung

In der Vorlesung wird der Ansatz "Schema on Write" erwähnt, der z. B. klassischen Datenbanksystemen zugrunde liegt. Dabei muss zuerst ein Schema definiert werden, bevor Daten in ein (Datenbank-)System eingefügt und verwaltet werden können.

Überlegen Sie sich, wie im Gegensatz dazu der Ansatz "Schema on Read" funktionieren würde. Geben Sie jeweils drei Vorteile der Ansätze "Schema on Write" und "Schema on Read" an.

### Bearbeitung

Bei "Schema on Read" werden die Daten beim Lesen anhand eines Schemas interpretiert. Ein einheitliches Schema mit festgelegten Datentypen muss daher nicht bereits beim Schreiben erzwungen werden.

**Vorteile von Schema on Read:**

- Potenziell schnellere Schreibprozesse, da beim Einlesen weniger Umwandlungen und Schemaprüfungen erforderlich sind
- Flexibleres Speichern, da beim Schreiben kein einheitliches Schema erzwungen werden muss
- Verschiedene Sichten auf dieselben gespeicherten Daten möglich

**Vorteile von Schema on Write:**

- Sicherung der Datenintegrität durch Prüfung der Daten beim Schreiben
- Ein festgelegtes Schema als Grundlage für die Dokumentation
- Potenziell effizientere Abfragen durch bereits strukturierte und typisierte Daten

## Aufgabe 2

### Aufgabenstellung

Betrachten Sie gerichtete, gewichtete Property-Graphen wie in Kapitel 3, Folie 4. Geben Sie ein Entity-Relationship-Modell für diese Datenstruktur an und überführen Sie dieses in Relationenschemata, die sich in einer relationalen Datenbank abbilden ließen.

Anders ausgedrückt: repräsentieren Sie systematisch Property-Graphen in einer relationalen Datenbank.

### Bearbeitung

#### ER-Modell

Siehe [ER-Modell](2_übung_ER.drawio).

#### Relationenschema

Knoten(**<u>KnotenId</u>**, Name)

Kanten(**<u>KantenId</u>**, Name, Gewicht)

KnotenEigenschaften(**<u>KnEId</u>**, <u>KnotenId</u>, Key, Value)

KantenEigenschaften(**<u>KaEId</u>**, <u>KantenId</u>, Key, Value)

KnotenHatKante(<u>VonKnotenId</u>, <u>ZuKnotenId</u>, **<u>KantenId</u>**)

Primärschlüssel sind fett markiert. Die Fremdschlüssel verweisen wie folgt auf die zugehörigen Primärschlüssel:

- `KnotenEigenschaften.KnotenId` auf `Knoten.KnotenId`
- `KantenEigenschaften.KantenId` auf `Kanten.KantenId`
- `KnotenHatKante.VonKnotenId` und `KnotenHatKante.ZuKnotenId` auf `Knoten.KnotenId`
- `KnotenHatKante.KantenId` auf `Kanten.KantenId`

Zu jeder Kante muss genau eine Zeile in `KnotenHatKante` mit einem Start- und einem Zielknoten vorhanden sein.

## Aufgabe 3

### Aufgabenstellung

Betrachten Sie eine Hierarchie von Abteilungen in einer Firma, die wie folgt in einer Relation repräsentiert wird. Sie finden diese Daten auch in der Oracle-Datenbank `pcork1` auf `cork.fh-trier.de:1521` in der Tabelle `ds_abteilung`, die Sie mit Ihrem Account `dsXYZ` mit einem beliebigen Oracle-Client (SQL\*Plus, SQL Developer, DataGrip, VS Code, …) benutzen können.

**Abteilungen**

| abt_nr | abt_name             | kosten     | ober_abt_nr |
| ------ | -------------------- | ---------- | ----------- |
| 1      | Meyer AG             | 50.000     | -           |
| 2      | Vertrieb             | 10.000     | 1           |
| 3      | Produktion           | 20.000     | 1           |
| 4      | Vertrieb DE          | 1.000.000  | 2           |
| 5      | Vertrieb FR          | 500.000    | 2           |
| 6      | Produktion Automobil | 10.000.000 | 3           |
| 7      | Produktion Aero      | 20.000.000 | 3           |
| …      | …                    | …          | …           |

Schreiben Sie eine Anfrage in SQL, die die Kosten jeder Abteilung inklusive aller ihrer Unterabteilungen berechnet (Hinweis: Rekursion, UNION ALL). Können Sie zusätzlich ausgeben, in welcher Tiefe (d.h. Entfernung von der Wurzel "Meyer AG") die jeweilige Abteilung steht?

### Bearbeitung

Die mit KI-Unterstützung erstellte Anfrage berechnet für jede Abteilung die Summe ihrer eigenen Kosten und der Kosten aller Unterabteilungen. Die Syntax ist für Oracle formuliert.

```sql
WITH kostenbaum (start_abt_nr, abt_nr, kosten) AS (
    SELECT abt_nr, abt_nr, kosten
    FROM ds_abteilung

    UNION ALL

    SELECT k.start_abt_nr, a.abt_nr, a.kosten
    FROM kostenbaum k
    JOIN ds_abteilung a
        ON a.ober_abt_nr = k.abt_nr
)
SELECT start_abt_nr, SUM(kosten) AS gesamtkosten
FROM kostenbaum
GROUP BY start_abt_nr
ORDER BY start_abt_nr;
```

Die Zusatzaufgabe zur Tiefe wurde nicht bearbeitet.
