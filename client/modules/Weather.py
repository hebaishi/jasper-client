import random
import re
import feedparser
import unicodedata

WORDS = ["WEATHER","TODAY","TOMORROW"]

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
    list=[];
    d=feedparser.parse(URL)
    if bool(re.search(r'\btoday\b', text, re.IGNORECASE)):
	list=[0]
    elif bool(re.search(r'\btomorrow\b', text, re.IGNORECASE)):
	list=[1]
    else:
	list=[0, 1, 2]
    for x in list:
        s=unicodedata.normalize('NFKD',d.entries[x].title).encode('ascii','ignore')
        s=re.sub(r'(\d+)C',r'\1 degrees celsius.',s)
	s=re.sub(r'\(\d+F\)',r'',s)
        mic.say(s)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bweather\b', text, re.IGNORECASE))
