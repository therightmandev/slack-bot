from api_functions import Api_Requests


def main():

    TOKEN = ""

    api = Api_Requests(TOKEN)
    USERS = api.get_user_dict()
    CHANNELS = api.get_channel_dict()


    res = api.send_msg('Should be posted as bot', CHANNELS['talkingbots'])
    print(res.content.decode())

main()
