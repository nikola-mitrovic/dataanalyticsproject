from db_connection import DatabaseConnector
from create_tables import create_tables
from insert_data import load_and_insert_data
from add_additional_headers import add_categories
from sqlalchemy import text


def drop_tables(engine):
    """
    Dropt vorhandene Tabellen, um die Datenbank neu zu initialisieren.
    """
    try:
        with engine.connect() as connection:
            print("Dropping Tabellen...")
            connection.execute(text("DROP TABLE IF EXISTS historical_forecast;"))
            connection.execute(text("DROP TABLE IF EXISTS historical_weather;"))
            print("Tabellen erfolgreich gelöscht!")
    except Exception as e:
        print(f"Fehler beim Droppen der Tabellen: {e}")


def main():
    """
    Führt alle Schritte zur Datenbankinitialisierung und -befüllung aus.
    """
    print("### Starte die gesamte Datenbankinitialisierung ###")

    # Verbindung zur Datenbank herstellen
    db_connector = DatabaseConnector()
    engine = db_connector.get_engine()

    # 1. Tabellen löschen (Drop Tables)
    drop_tables(engine)

    # 2. Tabellen erstellen
    create_tables()

    # 3. Daten einfügen
    load_and_insert_data(engine)

    # 4. Zusätzliche Kategorien hinzufügen
    add_categories(engine)

    print("### Datenbankinitialisierung abgeschlossen ###")


if __name__ == "__main__":
    main()
