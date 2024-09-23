# RealDayTrading_Wiki
Downloads the contents of the reddit /r/RealDayTrading [wiki](https://www.reddit.com/r/RealDayTrading/wiki/) and converts to a HTML file containing all reddit posts and embedded/linked images.  

An EPUB e-book  [The Damn Wiki - Hari Seldon.epub](https://github.com/RichVarney/RealDayTrading_Wiki/blob/main/The%20Damn%20Wiki%20-%20Hari%20Seldon.epub) has also been included, which was converted using [Calibre](https://calibre-ebook.com/). This might be useful for those wishing to read on an e-book or mobile device. You can also convert to PDF or DOCX as you wish.

[<img src="Front%20cover.png" width="200">](https://github.com/RichVarney/RealDayTrading_Wiki/blob/main/The%20Damn%20Wiki%20-%20Hari%20Seldon.epub)



If you want to create the HTML file for yourself, follow the instructions below:

## Requirements:
beautifulsoup4, praw, urllib3

## How to use:
Edit ```download_RealDayTrading_wiki.py``` to include a Reddit API client ID and secret. You must also include a valid user agent which you can get from your browser or using sites like https://www.whatismybrowser.com/detect/what-is-my-user-agent/  

    CLIENT_ID = 'ADD_YOUR_REDDIT_API_CLIENT_ID'  
    CLIENT_SECRET = 'ADD_YOUR_REDDIT_API_CLIENT_SECRET'  
    USER_AGENT = 'ADD_A_VALID_USER_AGENT'  

Then run the file with:  

    python download_RealDayTrading_wiki.py  

This will download all posts and images in the wiki, combine them into one HTML file which can then be converted to EPUB by Calibre, for example.

## Result:
./wiki_output.html  
./images  
* all images are stored in here in their original format (JPG or PNG)

./posts  
* all posts are stored here in markdown format
