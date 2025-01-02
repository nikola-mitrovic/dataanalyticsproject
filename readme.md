# Weather Data Analytics Project

## Projektübersicht

Dieses Projekt analysiert Wetterdaten, die von einer API abgerufen und in einer MySQL-Datenbank gespeichert werden. Es umfasst folgende Funktionen:

1. **Abrufen von Wetterdaten** (historische Wetterdaten und Vorhersagen).
2. **Speichern der Daten in CSV-Dateien**.
3. **Erstellen und Verwalten einer MySQL-Datenbank**.
4. **Importieren der Daten in die Datenbank**.
5. **Analysen und Modelle in Jupyter Notebooks**.

---

## Setup der Umgebung

### 0. Vorbereitung der Python-Umgebung

1. Virtual Environment erstellen:
   ```bash
   python -m venv venv
   ```
2. Aktivieren:
   ```bash
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -e .
   ```

---

## Setup der Datenbank

### 1. Datenbank erstellen und Benutzer konfigurieren

1. Öffne das MySQL-Terminal:
   ```bash
   mysql -u root -p
   ```
2. Lade und führe das SQL-Setup-Skript aus:
   ```bash
   mysql -u root -p < setup.sql
   ```

---

### 2. Tabellen erstellen

1. Führe das Skript zum testen der DB Verbindung aus:
   ```bash
   python database/db_connection.py
   ```
2. Führe das Skript zum Erstellen der Tabellen aus:
   ```bash
   python database/create_tables.py
   ```

---

## Datenabruf und Speicherung

### 3. Daten aus der API abrufen und speichern

1. Starte den Datenabruf und erstelle CSV-Dateien:
   ```bash
   python scripts/fetch_data.py
   ```

---

## Datenimport in die Datenbank

### 4. Daten in die Datenbank importieren

1. Nutze ein separates Skript (z.B. `import_data.py`) zum Import der Daten.
   ```bash
   python database/import_data.py
   ```

---

## Weitere Schritte

- **Analysen in Jupyter Notebooks:** Visualisierung, EDA, Modellierung.
- **Dokumentation und Präsentation:** Modelle und Ergebnisse beschreiben.

---

## Anforderungen

- Python 3.12+
- MySQL 8.0+
- Abhängigkeiten aus `setup.py`.

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.

