import random
import re
import feedparser

WORDS = ["BBC","UNITED","KINGDOM"]

URL="http://feeds.bbci.co.uk/news/uk/rss.xml"

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    mic.say("Pulling up BBC UK news.")
    d=feedparser.parse(URL)
    for x in xrange(0,4):
	mic.say(d.entries[x].title)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bbbc united kingdom\b', text, re.IGNORECASE))
