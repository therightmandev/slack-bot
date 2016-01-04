import requests, json, websocket, time
from datetime import datetime
from os import system


token = ""

replies = {'hey': 'hi!',
            '!membersheet': ':fast_forward: http://bit.ly/1R5tvN3 :rewind:\nI hope I was the fastest!',
            '!projects': 'I\'ll add it in a second, jeez!'
}

def get_dict(tkn):
    r = requests.get("https://slack.com/api/rtm.start", params={'token': tkn})
    jsn_dict = json.loads(r.content.decode())
    with open("cont.txt", 'w') as f:
        f.write(r.content.decode())
    return jsn_dict

team_dict = get_dict(token)

def send_msg(sock, msg, channel_id='C0H0SR40J'):
    template = {
        "type": "message",
        "channel": channel_id,
        "text": msg
    }

    sock.send(json.dumps(template))

def get_channel_id(name, channels=team_dict['channels']):
    for x in range(len(channels)):
        channel = channels[x]
        if channel['name'] == name:
            return channel['id']

def get_channel_name(ident, channels=team_dict['channels']):
    for channel in channels:
        if channel['id'] == ident:
            return channel['name']
    return 'UNIDENTIFIED CHANNEL'

def get_username(ident, users=team_dict['users']):
    for user in users:
        if user['id'] == ident:
            return user['name']
    return 'UNIDENTIFIED'

def get_user_id(name, users=team_dict['users']):
    for user in users:
        if user['name'] == name:
            return user['id']
    return 'UNIDENTIFIED'

def determine_type(res_dict):

    keys = list(res_dict.keys())

    if res_dict is None:
        pass
    elif 'type' in keys:
        if res_dict['type'] == 'message':
            if 'subtype' in keys:
                if res_dict['subtype'] == 'bot_message':
                    print("#" + get_channel_name(res_dict['channel']).upper(),"__BOT__ - ", res_dict['username'], "=>", res_dict['text'])
                elif res_dict['subtype'] == 'channel_leave':
                    print("xxxxxxxxxx " + get_username(res_dict['user']) + " left " + "#" + get_channel_name(res_dict['channel']).upper() + " xxxxxxxxxx")
                elif res_dict['subtype'] == 'channel_join':
                    print("++++++++++ " + get_username(res_dict['user']) + " joined " + "#" + get_channel_name(res_dict['channel']))
                elif res_dict['subtype'] == 'message_deleted':
                    print("#" + get_channel_name(res_dict['channel']) + " xxDELETEDxx from " + get_username(res_dict['previous_message']['user']) + ":\n" + res_dict['previous_message']['text'])
                else:
                    print(res_dict)
            elif 'user' in keys:
                print("#" + get_channel_name(res_dict['channel']).upper() + "  -  " + get_username(res_dict['user']), "=>", res_dict['text'].encode('utf-8'))
            else:
                print(res_dict)

            if 'text' in keys:
                if res_dict['text'] in list(replies.keys()):
                    return replies[res_dict['text']], res_dict['channel'] #return answer and the channel

        elif res_dict['type'] == 'user_typing':
            print("#" + get_channel_name(res_dict['channel']).upper()," - ", get_username(res_dict['user']), "is typing...")

        elif res_dict['type'] == 'presence_change':
            if res_dict['presence'] == 'active':
                print("-----------", get_username(res_dict['user']), "is ONline ----------")
            elif res_dict['presence'] == 'away':
                print("-----------", get_username(res_dict['user']), "is OFFline ----------")
            else:
                print(res_dict)

        elif res_dict['type'] == 'error':
            print(res_dict['error'])

        elif res_dict['type'] == 'hello':
            print("Connected")

        elif res_dict['type'] == 'reconnect_url':
            print("*new url*")

        else:
            print(res_dict)
    elif ['reply_to'] in keys:
        print("#" + get_channel_name(res_dict['channel']) + "Reply to " + res_dict['reply_to'] + ": " + res_dict['text'])


def parse_res(res):
    res_dict = json.loads(res)
    return determine_type(res_dict)

def main():

    while 1:
        try:
            system("cls")

            gen_url = team_dict['url']

            ws = websocket.WebSocket()
            ws.connect(gen_url)


            while 1:
                response = ws.recv()
                try:
                    reply, chnnl = parse_res(response)
                except:
                    reply = parse_res(response)
                if reply is not None:
                    send_msg(ws, reply, channel_id=chnnl)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break


if __name__ == "__main__":
    main()
