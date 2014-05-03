import random
import re
import feedparser

WORDS = ["WEATHER"]

URL="http://open.live.bbc.co.uk/weather/feeds/en/2643743/3dayforecast.rss"

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    mic.say("Pulling up the weather.")
    d=feedparser.parse(URL)
    for x in xrange(0,3):
	mic.say(d.entries[x].title)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bweather\b', text, re.IGNORECASE))
