import requests
import smtplib


MY_EMAIL = 'day32.0001@gmail.com'
MY_PASSWORD = 'wgnavynehmlbghzu'
TO_EMAIL = 'muhammad.mamleev1998@gmail.com'
MESSAGE = f'Subject:RAIN ALERT!\n\nIt is going to rain today. Bring an umbrella with you.☔'.encode('utf-8')

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": "54.771648",
    "lon": "56.026932",
    "appid": 'cb9e33fa5bb64bb673aab90c5b4921f5',
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# weather_id = weather_data['list'][0]['weather'][0]['id']
weather_slice = weather_data['list'][:4]
# print(weather_slice)


will_rain = False

for hour_data in weather_slice:
    condition = hour_data['weather'][0]['id']
    if condition < 700:
        will_rain = True

if will_rain:
    print('Bring an Umbrella')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=MESSAGE,
        )
else:
    print('NO Rain')
