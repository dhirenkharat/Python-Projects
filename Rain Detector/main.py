import requests
from twilio.rest import Client
import os

# api_key="f1a333e3185c668e680dfd96da976947"
ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
API_KEY="69f04e4613056b159c2761a9d9e664d2"

account_sid = "AC57bc1d5d37d576fede0cf15bfe1c6b29"
auth_token = "4d59bb898885a31e67f1ebef37f01954"

parameter={
    "lat":18.520430,
    "lon":73.856743,
    "exclude":"current,daily,minutely",
    "appid": API_KEY,

}


response = requests.get(url=ENDPOINT,params=parameter)
response.raise_for_status()
weather_data = response.json()



# print(weather_data)
# print(weather_data["hourly"][0]["weather"][0]["id"])
flag=0
for i in range(0,12):
    if weather_data["hourly"][i]["weather"][0]["id"]<700:
        flag=1
    else:
        flag=0



if flag==1:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring umbrella",
        from_='+18314806573',
        to='+918605389923'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Dont Bring umbrella",
        from_='+18314806573',
        to='+918605389923'
    )