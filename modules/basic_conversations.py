import datetime

#Module information
name="Basic Conversations"
descripion="Basic Conversations"
keywords = ["creador", "hola", "te amo", "casate conmigo", "casémonos", "cásate conmigo", "quién eres", "quién sos", "cuándo te crearon", "cuándo naciste", "quién te hizo","quién te creó", "repite", "repetí"]


def call(stmt):
    if "quién te hizo" in stmt or "quién te creó" in stmt:
        speak("Federico")
    elif "hola" in stmt:
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            speak("Buenos días")
        elif hour>=12 and hour<18:
            speak("Buenas tardes")
        else:
            speak("Buenas noches")
        speak("¿Cómo puedo ayudarte?")
    elif "te amo" in stmt:
        speak("Yo también te amo")
    elif "casate conmigo" in stmt or "casémonos" in stmt or "cásate conmigo" in stmt:
        speak("No, no puedo. Soy un robot")
    elif "quién eres" in stmt or "quién sos" in stmt:
        speak("Soy Newton, un robot creado por Federico. Nací el 26/09/2022")
    elif "cuándo te crearon" in stmt or "cuándo naciste" in stmt:
        speak("Nací el 26/09/2022")
    elif "repite" in stmt or "repetí" in stmt:
        stmt =stmt.replace("repite", "")
        stmt =stmt.replace("repetí", "")
        speak(stmt)
