import requests, json, websocket
from os import system
from parse_res import Parse

def get_url(tkn):
    r = requests.get("https://slack.com/api/rtm.start", params={'token': tkn})
    jsn_dict = json.loads(r.content.decode())
    with open("cont.txt", 'w') as f:
        f.write(r.content.decode())
    return jsn_dict['url']


def main():

    with open('token.txt', 'r') as t:
        TOKEN = t.readlines()[0]

    parse = Parse()

    system("cls")

    while 1:

        gen_url = get_url(TOKEN)

        ws = websocket.WebSocket()
        ws.connect(gen_url)

        while 1:
            response = ws.recv()
            parse.parse(response)

if __name__ == '__main__':
    main()
