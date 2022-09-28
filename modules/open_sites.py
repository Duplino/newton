import webbrowser

name="Open Sites"
descripion="Opens your favoirite sites"
keywords = ["abrir", "abre"]

def call(stmt):
    sites = {
        "youtube": "youtube.com",
        "google": "google.com",
        "facebook": "facebook.com",
        "instagram": "instagram.com",
        "twitter": "twitter.com",
        "whatsapp": "web.whatsapp.com",
        "gmail": "mail.google.com",
        "reddit": "reddit.com",
        "github": "github.com",
        "stackoverflow": "stackoverflow.com",
        "linkedin": "linkedin.com"
        }
    for key, value in sites.items():
        if key in stmt:
            webbrowser.open(value)
            speak("Abriendo " + key)
            break