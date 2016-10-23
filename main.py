import os
from flask import Flask, request, Response, render_template
from slack_accessor import list_channels

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')

@app.route('/channel/<name>')
def get_channel(name):
    return render_template("channel.html", name=name)

@app.route('/', methods=['GET'])
def get_home():
    channels = list_channels();
    return render_template('home.html', channels = channels)

if __name__ == "__main__":
    app.run(debug=True)