import requests as r
import json

class Api_Requests:
    def __init__(self, token):
        self.main_link = 'https://slack.com/api/'
        self.TOKEN = token


    def send_msg(self, text, channel_id, as_user='true', username='still_learning'):
        if as_user: res = r.get(self.main_link + 'chat.postMessage', params={'token': self.TOKEN, 'text': text, 'channel': channel_id, 'as_user': as_user})
        elif not as_user: res = r.get(self.main_link + 'chat.postMessage', params={'token': self.TOKEN, 'text': text, 'channel': channel_id, 'as_user': as_user, 'username': username})
        return res


    def get_user_dict(self):
        res = r.get(self.main_link + 'users.list', params={'token': self.TOKEN, 'presence': '0'})
        res_dict = json.loads(res.content.decode())
        user_dict = {}
        for user in res_dict['members']:
            user_dict[user['name']] = user['id']
        return user_dict


    def get_channel_dict(self):
        res = r.get(self.main_link + 'channels.list', params={'token': self.TOKEN, 'exclude_archived': '1'})
        res_dict = json.loads(res.content.decode())
        chnl_dict = {}
        for channel in res_dict['channels']:
            chnl_dict[channel['name']] = channel['id']
        return chnl_dict
