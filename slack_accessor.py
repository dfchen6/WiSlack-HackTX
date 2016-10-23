import os
import time
from multiprocessing import Pool
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

slack_client = SlackClient(SLACK_TOKEN)

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='bot',
        icon_emoji=':robot_face:'
    )

def list_channel_history(channel_id):
    history_call = slack_client.api_call("channels.history",channel=channel_id)
    if history_call.get('ok'):
        return history_call['messages']
    return None

def list_channel_history_by_name(channel_name):
    channels = list_channels()
    for channel in channels:
        if (channel['name'] == channel_name):
            return list_channel_history(channel['id'])
    return None

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
            if c['name'] == 'hackathon':
            	pool = Pool(processes=1)
            	print(pool.map(list_channel_history, [c['id']]))
    else:
        print("Unable to authenticate.")