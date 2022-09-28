import pyautogui

name="Media Controls"
descripion="Controla tu música"
keywords = ["play", "pausa", "reproducir", "parar","siguiente", "anterior", "volumen"]

def call(stmt):
    if "play" in stmt or "reproducir" in stmt:
        pyautogui.press("playpause")
    elif "pausa" in stmt or "parar" in stmt:
        pyautogui.press("playpause")
    elif "siguiente" in stmt:
        pyautogui.press("nexttrack")
    elif "anterior" in stmt:
        pyautogui.press("prevtrack")
    elif "volumen" in stmt:
        if "subir" in stmt:
            pyautogui.press("volumeup")
        elif "bajar" in stmt:
            pyautogui.press("volumedown")
        elif "silencio" in stmt:
            pyautogui.press("volumemute")