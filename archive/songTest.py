import lyricsgenius
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify()

username = "????????????????????????????????"
scope = 'playlist-read-private'
client_id='????????????????????????????????'
client_secret='????????????????????????????????'
redirect_uri='????????????????????????????????'

SPOTIPY_CLIENT_ID = '????????????????????????????????'
SPOTIPY_CLIENT_SECRET = '????????????????????????????????'
SPOTIPY_REDIRECT_URI = 'spotify:track:????????????????????????????????'

util.prompt_for_user_token(username,scope)

results = sp.search(q='modest mouse', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print (' ', i, t['name'])

genius = lyricsgenius.Genius("????????????????????????????????")
#artist = genius.search_artist("Passion Pit", max_songs=3, sort="title")
#print(artist.songs)
#song = genius.search_song("American Blood", artist.name)
#print(song.lyrics)
#target = "peak" # this is def in American Blood's lyrics.

artist = genius.search_artist("Playboi Carti", max_songs = 1, sort="title")
print(artist.songs)
song = genius.search_song("dothatshit!", artist.name)
print(song.lyrics)

target = "bee"

if song.lyrics.find(target) == -1:
	print ("Target not found.")
else:
	print ("Target located!")

naughtyWords = ["shit","piss","fuck","cunt","cocksucker","motherfucker","tits","goddamn", "god damn", "sex", "cock", "ass", "nigger", "nigga", "dick", "bitch", "cum"]

i = 0
for x in naughtyWords:
	if song.lyrics.find(naughtyWords[i]) == -1:
        	print ("Target word " + naughtyWords[i] + " not found.")
	else:
        	print ("Target word " + naughtyWords[i] + " located!")
	i += 1


playlists = sp.user_playlists('renderos17')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None