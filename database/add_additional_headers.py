from db_connection import DatabaseConnector
from sqlalchemy import text


def add_categories(engine):
    """
    Fügt neue Kategorien direkt in der Datenbank hinzu.
    """
    try:
        with engine.connect() as connection:
            # Temperaturkategorien hinzufügen
            print("Füge Temperaturkategorien hinzu...")
            connection.execute(text("""
                ALTER TABLE historical_forecast ADD COLUMN temp_category VARCHAR(10);
            """))
            connection.execute(text("""
                UPDATE historical_forecast
                SET temp_category = CASE
                    WHEN temperature_2m <= 0 THEN 'kalt'
                    WHEN temperature_2m > 0 AND temperature_2m <= 15 THEN 'mild'
                    ELSE 'heiß'
                END;
            """))
            connection.commit()  # WICHTIG: Commit für Forecast-Tabelle

            connection.execute(text("""
                ALTER TABLE historical_weather ADD COLUMN temp_category VARCHAR(10);
            """))
            connection.execute(text("""
                UPDATE historical_weather
                SET temp_category = CASE
                    WHEN temperature_2m <= 0 THEN 'kalt'
                    WHEN temperature_2m > 0 AND temperature_2m <= 15 THEN 'mild'
                    ELSE 'heiß'
                END;
            """))
            connection.commit()  # WICHTIG: Commit für Weather-Tabelle

            # Windkategorien hinzufügen
            print("Füge Windkategorien hinzu...")
            connection.execute(text("""
                ALTER TABLE historical_forecast ADD COLUMN wind_category VARCHAR(10);
            """))
            connection.execute(text("""
                UPDATE historical_forecast
                SET wind_category = CASE
                    WHEN wind_speed_10m <= 10 THEN 'schwach'
                    WHEN wind_speed_10m > 10 AND wind_speed_10m <= 30 THEN 'mäßig'
                    ELSE 'stark'
                END;
            """))
            connection.commit()

            connection.execute(text("""
                ALTER TABLE historical_weather ADD COLUMN wind_category VARCHAR(10);
            """))
            connection.execute(text("""
                UPDATE historical_weather
                SET wind_category = CASE
                    WHEN wind_speed_10m <= 10 THEN 'schwach'
                    WHEN wind_speed_10m > 10 AND wind_speed_10m <= 30 THEN 'mäßig'
                    ELSE 'stark'
                END;
            """))
            connection.commit()

            # Niederschlagskategorien hinzufügen
            print("Füge Niederschlagskategorien hinzu...")
            connection.execute(text("""
                ALTER TABLE historical_forecast ADD COLUMN rain_category VARCHAR(10);
            """))
            connection.execute(text("""
                UPDATE historical_forecast
                SET rain_category = CASE
                    WHEN precipitation <= 0.5 THEN 'trocken'
                    WHEN precipitation > 0.5 AND precipitation <= 5 THEN 'nass'
                    ELSE 'sehr nass'
                END;
            """))
            connection.commit()

            connection.execute(text("""
                ALTER TABLE historical_weather ADD COLUMN rain_category VARCHAR(10);
            """))
            connection.execute(text("""
                UPDATE historical_weather
                SET rain_category = CASE
                    WHEN precipitation <= 0.5 THEN 'trocken'
                    WHEN precipitation > 0.5 AND precipitation <= 5 THEN 'nass'
                    ELSE 'sehr nass'
                END;
            """))
            connection.commit()  # Commit für die letzte Kategorie

        print("Kategorien erfolgreich hinzugefügt!")

    except Exception as e:
        print(f"Fehler beim Hinzufügen der Kategorien: {e}")


def main():
    # Verbindung zur Datenbank herstellen
    db_connector = DatabaseConnector()
    engine = db_connector.get_engine()

    if engine is not None:
        try:
            add_categories(engine)
        except Exception as e:
            print(f"Fehler beim Hinzufügen der Kategorien: {e}")
    else:
        print("Verbindung zur Datenbank fehlgeschlagen.")


if __name__ == "__main__":
    main()
