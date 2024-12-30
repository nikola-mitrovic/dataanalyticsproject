class Config:
    # Basis-URLs
    BASE_URL_FORECAST = "https://api.open-meteo.com/v1/forecast"
    BASE_URL_HISTORICAL = "https://archive-api.open-meteo.com/v1/archive"
    BASE_URL_HISTORICAL_FORECAST = "https://historical-forecast-api.open-meteo.com/v1/forecast"

    # ---- Variablenlisten ----

    # Variablen für historische Wetterdaten
    HISTORICAL_VARIABLES = [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "rain",
        "snowfall",
        "snow_depth",
        "weather_code",
        "pressure_msl",
        "surface_pressure",
        "cloud_cover",
        "cloud_cover_low",
        "cloud_cover_mid",
        "cloud_cover_high",
        "wind_speed_10m",
        "wind_direction_10m",
        "wind_gusts_10m",
        "soil_temperature_0_to_7cm",
        "soil_moisture_0_to_7cm"
    ]

    # Variablen für historische Vorhersagen
    HISTORICAL_FORECAST_VARIABLES = [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "rain",
        "snowfall",
        "snow_depth",
        "weather_code",
        "pressure_msl",
        "surface_pressure",
        "cloud_cover",
        "cloud_cover_low",
        "cloud_cover_mid",
        "cloud_cover_high",
        "visibility",
        "wind_speed_10m",
        "wind_direction_10m",
        "wind_gusts_10m",
        "soil_temperature_0cm",
        "soil_moisture_0_to_1cm"
    ]

    # ---- Parameterkonfiguration ----

    # Parameter für historische Wetterdaten
    HISTORICAL_PARAMS = {
        "hourly": ",".join(HISTORICAL_VARIABLES),  # Variablenliste aus HISTORICAL_VARIABLES
        "timezone": "Europe/Zurich"
    }

    # Parameter für historische Vorhersagen
    HISTORICAL_FORECAST_PARAMS = {
        "hourly": ",".join(HISTORICAL_FORECAST_VARIABLES),  # Variablenliste aus HISTORICAL_FORECAST_VARIABLES
        "timezone": "Europe/Zurich"
    }

    # ---- Globale Einstellungen ----
    # Zeitzone
    TIMEZONE = "Europe/Zurich"

    # Standardkoordinaten (z.B. Zürich)
    DEFAULT_LATITUDE = 47.3769
    DEFAULT_LONGITUDE = 8.5417
