# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org>

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