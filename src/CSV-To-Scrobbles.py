import csv

new=open("new.csv","w")
log=open("log.txt","w")
writer = csv.writer(new)

songs = []
c = 0
num = 1

failedSongs = ["FAILED SONGS: \n"]
songsMissingPlayValues = ["SONGS MISSING DATA IN SPREADSHEET: \n"]

with open("old.csv","r") as f:
    reader = csv.reader(f)
    for song in reader:
        try:
            if(song[4] == ''):
                song[4] = '0'
                if(songsMissingPlayValues.count("artist: " + song[0] + ", song name: " + song[2] + "\n") <= 0):
                    songsMissingPlayValues.append("artist: " + song[0] + ", song name: " + song[2] + "\n")
            for i in range(0,int(song[4])+1):
                    c += 1
                    if(c == 2750):
                        c = 0
                        name = "new"+str(num)+".csv"
                        new=open(name,"w")
                        writer = csv.writer(new)
                        num += 1
                    if(len(song) == 7):
                        songWriteValue = song[:]
                        del songWriteValue[4]
                        writer.writerow(songWriteValue)
                    else:
                        raise("song did not parse properly")
        except:
            if(failedSongs.count("artist: " + song[0] + ", song name: " + song[2] + "\n") <= 0):
                failedSongs.append("artist: " + song[0] + ", song name: " + song[2] + "\n")
            continue

print(str(len(failedSongs)-1) + " song(s) have failed to be added, please check log.txt for more information")
log.writelines(failedSongs)     
print(str(len(songsMissingPlayValues)-1) + " song(s) were missing data on the number of plays, please check log.txt for more information")
print("They have been assumed to have only been played once.")
log.writelines(songsMissingPlayValues)     