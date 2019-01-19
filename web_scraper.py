import urllib2
from bs4 import BeautifulSoup

# Parse website into soup format
rock_chart = 'https://www.billboard.com/charts/rock-songs'
page = urllib2.urlopen(rock_chart)
soup = BeautifulSoup(page, 'html.parser')

# Extract Top Song
top_song_title = soup.find('div', attrs={'class': 'chart-number-one__title'})
title = top_song_title.text

top_song_artist = soup.find('div', attrs={'class': 'chart-number-one__artist'})
artist = top_song_artist.text

print("The top rock song is {} by {}.".format(title, artist))