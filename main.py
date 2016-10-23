import os
from flask import Flask, request, Response, render_template
from slack_accessor import list_channels, list_channel_history_by_name
from indico_query import get_key_word, get_sentiment
from helper import split_words
# from flask.ext.pymongo import PyMongo

app = Flask(__name__)
# app.config['MONGO_DBNAME'] = 'slack'
# app.config['MONGO_URI'] = 'mongodb://admin:123456@ds019638.mlab.com:19638/slack'
# mongo = PyMongo(app)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')

@app.route('/channels/<name>')
def get_channel(name):
	history = list_channel_history_by_name(name)
	texts = map(lambda x : x['text'], history)
	key_words = get_key_word(texts)
	organized = []
	for i in range(0, len(key_words)):
		organized.append(split_words(texts[i], key_words[i]))
	print(organized)
	#print(key_words)
	return render_template("channel.html", name = name, history = history, key_words = key_words, organized = organized)

@app.route('/channels')
@app.route('/', methods=['GET'])
def get_home():
    channels = list_channels();
    return render_template('home.html', channels = channels)

@app.route('/add')
def add_user():
	user = mongo.db.tags
	user.insert({'Tags' : 'cool'})
	return 'User added!'

if __name__ == "__main__":
    app.run(debug=True)