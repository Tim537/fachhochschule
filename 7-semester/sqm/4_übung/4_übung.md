# Übung 4 - Testen, Qualität, Vorgehensmodelle

## Aufgabe 1

### Aufgabenstellung

Nennen Sie sechs Faktoren, die die Qualitätssicherung heutiger software-basierter Systeme anspruchsvoll machen.

### Bearbeitung

- **CI/CD und kurze Releasezyklen:** Häufige Änderungen müssen fortlaufend geprüft werden. Automatisierte Tests müssen schnell und zuverlässig Rückmeldung geben, damit fehlerhafte Änderungen vor der Auslieferung erkannt werden. [Quelle: Microsoft](https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery)
- **Verteilte Systeme:** Netzwerkverzögerungen und Teilausfälle erzeugen viele mögliche Fehlerzustände. Ihr Zusammenspiel ist aufwendig zu testen und Fehler sind oft schwer reproduzierbar. [Quelle: AWS](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/)
- **Geräte- und Plattformvielfalt:** Unterschiedliche Geräte, Betriebssystemversionen und Konfigurationen vergrößern die Zahl der zu prüfenden Kombinationen. [Quelle: Android Developers](https://developer.android.com/training/testing/fundamentals)
- **Prüfung von KI-generiertem Code:** Plausibel wirkender Code kann Fehler und Sicherheitslücken enthalten. Auch KI-generierte Tests müssen unabhängig geprüft werden, da sie dieselben falschen Annahmen wie der Code übernehmen können. [Quelle: OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html)
- **Externe Softwareabhängigkeiten:** Bibliotheken und Frameworks bringen eigene Abhängigkeiten und Schwachstellen mit. Auch fremde Komponenten und ihre Updates müssen über den gesamten Lebenszyklus geprüft werden. [Quelle: NIST, SSDF PW.4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf)
- **Cybersicherheit:** Korrekte Funktionen allein reichen nicht aus; auch Missbrauch und Angriffe müssen geprüft werden. Neue Schwachstellen erfordern laufende Sicherheitsprüfungen und Nachbesserungen. [Quelle: NCSC](https://www.ncsc.gov.uk/collection/software-security-code-of-practice-implementation-guidance/theme-1-secure-design-development)

## Aufgabe 2 (Team, Durchführen von JUnit Tests bei vorgegebenem Beispielcode)

### Aufgabenstellung

Da wir zum Testen von IntakeDAV wahrscheinlich nicht in den Code schauen können, also keine Komponententests im Sinne von White-Box-Tests ausführen können, werden wir dies in dieser Aufgabe im Rahmen einer einfachen Implementierung üben. Dabei werde ich Ihnen den Code vorgeben.

Sie benötigen für diese Aufgabe:

- Eclipse IDE (z. B. v4.6 „Neon“ Installer oder neuer)
  - [Eclipse Downloads](http://www.eclipse.org/downloads)
  - Select: Get Eclipse Neon
  - Start Installer
  - Select: Eclipse IDE for Java Developers
  - Start Eclipse

Dann sollten Sie wie folgt vorgehen. Das Übungsprojekt finden Sie auf StudIP unter dem Namen `Uebung1-2.zip` im Ordner `3-Sonstige Unterlagen`.

1. Eclipse starten und das Übungsprojekt importieren
   1. File → Import, General → Existing Projects into Workspace
   2. Next klicken
   3. Auf der nächsten Seite vom Wizard das Projektarchiv angeben
   4. Finish klicken
2. Das Beispiel verstehen
   1. Die Beschreibung des Adressbuchs lesen
   2. Den Quellcode anschauen
   3. Dazu die Klasse `exercise1.addressbook.controller.Manager` ausführen
      - Rechtsklick auf die Klasse → Run As → Java Application
3. Anschließend sollten Sie die Datei für die JUnit Testfälle bearbeiten
   1. `/Uebung1/src/exercise1/test/AddressBookFunctionalTest.java`
4. Ihre Tests sollten fehlerfrei ausführen
   1. Rechtsklick auf die Testklasse → Run As → JUnit Test
5. Die fertige Testklasse soll im Rahmen der Übung erklärt und vorgeführt werden.

Die Implementierung nutzt das Entwurfspattern „MVC“. Dabei ist die Implementierung noch am Anfang, aber es sollen bereits erste Tests ausgeführt werden.

Wir kommen nun zu der Durchführung von JUnit Tests (hier JUnit 4, Sie können auch JUnit 5 verwenden).

1. Schreiben Sie eine Methode zum Aufsetzen der Testumgebung (`setUp()`) (Warum ist diese Methode notwendig?). Diese Methode soll automatisch vor jedem JUnit Testfall ausgeführt werden. Innerhalb der Methode soll zumindest ein neues `AddressBook` Objekt angelegt und im Attribut `addressBook` gespeichert werden.
2. Schreiben Sie einen JUnit Testfall zum Überprüfen der Funktionalität der `addEntry()` Methode der Klasse `AddressBook`.
3. Schreiben Sie einen JUnit Testfall zum Überprüfen der Funktionalität der `getEntry()` Methode der Klasse `AddressBook`.

### Bearbeitung

```java
/*
 * Example code used in exercises for lecture "Grundlagen des Software-Testens"
 * Created and given by Ina Schieferdecker, Theo Vassiliou and Julia Martini
 * Technische Universität Berlin
 */
package exercise1.test;

import static org.junit.Assert.assertThrows;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.Collection;

import org.junit.Before;
import org.junit.Test;

import exercise1.addressbook.model.AddressBook;
import exercise1.addressbook.model.EmailAddress;
import exercise1.addressbook.model.Entry;
import exercise1.addressbook.model.Gender;
import exercise1.addressbook.model.PhoneNumber;
import exercise1.addressbook.model.SizeLimitReachedException;

/**
 * Uebung 1 - Grundlagen des Testens mit JUnit
 * 
 * Bitte Nummer der Gruppe eintragen: 0
 * 
 * Bitte Gruppenmitglieder eintragen:
 * 
 * @author ...
 * @author ...
 * @author ...
 * @author ...
 */
public class AddressBookFunctionalTest {

	// The component under test
	private AddressBook addressBook;

	/*
	 * Aufgabe 3a) Schreiben Sie eine Methode zum Aufsetzen der Testumgebung
	 * ("Fixture"). Diese Methode soll automatisch vor jedem einzelnen JUnit
	 * Testfall ausgeführt werden. Innerhalb der Methode soll mindestens ein
	 * neues AddressBook Objekt angelegt und im Attribut "addressBook"
	 * gepeichert werden.
	 */
	@Before
	public void setUp() {
		addressBook = new AddressBook();
	}

	/*
	 * Aufgabe 3b) Schreiben Sie einen JUnit Testfall zum überprüfen der
	 * Funktionalität der addEntry() Methode.
	 */
	@Test
	public void add11EntriesToAddressBook() throws SizeLimitReachedException {
		/* Add 10 entries */
		for (int i = 0; i < 10; i++) {
		    Entry entry = new Entry("Java", "Entwickler" + i, Gender.Male, new EmailAddress("java@development.com"));
		    assertTrue(addressBook.addEntry(entry));
		}
		
		/* Add 11th entry */
		Entry eleventhEntry = new Entry("PHP", "Entwickler", Gender.Male, new EmailAddress("php@development.com"));
		
		assertThrows(SizeLimitReachedException.class, () -> {addressBook.addEntry(eleventhEntry);});
	}

	/*
	 * Aufgabe 3c) Schreiben Sie einen JUnit Testfall zum überprüfen der
	 * Funktionalität der getEntry() Methode.
	 */
	@Test
	public void getUndefinedEntry() {
		assertNull(addressBook.getEntry("Python", "Entwickler"));
	}
}
```

### Tipps zum Umgang mit JUnit (aus dem Übungsblatt)

JUnit ist ein Framework für Komponententests und basiert auf Java Annotations. JUnit ist in Eclipse integriert.

Ein typischer Aufbau einer Testklasse sieht wie folgt aus:

```java
public class Example {
    @Before
    public void setUp() { }

    @Test
    public void testcase1() {
        assertTrue(...);
    }

    @Test
    public void testcase2() { }

    @After
    public void tearDown() { }
}
```

Testfälle sind erfolgreich, wenn

- die mit `@Test` annotierte Methode komplett ausführt,
- keine assert Anweisung scheitert, und
- keine Exception geworfen wird.

Assertions sind in der Klasse `org.junit.Assert` definiert und haben folgende Struktur:

```text
assert(message, expected, actual)
```

Es stehen vielfältige Varianten der assert() Methode zur Verfügung:

- `assertEquals`
- `assertArrayEquals`
- `assertSame`
- `assertNotSame`
- `assertFalse`
- `assertTrue`
- `assertNull`
- `assertNonNull,fail` (so im Übungsblatt angegeben)
