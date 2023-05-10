import requests
import pyttsx3
engine = pyttsx3.init();

def weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    engine.say("Where would you like the weather of?");
    engine.runAndWait();
    city = input('City Name :')
    url = api_address + city
    json_data = requests.get(url).json()

    descript = json_data['weather'][0]["description"]

    temp_max = json_data['main']["temp_max"]
    temp_max= (temp_max - 273.15)*(9/5)+32
    temp_max = round(temp_max,2)
    temp_max = str(temp_max)+"F"

    temp_min = json_data['main']["temp_min"]
    temp_min= (temp_min - 273.15)*(9/5)+32
    temp_min = round(temp_min,2)
    temp_min = str(temp_min)+"F"

    current_temp = json_data['main']["temp"]
    current_temp= (current_temp - 273.15)*(9/5)+32
    current_temp = round(current_temp,2)
    current_temp = str(current_temp)+"F"

    pressure = json_data['main']["pressure"]
    pressure = str(pressure)

    humidity = json_data['main']["humidity"]
    humidity = str(humidity) + "%"

    output= "Description: " + descript + " - Max temp: " + temp_max + " - Min temp: " + temp_min + "- Current temp: " + current_temp + "- Pressure: " + pressure + "- Humidity:" + humidity 

    format_add1 = json_data['main']

    #print(format_add)
    print(output)
    engine.say(output);
    engine.runAndWait();