import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv  # Neu

# Lädt das Passwort aus der .env Datei
load_dotenv()

# --- KONFIGURATION ---
DB_USER = 'root'
# Hier holen wir das Passwort sicher:
DB_PASS = os.getenv('DB_PASS')  
DB_HOST = 'localhost'
DB_NAME = 'bike_db'

def process_data():
    print("🔄 Start: Lade CSV-Datei...")
    # Wir gehen einen Ordner hoch (..) und dann in data
    csv_path = '../data/SeoulBikeData.csv'
    
    # Encoding 'unicode_escape' ist nötig für dieses spezielle Dataset
    df = pd.read_csv(csv_path, encoding='unicode_escape')

    # 1. Spalten umbenennen (Clean Code!)
    column_mapping = {
        'Date': 'record_date',
        'Rented Bike Count': 'bike_count',
        'Hour': 'record_hour',
        'Temperature(°C)': 'temperature',
        'Humidity(%)': 'humidity',
        'Wind speed (m/s)': 'wind_speed',
        'Visibility (10m)': 'visibility',
        'Solar Radiation (MJ/m2)': 'solar_radiation',
        'Rainfall(mm)': 'rainfall',
        'Snowfall (cm)': 'snowfall',
        'Seasons': 'seasons',
        'Holiday': 'holiday_str',
        'Functioning Day': 'func_day_str'
    }
    df = df.rename(columns=column_mapping)
    
    # 2. Datenformate anpassen
    print("⚙️  Transformiere Daten...")
    df['record_date'] = pd.to_datetime(df['record_date'], format='%d/%m/%Y').dt.date
    df['is_holiday'] = df['holiday_str'] == 'Holiday'
    df['is_functioning_day'] = df['func_day_str'] == 'Yes'

    # 3. Datenbank-Verbindung
    print("🔌 Verbinde mit MySQL...")
    connection_str = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(connection_str)

    # 4. Daten aufteilen (Normalisierung)
    weather_cols = ['record_date', 'record_hour', 'temperature', 'humidity', 
                    'wind_speed', 'visibility', 'solar_radiation', 'rainfall', 
                    'snowfall', 'seasons', 'is_holiday', 'is_functioning_day']
    
    rentals_cols = ['record_date', 'record_hour', 'bike_count']

    print("💾 Speichere in Tabellen (das dauert kurz)...")
    try:
        df[weather_cols].to_sql('weather_data', con=engine, if_exists='append', index=False)
        df[rentals_cols].to_sql('rentals', con=engine, if_exists='append', index=False)
        print("✅ ERFOLG: Alle Daten sind in der Datenbank!")
    except Exception as e:
        print(f"❌ FEHLER: {e}")

if __name__ == "__main__":
    process_data()