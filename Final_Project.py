import random

gMajChords = ["Gm", "Am","Bm","Cmaj","Dmaj","Em","Fdim"]
cMajChords = ["Cmaj", "Dm", "Em", "Fmaj", "Gmaj", "Am", "Bdim"]
dMajChords = ["Dmaj", "Em", "F#m", "Gmaj", "Amaj", "Bmin", "C#dim"]
eMajChords = ["Emaj", "F#m", "G#min", "Amaj", "Bmaj", "C#m", "D#dim"]
print ("Choose a random Chord from the list")
sampled_list = random.sample(eMajChords,4)
print(sampled_list)
print("Here are your chords!")

#This program will give you a random chord progression from the key of your choosing.
#Select one of the MajChords, and select up 3-6 chords that you want in the progession.