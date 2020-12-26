import lyricsgenius
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

genius = lyricsgenius.Genius("D53BzEbSVz2RmrRLyHfxFbNkFmQwvr6SVhB9QHOKw49i2m0Bmimyz47vg4ZY5Ksl")

targetPlaylistURI = 'spotify:playlist:2SmqZrAaWFs9GP4AAfNnIZ'

# Import bad word list
readFile = "badwords.txt"
badWordList = []
with open(readFile) as f:
   lines = f.readline()
for line in lines.split(","):
   badWordList.append(" " + line + " ")

playlist = spotify.playlist(targetPlaylistURI)
#print(playlist)

tracks = spotify.playlist_items(targetPlaylistURI, fields='items.track.name,items.track.artists.name')

# Dump JSON to file
with open("data_file.json", "w") as write_file:
    json.dump(tracks, write_file)

def findBadWords(song):
    explicit = False
    i = 0
    for x in badWordList:
    	if song.lyrics.find(badWordList[i]) != -1:
                explicit = True
            	# print ("The word" + badWordList[i] + "was found in the song.")
    	i += 1
    return explicit

explicitSongTitles = []
noLyricsFound = []

# Print playlist track number, track name, artist name
for i, n in enumerate(tracks['items']):
    print(' ', i, n['track']['name'], n['track']['artists'][0]['name'])
    song = genius.search_song(n['track']['name'], n['track']['artists'][0]['name'])
    if song is not None:
        lyricsExplicit = findBadWords(song)
    else:
        noLyricsFound.append(n['track']['name'] + " by " + n['track']['artists'][0]['name'])
    if lyricsExplicit:
        explicitSongTitles.append(n['track']['name'] + " by " + n['track']['artists'][0]['name'])
    # print(song.lyrics)

print("Songs with explicit lyrics:")
for x in explicitSongTitles:
    print(x)

print("Songs with no lyrics found:")
for x in noLyricsFound:
    print(x)
