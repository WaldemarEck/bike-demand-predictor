import joblib
import pandas as pd
import sys
import os

# Pfad zum gespeicherten Modell
# Wir gehen von 'src' einen Ordner hoch (..) und dann in 'models'
MODEL_PATH = '../models/bike_predictor_rf.pkl'

def load_model():
    if not os.path.exists(MODEL_PATH):
        print(f"❌ FEHLER: Modelldatei nicht gefunden unter: {MODEL_PATH}")
        print("Bitte führe zuerst das Notebook '03_machine_learning' aus.")
        sys.exit(1)
        
    print("🔄 Lade Modell...")
    model = joblib.load(MODEL_PATH)
    return model

def predict():
    print("\n--- 🚲 Bike Demand AI Vorhersage ---")
    print("Bitte geben Sie die Wettersituation ein:")
    
    try:
        # Eingaben vom Benutzer abfragen
        hour = float(input("Uhrzeit (0-23): "))
        temp = float(input("Temperatur (°C): "))
        humidity = float(input("Luftfeuchtigkeit (%): "))
        wind = float(input("Windgeschwindigkeit (m/s): "))
        rain = float(input("Regen (mm) [0 für keinen]: "))
        
        # Statische Werte für Vereinfachung (könnte man auch abfragen)
        solar = 0.5 
        is_holiday = False
        is_functioning = True
        
        # DataFrame bauen (Muss exakt die gleichen Spalten wie beim Training haben!)
        # Die Reihenfolge ist wichtig.
        input_data = pd.DataFrame({
            'record_hour': [hour],
            'temperature': [temp],
            'humidity': [humidity],
            'wind_speed': [wind],
            'solar_radiation': [solar],
            'rainfall': [rain],
            'is_holiday': [is_holiday],
            'is_functioning_day': [is_functioning]
        })
        
        # Modell laden
        model = load_model()
        
        # Vorhersage machen
        prediction = model.predict(input_data)[0]
        
        print("-" * 40)
        print(f"🔮 KI-PROGNOSE: Wir benötigen ca. {int(prediction)} Fahrräder.")
        print("-" * 40)
        
    except ValueError:
        print("❌ Bitte geben Sie nur Zahlen ein (z.B. 12.5 statt 12,5)!")

if __name__ == "__main__":
    predict()