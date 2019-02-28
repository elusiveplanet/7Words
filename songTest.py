import lyricsgenius
genius = lyricsgenius.Genius("D53BzEbSVz2RmrRLyHfxFbNkFmQwvr6SVhB9QHOKw49i2m0Bmimyz47vg4ZY5Ksl")
artist = genius.search_artist("Passion Pit", max_songs=3, sort="title")
print(artist.songs)
song = genius.search_song("American Blood", artist.name)
print(song.lyrics)
target = "peak" # this is def in American Blood's lyrics.

artist = genius.search_artist("Playboi Carti", max_songs = 5, sort="title")
print(artist.songs)
song = genius.search_song("dothatshit!", artist.name)
print(song.lyrics)

target = "bee"

if song.lyrics.find(target) == -1:
	print ("Target not found.")
else:
	print ("Target located!")

naughtyWords = ["shit","piss","fuck","cunt","cocksucker","motherfucker","tits","goddamn", "god damn", "sex", "cock", "ass"]

i = 0
for x in naughtyWords:
	if song.lyrics.find(naughtyWords[i]) == -1:
        	print ("Target word " + naughtyWords[i] + " not found.")
	else:
        	print ("Target word " + naughtyWords[i] + " located!")
	i += 1
