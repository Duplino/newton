import datetime
name="Fecha y hora"
descripion="herramientas de fecha y hora"
keywords = ["fecha", "hora", "día"]

def call(stmt):
    if "hora" in stmt:
        speak("Son las " + str(datetime.datetime.now().strftime("%H:%M")))
    elif "día" in stmt or "fecha" in stmt:
        speak("Hoy es " + str(datetime.datetime.now().strftime("%A %d/%m/%Y")))