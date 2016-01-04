import requests as r
import json

class Api_Requests:
    def __init__(self):
        self.main_link = 'https://slack.com/api/'
        with open('token.txt', 'r') as t:
            self.TOKEN = t.readlines()[0]


    def send_msg(self, text, channel_id, as_user='true', username='still_learning'):
        if text is not None:
            if as_user: res = r.get(self.main_link + 'chat.postMessage', params={'token': self.TOKEN, 'text': text, 'channel': channel_id, 'as_user': as_user})
            elif not as_user: res = r.get(self.main_link + 'chat.postMessage', params={'token': self.TOKEN, 'text': text, 'channel': channel_id, 'as_user': as_user, 'username': username})
            return res


    def get_user_dicts(self):
        res = r.get(self.main_link + 'users.list', params={'token': self.TOKEN, 'presence': '0'})
        res_dict = json.loads(res.content.decode())
        user_name_dict = {}
        user_id_dict = {}
        for user in res_dict['members']:
            user_name_dict[user['name']] = user['id']
        for user in res_dict['members']:
            user_id_dict[user['id']] = user['name']
        return user_name_dict, user_id_dict


    def get_channel_dicts(self):
        res = r.get(self.main_link + 'channels.list', params={'token': self.TOKEN, 'exclude_archived': '1'})
        res_dict = json.loads(res.content.decode())
        chnl_name_dict = {}
        chnl_id_dict = {}
        for channel in res_dict['channels']:
            chnl_name_dict[channel['name']] = channel['id']
        for channel in res_dict['channels']:
            chnl_id_dict[channel['id']] = channel['name']
        return chnl_name_dict, chnl_id_dict
