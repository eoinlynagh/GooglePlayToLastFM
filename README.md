# GooglePlayToLastFM

1. Follow the instructions in the javascript file, post into a .txt file and open with excel, and save as *old.csv.*

2. Run the python file in the same directory as the csv file, and it will autogenerate csv files the approriate size to prevent you from going over on your submissions for the day. If you have more than 8000 it will take you more than 1 day to upload them all.

3. Download this: https://github.com/coczero/Last.fm-Scrubbler-WPF and then adjust the settings in CSV scrobbler section to match this:
    
        Artist Field -- 0
        
        Album Field -- 1
        
        Track Field -- 2
        
        Timestamp (just sets it to today) -- 3
        
        Album Artist (idk what this is) -- 0
        
        Duration -- 3
        
        Delimiters -- Don't changes
        
4. Select the one of the csv files (or only one if you have less than 8000) and enjoy lastfm

As a note, this should work in theory with any csv file for any music service, you might just have to adjust the numbers the pyhton file uses for indexing (line 53 and 60)

**original javascript file (it is slightly edited here however): https://gist.github.com/jmiserez/c9a9a0f41e867e5ebb75**
