# import system libraries
import time, random


# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '808eacd0719741bb8ac225c5ad1e69f5'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'jemorales'


prev_read = 0

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'analog' feed
    feed_01 = aio.feeds('var01')
except RequestError: # create an `analog` feed
    feed = Feed(name='var01')
    feed_01 = aio.create_feed(feed)


try: # if we have a 'analog' feed
    feed_00 = aio.feeds('var00')
except RequestError: # create an `analog` feed
    feed = Feed(name='var00')
    feed_00 = aio.create_feed(feed)

while True:
    # grab the `analog` feed value
    read = aio.receive(feed_01.key)
    if (read.value != prev_read):
        print('received <- ', read.value)
    prev_read = read.value
    var = random.randrange(50, 80)
    aio.send(feed_00.key, var)
    print ('sent -> ' + str(var))
    # timeout so we don't flood IO with requests
    time.sleep(2)
