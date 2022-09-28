import random
name="Games"
descripion="Juegos"
keywords = ["moneda", "dado"]


def call(stmt):
    if "moneda" in stmt:
        if random.randint(0,1) == 0:
            speak("Cara")
        else:
            speak("Cruz")
    elif "dado" in stmt:
        #identyfy if theres a number in statement
        number = 6
        for i in stmt.split():
            if i.isdigit():
                number = int(i)
                break
        speak("El dado cayó en " + str(random.randint(1,number)))
    
