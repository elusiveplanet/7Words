import lyricsgenius
genius = lyricsgenius.Genius("D53BzEbSVz2RmrRLyHfxFbNkFmQwvr6SVhB9QHOKw49i2m0Bmimyz47vg4ZY5Ksl")
artist = genius.search_artist("Passion Pit", max_songs=3, sort="title")
print(artist.songs)
