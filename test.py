import webbrowser
import time
import random

while True:
    sites = random.choice(['amazom.com', 'akirachix.com', 'google.co', 'youtube.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(2,10)
    time.sleep(seconds)