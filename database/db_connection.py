import os
import json
from sqlalchemy import create_engine


class DatabaseConnector:
    def __init__(self, config_file="db_config.json"):
        """
        Initialisiert die Datenbankverbindung basierend auf einer Konfigurationsdatei.
        """
        # Pfad zur JSON-Konfigurationsdatei
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, config_file)

        # Konfiguration aus JSON-Datei lesen
        with open(config_path, 'r') as file:
            config = json.load(file)

        self.host = config['host']
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']

        # SQLAlchemy Engine vorbereiten
        self.engine = None

    def get_engine(self):
        """
        Erstellt und gibt eine SQLAlchemy-Engine zurück.
        """
        if self.engine is None:  # Engine nur einmal erstellen!
            connection_string = (
                f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}"
            )
            self.engine = create_engine(connection_string, echo=False)  # Kein zusätzlicher Output
        return self.engine


# Test der Verbindung
if __name__ == "__main__":
    db_connector = DatabaseConnector()
    engine = db_connector.get_engine()  # Test Engine
    print("SQLAlchemy Engine erfolgreich erstellt!")
