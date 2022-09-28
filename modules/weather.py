import requests

name="Weather"
descripion="Te dice el clima"
keywords = ["clima", "tiempo", "tiempo en", "clima en"]

def call(stmt):
    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("Diga el nombre de la ciudad")
    city_name=takeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" La temperatura en Kelvin es de " +
                str(current_temperature) +
                "\n La humedad en porcentaje es de " +
                str(current_humidiy) +
                "\n Descripción del clima  " +
                str(weather_description))

    else:
        speak(" Ciudad no encontrada ")