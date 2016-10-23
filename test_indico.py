import indicoio
indicoio.config.api_key = '52f70bbc93b34cd04743740ceae89d1a'


# Key words extraction
def get_key_word(s):
	indicoio.keywords(s, version=2)

# Sentiment Analysis
def get_sentiment(s):
	indicoio.keywords(s, version=2)

