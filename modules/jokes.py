import json
import requests
#access module in parent directory


name="Chistes"
descripion="Cuenta tus chistes favoritos"
keywords = ["chiste", "broma", "gracioso"]
def call(stmt):
    #request to https://v2.jokeapi.dev/joke/Any
    joke = requests.get("https://v2.jokeapi.dev/joke/Any?lang=es")
    joke = json.loads(joke.text)
    if joke["type"] == "twopart":
        speak(joke["setup"])
        speak(joke["delivery"])
    else:
        speak(joke["joke"])