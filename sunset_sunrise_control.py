import requests
from datetime import datetime
import pytz

LATITUDE = 33.5779
LONGITUDE = -101.8552
CENTRAL_TZ = pytz.timezone("America/Chicago")

class SunriseSunsetController:
    def __init__(self):
        self.sunrise_time = None
        self.sunset_time = None
        self.last_update = None
        self.fetch_sun_times()

    def fetch_sun_times(self):
        url = f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&formatted=0"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            sunrise_utc = datetime.fromisoformat(data['results']['sunrise']).replace(tzinfo=pytz.utc)
            sunset_utc = datetime.fromisoformat(data['results']['sunset']).replace(tzinfo=pytz.utc)

            self.sunrise_time = sunrise_utc.astimezone(CENTRAL_TZ)
            self.sunset_time = sunset_utc.astimezone(CENTRAL_TZ)
            self.last_update = datetime.now()

            print(f"[SUNRISE-SUNSET] Sunrise: {self.sunrise_time.strftime('%I:%M:%S %p')}, Sunset: {self.sunset_time.strftime('%I:%M:%S %p')}")

        except requests.exceptions.RequestException as e:
            print(f"[SUNRISE-SUNSET] Error fetching data: {e}")

    def needs_update(self):
        if self.last_update is None:
            return True
        return datetime.now().date() > self.last_update.date()

    def check_sun_times(self):
        now = datetime.now(CENTRAL_TZ)
        if self.sunrise_time and (now >= self.sunrise_time) and (now < self.sunset_time):
            return "open"
        elif self.sunset_time and now >= self.sunset_time:
            return "close"
        return "no_change"
