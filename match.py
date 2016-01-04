import re
from urllib.parse import urlencode



def match(text, from_u, from_c):
    text = text.lower()
    replies = {
            'k': 'not k, ok! at least that :angry:',
            'hi': 'Hey there!',
            'yo': 'yeah?',
            'hey': 'Hey, what\'s up?',
            'bye': 'Goodbye :simple_smile:',
            'jk': 'You\'re joking?',
            'no': 'NOOO??',
            'faggot': 'stahp :cry:',
            'why?': 'because',
            'why?': 'because'
    }
    commands = {
            'current replies': str('```' + str(replies) + '```')
    }
    if from_u != 'U0HEZTKPX':
        if text.lower() in list(replies.keys()):
            return replies[text.lower()]
        elif text.lower() in list (commands.keys()):
            return commands[text.lower()]

        if len(re.findall('^no\sway\s(.*?)', text)) > 0:
            return str('yes way ' + re.findall('^no\sway\s(.+)', text)[0])
        elif len(re.findall('^google\s(.+)', text)) > 0:
            print(str(re.findall('^google\s(.+)', text)))
            return str('http://google.com/search?' + urlencode({'q': re.findall('^google\s(.+)', text)[0]}))
        elif len(re.findall('^please\ssay\s(.+)', text)) > 0:
            return re.findall('^please\ssay\s(.+)', text)[0]
        elif len(re.findall('.*boss.*', text)) > 0:
            return 'The boss? That\'s @therightman :sunglasses:'
        elif len(re.findall('^list\sactive\susers', text)) > 0:
            list_active()
