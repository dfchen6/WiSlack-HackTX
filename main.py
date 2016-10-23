import os
from flask import Flask, request, Response, render_template
from slack_accessor import list_channels, list_channel_history_by_name

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')

@app.route('/channels/<name>')
def get_channel(name):
	history = list_channel_history_by_name(name)
	return render_template("channel.html", name = name, history = history)

@app.route('/', methods=['GET'])
def get_home():
    channels = list_channels();
    return render_template('home.html', channels = channels)

if __name__ == "__main__":
    app.run(debug=True)