#!/usr/bin/env python
# coding: utf-8

# In[20]:


import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
num = int(input("Enter page number you want combine from multiple documents "))
pdf1 = open('birds.pdf', 'rb')
pdf2 = open('birdspic.pdf', 'rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1) 
page = pdf1_reader.pages[num - 1]
pdf_writer.add_page(page)
pdf2_reader = PdfReader(pdf2) 
page = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page)
with open('output.pdf', 'wb') as output:
   pdf_writer.write(output)





import json

def fetch_weather_data_from_json(file_path):
    try:
        with open(file_path, "r") as json_file:
            weather_data = json.load(json_file)
            return weather_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in the file: {file_path}")
    except Exception as e:
        print(f"Error occurred while reading the JSON file: {e}")
    return None

if __name__ == "__main__":
    file_path = "/content/drive/MyDrive/weather.json"
    weather = fetch_weather_data_from_json(file_path)

    if weather:
        print("Current Weather Data:")
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['conditions']}")
    else:
        print("Failed to fetch weather data from the JSON file.")


# In[21]:


{
 "coord": {
 "lon": 
-73.99
,
 "lat": 40.73
 },
 "weather": [
 
{
 "id": 800
,
 "main": "Clear"
,
 "description": "clear sky"
,
 "icon": "01d"
 
}
 ],
 "base": "stations"
,
 "main": {
 "temp": 15.45
,
 "feels_like": 12.74
,
 "temp_min": 14.44
,
 "temp_max": 16.11
,
 "pressure": 1017
,
 "humidity": 64
 },
 "visibility": 10000
,
 "wind": {
 "speed": 4.63
,
 "deg": 180
 },
 "clouds": {
 "all": 
1
 },
 "dt": 1617979985
,
 "sys": {
 "type": 
1
,
 "id": 5141
,
 "country": "US"
,
 "sunrise": 1617951158
,
 "sunset": 1618000213
 },
 "timezone": 
-14400
,
 "id": 5128581
,
 "name": "New York"
,
 "cod": 200 }


# In[ ]:




