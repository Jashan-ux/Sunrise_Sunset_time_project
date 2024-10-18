import requests
from datetime import datetime, timedelta
import pytz

MY_LAT = 30.670067
MY_LONG = 76.664383
Specific_date = f"2024-10-{(datetime.now().day)+1}"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": Specific_date, 
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()


sunrise_utc = data["results"]["sunrise"]
sunset_utc = data["results"]["sunset"]


sunrise_time_utc = datetime.strptime(sunrise_utc, '%I:%M:%S %p')
sunset_time_utc = datetime.strptime(sunset_utc, '%I:%M:%S %p')


today = datetime.now(pytz.timezone('Asia/Kolkata'))


sunrise_time_utc = sunrise_time_utc.replace(year=today.year, month=today.month, day=today.day+1)
sunset_time_utc = sunset_time_utc.replace(year=today.year, month=today.month, day=today.day+1)

ist_timezone = pytz.timezone('Asia/Kolkata')


sunrise_time_ist = pytz.utc.localize(sunrise_time_utc).astimezone(ist_timezone)
sunset_time_ist = pytz.utc.localize(sunset_time_utc).astimezone(ist_timezone)


print("Sunrise (IST):", sunrise_time_ist.strftime('%Y-%m-%d %H:%M:%S'))
print("Sunset (IST):", sunset_time_ist.strftime('%Y-%m-%d %I:%M:%S'))
