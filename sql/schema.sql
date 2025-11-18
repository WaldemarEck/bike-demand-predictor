CREATE DATABASE IF NOT EXISTS bike_db;
USE bike_db;

-- 1. Wetterdaten (Metadaten)
CREATE TABLE weather_data (
    record_date DATE NOT NULL,
    record_hour INT NOT NULL,
    temperature DECIMAL(4,1),
    humidity INT,
    wind_speed DECIMAL(4,1),
    visibility INT,
    solar_radiation DECIMAL(4,2),
    rainfall DECIMAL(4,1),
    snowfall DECIMAL(4,1),
    seasons VARCHAR(20),
    is_holiday BOOLEAN,
    is_functioning_day BOOLEAN,
    PRIMARY KEY (record_date, record_hour)
);

-- 2. Ausleihen (Bewegungsdaten)
CREATE TABLE rentals (
    record_date DATE NOT NULL,
    record_hour INT NOT NULL,
    bike_count INT,
    PRIMARY KEY (record_date, record_hour),
    FOREIGN KEY (record_date, record_hour) 
        REFERENCES weather_data(record_date, record_hour)
        ON DELETE CASCADE
);