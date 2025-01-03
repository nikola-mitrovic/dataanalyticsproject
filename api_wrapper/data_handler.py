import pandas as pd


class DataHandler:
    @staticmethod
    def save_to_csv(data, filename):
        """
        Speichert die Daten in einer CSV-Datei.
        """
        if isinstance(data, pd.DataFrame):
            data.to_csv(filename, index=False)
            print(f"Datei {filename} wurde erfolgreich gespeichert.")
        else:
            raise ValueError("Ungültiges Datenformat. Erwartet DataFrame.")

    @staticmethod
    def clean_data(df):
        """
        Entfernt fehlende Werte und Duplikate.
        """
        # Fehlende Werte entfernen (nur Zeilen mit komplett fehlenden Werten)
        df = df.dropna(how="all")

        # Duplikate anhand des Zeitstempels entfernen
        if 'datetime' in df.columns:
            df = df.drop_duplicates(subset=['datetime'])

        return df

    @staticmethod
    def handle_missing_values(df):
        """
        Behandelt fehlende Werte, indem diese explizit als NaN markiert werden.
        """
        print("Fehlende Werte werden behandelt...")  # Logging zur Kontrolle
        # Fehlende Werte explizit auf NaN setzen
        df = df.fillna(pd.NA)  
        return df