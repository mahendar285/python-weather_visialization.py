import requests
import matplotlib.pyplot as plt

API_KEY = "b2f27d89aadbfb761f94da8072e50eb3"   # Replace with your OpenWeatherMap API key
CITY    = "Hyderabad"           # You can change to any city
DAYS    = 5                     # Number of forecast days
UNITS   = "metric"              # Use 'imperial' for Fahrenheit

url = (
    f"http://api.openweathermap.org/data/2.5/forecast"
    f"?q={CITY}&cnt={DAYS * 8}&appid={API_KEY}&units={UNITS}"
)

resp = requests.get(url)
data = resp.json()

if resp.status_code != 200 or 'list' not in data:
    raise SystemExit(f"API error: {data.get('message', 'unknown')}")

times, temps, hums = [], [], []
for row in data['list']:
    times.append(row['dt_txt'])
    temps.append(row['main']['temp'])
    hums.append(row['main']['humidity'])

# Temperature Plot
plt.figure(figsize=(10, 4))
plt.plot(times, temps, marker='o', color='orange')
plt.title(f"{CITY} - {DAYS} Day Temperature Forecast")
plt.ylabel("Temperature (°C)" if UNITS == "metric" else "Temperature (°F)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Humidity Plot
plt.figure(figsize=(10, 4))
plt.plot(times, hums, marker='o', color='blue')
plt.title(f"{CITY} - {DAYS} Day Humidity Forecast")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
