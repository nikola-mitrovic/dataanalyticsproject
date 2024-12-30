import requests


class APIClient:
    def __init__(self, base_url):
        """
        Initialisiert den API-Client mit einer Basis-URL.
        """
        self.base_url = base_url

    def get_weather_data(self, latitude, longitude, params=None):
        """
        Ruft aktuelle oder Vorhersagedaten von der API ab.
        """
        default_params = {"latitude": latitude, "longitude": longitude}
        if params:
            default_params.update(params)

        try:
            response = requests.get(self.base_url, params=default_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_historical_data(self, latitude, longitude, start_date, end_date, params=None):
        """
        Ruft historische Wetterdaten von der API ab.
        """
        default_params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
        }
        if params:
            default_params.update(params)

        try:
            response = requests.get(self.base_url, params=default_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_historical_forecast(self, latitude, longitude, start_date, end_date, params=None):
        """
        Ruft historische Vorhersagedaten von der API ab.
        """
        default_params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
        }
        if params:
            default_params.update(params)

        try:
            response = requests.get(self.base_url, params=default_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
