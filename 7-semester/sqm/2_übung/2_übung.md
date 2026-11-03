# Übung 2 - Spezifikation, Testen und Qualität

## Aufgabe 1

### Aufgabenstellung

1. Definieren Sie das Verhalten der Methode find_max(Integer [ ] a) {...} mit Ihren eigenen Worten, zunächst ohne die Methode zu implementieren. Versuchen Sie in Ihrer Definition das Verhalten so zu beschreiben, dass die Methode von einem externen Dienstleister nur auf Basis Ihrer Beschreibung implementiert werden könnte.
2. Definieren Sie ähnlich zu dem Beispiel aus der Vorlesung (Sortierprogramm sort()) eine passende Vorbedingung und eine passende Zusicherung für Ihr Programm find_max(...).
3. Geben Sie Ihre Beschreibung aus Aufgabenteil a) und Ihre Spezifikation aus Aufgabenteil einem Ihrer Mitstudierenden (Team) und lassen Sie sie/ihn das Programm implementieren, ohne weitere Erklärungen dazu abzugeben. Hinweis: Als ImplementiererIn sollten Sie sich strikt an die übergebenen Vorgaben halten und nicht an das, was Sie glauben, was der/die SpezifikateurIn gemeint haben könnte.
4. Vergleichen Sie das Ergebnis der Implementierung aus Aufgabenteil c) mit Ihrer Erwartung.

### Bearbeitung 1.

Die Methode find_max() erhält ein gefülltes Array von Integern und gibt den höchsten Wert als Funktionswert wieder

### Bearbeitung 2.

Voraussetzung: Das Argument ist ein nicht leeres Array gefüllt mit Integern ohne null Werte
Zusicherung: Der Funktionswert ist ein Wert aus dem Array und kein anderer Wert aus dem Array ist größer als der Funktionswert

### Bearbeitung 3.

-

### Bearbeitung 4.

-

## Aufgabe 2

### Aufgabenstellung

In der Vorlesung wurden Ihnen Beispiele gezeigt, wie Softwarefehler dem Menschen, der Umwelt oder einem Unternehmen Schaden zufügen können. Recherchieren Sie einen aktuellen, in der Lehrveranstaltung noch nicht behandelten Fall, in dem ein Softwarefehler Menschen, Umwelt oder Unternehmen geschädigt hat. Bereiten Sie einen Kurzvortrag mit drei Folien vor:

- Folie 1: Der Vorfall – was stand auf dem Spiel? Beschreiben Sie das System, sein fehlerhaftes Verhalten und die Folgen. Beginnen Sie mit einer konkreten Situation aus Sicht einer betroffenen Person oder Organisation.
- Folie 2: Die Ursachen – wo hätte Qualitätssicherung ansetzen können? Unterscheiden Sie zwischen dem beobachteten Fehler, seiner technischen Ursache und möglichen organisatorischen Ursachen. Ordnen Sie den Fall mindestens einem Softwarequalitätsmerkmal zu. Kennzeichnen Sie ausdrücklich, was durch Quellen belegt ist und was Sie vermuten.
- Folie 3: Ihre Entscheidung – wofür investieren Sie? Sie sind vor der Veröffentlichung der Software für die Qualität verantwortlich und können zunächst nur eine zusätzliche Maßnahme zur Qualitätssicherung finanzieren. Welche wählen Sie und warum? Beschreiben Sie konkret, wie diese Maßnahme den Fehler hätte Prof. Dr. Georg Rock verhindern, aufdecken oder seine Folgen begrenzen können. Benennen Sie außerdem verbleibende Risiken.

### Bearbeitung

siehe Anhang

## Aufgabe 3

### Aufgabenstellung

In den Vorlesungsunterlagen bzw. im Rahmen der Vorlesungen wurde argumentiert „Testen erhöht indirekt die Prozessqualität, da Fehler dokumentiert, analysiert und damit Fehlhandlungen in Zukunft vermieden werden können.“ Versuchen Sie diese Aussage zu begründen oder zu widerlegen.

### Bearbeitung

Bhandari et al. (1993) beschreiben im Abstract ihrer Fallstudie eine Methode zur Verbesserung des Softwareentwicklungsprozesses anhand von Fehlerdaten. Dabei werden Fehler zunächst so klassifiziert, dass sie bestimmten Prozessaktivitäten zugeordnet werden können. Anschließend werden die Daten mithilfe eines Werkzeugs ausgewertet, um Hinweise für Verbesserungen zu gewinnen.

Die Autoren kommen zu dem Ergebnis, dass ein Projektteam durch die Analyse solcher Fehlerdaten seinen Prozess bereits während der Entwicklung verbessern kann. Das stützt die Aussage, dass Testen indirekt zur Prozessqualität beitragen kann: Erkannte Fehler liefern Daten, aus denen das Team Ansatzpunkte für Prozessänderungen ableiten kann. Entscheidend ist dabei die anschließende Auswertung der Daten.

## Aufgabe 4

### Aufgabenstellung

Erläutern Sie den Begriff Fehlermaskierung. Verwenden Sie hierzu ein selbstdefiniertes einfaches Beispiel.

### Bearbeitung

Definition (ISTQB Glossar):

- Fehlermaskierung ist ein Umstand, bei dem ein Fehlerzustand die Aufdeckung eines
  anderen verhindert.
- Fehlerzustand ist ein Defekt (innerer Fehlerzustand) in einer Komponente oder einem System, der eine geforderte Funktion des Produkts beeinträchtigen kann, z.B. inkorrekte Anweisung oder Datendefinition. Ein Fehlerzustand, der zur Laufzeit angetroffen wird, kann eine Fehlerwirkung einer Komponente oder Systems verursachen.

Bei einer Fehlermaskierung wird ein Fehlerzustand durch einen anderen verdeckt. Nehmen wir an, dass bei einer Loginfunktion zuerst die korrekte Strukturierung einer Email geprüft wird und danach, falls die Email korrekt strukturiert war, ob das Passwort eine gewisse Mindestlänge aufweist. Beide Verifikationen werden separat über eigene Funktionen aufgerufen.
Jedoch geben beide Funktionen immer Falsch als Antwort aus uns führen einen Fehlerzustand hervor. Durch die Abhängigkeit bei den Funktionsaufrufen kommt es zu einer Fehlermaskierung bei der, wenn die Login Funktion als ganzes getestet wird, der Fehler der Funktion zur verifikation der Passwortlänge nicht aufgedeckt werden kann weil der code nie erreicht wird.
