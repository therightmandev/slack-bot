from api_functions import Api_Requests


def main():

    api = Api_Requests()
    U_NAME_ID, U_ID_NAME = api.get_user_dicts()
    CHNL_NAME_ID, CHNL_ID_NAME = api.get_channel_dicts()


    res = api.send_msg('Should be posted as bot', CHANNELS['talkingbots'])
    print(res.content.decode())

main()
