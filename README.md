# GooglePlayToLastFM

1. Follow the instructions in the javascript file, paste the data into a file called "old.csv" and save it.   
    - MAKE SURE TO USE THE songsToText("all", true); function to get the pastable data

2. Run the python file in the same directory as the csv file, and it will autogenerate csv files the approriate size to prevent you from going over on your submissions for the day. If you have more than 8000 it will take you more than 1 day to upload them all.
    - It now works on most songs, please let me know if any fail

3. Download this: https://github.com/coczero/Last.fm-Scrubbler-WPF/releases and then adjust the settings in CSV scrobbler section to match this:
    
        Artist Field -- 0
        
        Album Field -- 1
        
        Track Field -- 2
        
        Timestamp (just sets it to today) -- 3
        
        Album Artist (idk what this is) -- 0
        
        Duration -- 3
        
        Delimiters -- Don't changes
        
4. Select the one of the csv files (or only one if you have less than 8000) and enjoy lastfm

As a note, this should work in theory with any csv file for any music service, you might just have to adjust the columns in the csv

**original javascript file (it is slightly edited here however): https://gist.github.com/jmiserez/c9a9a0f41e867e5ebb75**
