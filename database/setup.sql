-- setup.sql - Setup-Skript für die MySQL-Datenbank

-- 1. Erstelle die Datenbank
CREATE DATABASE IF NOT EXISTS weather_data;

-- 2. Benutzer erstellen (falls noch nicht vorhanden)
CREATE USER IF NOT EXISTS 'weather_user'@'localhost' IDENTIFIED BY 'password123';

-- 3. Rechte für den Benutzer auf die Datenbank vergeben
GRANT ALL PRIVILEGES ON weather_data.* TO 'weather_user'@'localhost';

-- 4. Änderungen anwenden
FLUSH PRIVILEGES;

-- Hinweis: Führe dieses Skript aus, indem du es im MySQL-Terminal lädst:
-- mysql -u root -p < setup.sql