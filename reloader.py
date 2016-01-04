from importlib import reload
import match

def reloader(text):
    if text.lower() == 'reload match':
        reload(match)
        return 'Reloaded Match'
