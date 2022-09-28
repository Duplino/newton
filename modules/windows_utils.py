import os

name="Windows Utils"
descripion="Basic Utils"
keywords = ["cerrar sesión", "bloquear"]

def call(stmt):
    if "cerrar sesión" in stmt:
        os.system("shutdown -l")
    elif "bloquear" in stmt:
        os.system("rundll32.exe user32.dll, LockWorkStation")