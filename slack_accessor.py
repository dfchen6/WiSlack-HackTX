import os
import time
from multiprocessing import Pool
from slackclient import SlackClient

SLACK_TOKEN = "xoxp-89077229511-89077924401-94985752357-7e62c2e0cb29705decdb59a3d7baddf9"

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
