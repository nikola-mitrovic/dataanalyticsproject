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

    @staticmethod
    def add_temperature_category(df):
        """
        Kategorisiert die Temperatur in 'kalt', 'warm' und 'heiß'.
        """
        def categorize_temp(temp):
            if pd.isna(temp):
                return "unbekannt"
            elif temp < 10:
                return 'kalt'
            elif 10 <= temp < 25:
                return 'warm'
            else:
                return 'heiß'

        df['enriched_temp_category'] = df['temperature_2m'].apply(categorize_temp)
        return df

    @staticmethod
    def add_precipitation_category(df):
        """
        Kategorisiert den Niederschlag in 'trocken', 'leicht', 'mäßig' und 'stark'.
        """
        def categorize_precipitation(precip):
            if pd.isna(precip):
                return "unbekannt"
            elif precip == 0:
                return 'trocken'
            elif 0 < precip < 5:
                return 'leicht'
            elif 5 <= precip < 20:
                return 'mäßig'
            else:
                return 'stark'

        df['enriched_precipitation_category'] = df['precipitation'].apply(categorize_precipitation)
        return df
