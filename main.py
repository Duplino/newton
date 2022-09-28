import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import random
import importlib
import json

modules = []
statement= ""


#open config.json and load vasriable
config = json.load(open("config.json"))
wake_word = config["assistant"]["wake_word"]


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        r.pause_threshold = 1
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='es-es')
            print(f"user said:{statement}\n")
        except Exception as e:
            #speak("Pardon me, please say that again")
            return "None"
        return statement.lower()

   



def modules_help(statement):
    #dispaly table of modules
    print("Modules:")
    for module in modules:
        print(f"{module['name']} - {module['keywords']}")
    



def wikipedia_search(statement):
    print('Searching Wikipedia...')
    statement =statement.replace("wikipedia", "")
    results = wikipedia.summary(statement, sentences=3)
    speak("According to Wikipedia")
    speak(results)

def quit(stmt):
    exit()




def load_module(name, function, keywords):
    modules.append({"name":name,"function":function, "keywords": keywords})
load_module("modules_help", modules_help, ["ayuda", "módulos", "módulo", "módulos disponibles", "módulos disponibles"])
load_module("Search Wikipedia", wikipedia_search, ["wikipedia"])


#import all files in modules folder
for file in os.listdir("modules"):
    if file.endswith(".py"):
        module = importlib.import_module("modules." + file[:-3])
        load_module(module.name, module.call, module.keywords)
        module.speak = speak
        module.takeCommand = takeCommand
        module.quit = quit
        module.config = config
        continue





if __name__=='__main__':
    func = 0
    while True:
        statement = takeCommand()
        if wake_word not in statement:           
            continue
        statement =statement.split(wake_word,1)[1]
        for module in modules:
            for keyword in module["keywords"]:
                if keyword in statement:
                    module["function"](statement)
                    func = 1
                    break
        if func == 1:
            func = 0
            continue
        else:
            phrases = ["No entiendo lo que me estás diciendo", "No te entiendo", "No te entiendo, repite"]
            speak(random.choice(phrases))
            continue
        #hear constantly and paly noise as soon as wakeword is said


        
        if 'noticias' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

       # elif "camera" in statement or "take a photo" in statement:
        #    ec.capture(0,"robo camera","img.jpg")

        elif 'busca'  in statement:
            statement = statement.replace("busca", "")
            webbrowser.open_new_tab(statement)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)


        elif "repite" in statement or "repetí" in statement:
            statement =statement.replace("repite", "")
            statement =statement.replace("repetí", "")
            speak(statement)

        else:
            speak("No sé hacer lo que me pediste, si querés puedo buscarlo")
            ans = takeCommand()
            if 'si' in str(ans) or 'dale' in str(ans):
                webbrowser.open_new_tab(statement)
            else:
                continue