import requests
#import os
from datetime import datetime

api_key = 'e215904d33e7bbb626771e53fb33f567'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

a="-------------------------------------------------------------\n"
b="Weather Stats for - {}  || {}\n".format(location.upper(), date_time)
c="-------------------------------------------------------------\n"

d="Current temperature   : {:.2f} deg C\n".format(temp_city)
e="Current weather desc  :"+weather_desc+"\n"
f="Current Humidity      :"+str(hmdt)+"%\n"
g="Current wind speed    :"+str(wind_spd)+" kmph\n"

file=open("weather.txt","w+")
file.write(a+b+c+d+e+f+g)
file.close()