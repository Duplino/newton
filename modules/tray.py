import sys
name="Tray"
descripion="Agrega a Newton a la barra de tareas"
keywords = []
def call(stmt):
    pass
from pystray import Icon as icon, Menu as menu, MenuItem as item
import PIL.Image as Image
import json
config = json.load(open("./config.json"))

#open image file
image = Image.open("icon.jpg")
# add text element to image
icon = icon("Newton", image, "Newton", menu(
    item("Salir", quit),
    #show version with text item
    item("Version "+config["assistant"]["version"], lambda: None, enabled=False)
)).run_detached()

