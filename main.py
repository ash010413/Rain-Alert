import requests
from twilio.rest import Client

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC8737f19bd0088f3cc31382c6e7a8f371"
auth_token = "5948825bc403b73bf66617821ef9abd5"
parameters = {
    "lat": 10.087500,
    "lon": 77.061699,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()

data = response.json()

all_weather_codes = []

for i in range(12):
    all_weather_codes.append(data['hourly'][i]['weather'][0]['id'])
print(all_weather_codes)

will_rain = False

for ele in all_weather_codes:
    if ele < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, take an umbrella with you!☔️",
        from_='+13475146325',
        to='+917506604473'
    )
print(message.status)