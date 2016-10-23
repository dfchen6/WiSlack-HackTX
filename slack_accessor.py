import os
import time
from multiprocessing import Pool
from slackclient import SlackClient

SLACK_TOKEN = "xoxp-18006151426-18336171664-95084351714-30f4d11848610258095987dfcb076d5d"

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
    history_call = slack_client.api_call("channels.history",channel=channel_id, count=30)
    if history_call.get('ok'):
        # Filter out people entering room
        filtered = [i for i in history_call['messages'] if i["text"].find("<@U") == -1]
        return filtered
    return None

def list_channel_history_by_name(channel_name):
    channels = list_channels()
    for channel in channels:
        if (channel['name'] == channel_name):
            return list_channel_history(channel['id'])
    return None
