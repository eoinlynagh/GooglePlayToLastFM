new=open("new.csv","w")
songs = []
c = 0
num = 1
with open("old.csv","r") as f:
    for line in f:
        songConstructor = []
        #if your song/artist/whatever has more than one comma you are out of luck, that should be unusual though
        lineSplitQuotes=line.split("\"")
        if(len(lineSplitQuotes) == 3):
            for value in lineSplitQuotes:
                if(value != lineSplitQuotes[1]): #split around comma
                    for x in value.split(","):
                        if(x):
                            songConstructor.append(x)
                else:
                    songConstructor.append("\""+value+"\"")
            songs.append(songConstructor)
        elif(len(lineSplitQuotes) == 1):
            vals=line.split(",")
            for value in vals:
                if(value):
                    songConstructor.append(value)
            songs.append(songConstructor)
    for song in songs:
        try:
            for i in range(0,int(song[4])+1):
                    c += 1
                    if(c == 2750):
                        c = 0
                        name = "new"+str(num)+".csv"
                        new=open(name,"w")
                        num += 1
                    if(len(song) == 7):
                        new.write(song[0]+","+song[1]+","+song[2]+","+song[3]+","+song[5]+","+song[6])
                    else:
                        raise("song did not parse properly")
        except:
            print("song failed:")
            print("\t artist: " + song[0])
            print("\t   name: " + song[1] + "\n")
            continue
