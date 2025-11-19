import streamlit as st
import pandas as pd
import joblib
import os

# --- 1. Konfiguration & Titel ---
st.set_page_config(page_title="Bike Demand Predictor", page_icon="🚲")

st.title("🚲 Seoul Bike Demand Predictor")
st.write("Dieses Dashboard nutzt Machine Learning, um die Nachfrage nach Leihfahrrädern vorherzusagen.")

# --- 2. Modell laden ---
@st.cache_resource
def load_model():
    # Wir bauen den Pfad dynamisch, damit es immer funktioniert
    model_path = os.path.join(os.path.dirname(__file__), '../models/bike_predictor_rf.pkl')
    return joblib.load(model_path)

try:
    model = load_model()
except Exception as e:
    st.error(f"Fehler beim Laden des Modells: {e}")
    st.stop()

# --- 3. Sidebar für Eingaben (Die Schieberegler) ---
st.sidebar.header("🌤️ Wetter-Bedingungen")

hour = st.sidebar.slider("Uhrzeit (Stunde)", 0, 23, 12)
temp = st.sidebar.slider("Temperatur (°C)", -20.0, 40.0, 20.0)
humidity = st.sidebar.slider("Luftfeuchtigkeit (%)", 0, 100, 50)
wind = st.sidebar.slider("Windgeschwindigkeit (m/s)", 0.0, 10.0, 1.5)
rain = st.sidebar.number_input("Regen (mm)", 0.0, 50.0, 0.0)

# --- Interaktive Checkboxen ---
is_holiday = st.sidebar.checkbox("Ist heute Feiertag?")

# Der "Kill-Switch": Wenn der Verleih zu ist, muss die Zahl 0 sein
is_open = st.sidebar.checkbox("Ist der Verleih geöffnet?", value=True)
is_functioning = is_open  # True oder False

# Statische Werte
solar = 0.5


# --- 4. Vorhersage ---
# DataFrame bauen (Exakt wie beim Training!)
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

if st.button("🔮 Vorhersage berechnen"):
    prediction = model.predict(input_data)[0]
    prediction = int(round(prediction))
    
    # Ergebnis anzeigen
    st.success(f"Benötigte Fahrräder: **{prediction}**")
    
    # Ein kleiner visueller Balken zur Einordnung
    st.progress(min(prediction / 3500, 1.0)) # 3500 ist ca das Maximum im Dataset
    
    if prediction > 2000:
        st.warning("⚠️ Achtung: Sehr hohe Nachfrage erwartet!")
    elif prediction < 100:
        st.info("ℹ️ Geringe Nachfrage.")