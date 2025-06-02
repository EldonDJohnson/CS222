import json
import ssl
from urllib.request import urlopen

def main():
    url = "https://api.weather.gov/points/40.1934,-85.3864" + "IN"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())

    for event in weatherData["properties"]:
        url = "https://api.weather.gov/gridpoints/IND/83,90/forecast"
        context = ssl._create_unverified_context()
        response = urlopen(url, context=context)
        forcastData = json.loads(response.read())
        
        for event in forcastData["periods"]:
            print(event["name"]["temperature"]["detailedForcast"])

main()