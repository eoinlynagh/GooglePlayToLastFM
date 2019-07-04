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
songs = [[]]
c = 0
num = 1
with open("old.csv","r") as f:
    for line in f:
        songConst = []
        #if your song/artist/whatever has more than one comma you are out of luck, that should be unusual though
        count=line.split("\"")
        if(len(count) == 3):
            for _ in count:
                if(_ != count[1]):
                    for x in _.split(","):
                        if(not not x):
                            songConst.append(x)
                else:
                    songConst.append("\""+_+"\"")
            songs.append(songConst)
        elif(len(count) == 1):
            vals=line.split(",")
            for _ in vals:
                if(_):
                    songConst.append(_)
            songs.append(songConst)
    songs.pop(0)
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