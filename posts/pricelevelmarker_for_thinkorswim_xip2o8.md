**Author**: u/--SubZer0--

**Posted on**: 2022-09-19

Original post: [https://www.reddit.com/r/RealDayTrading/comments/xip2o8/pricelevelmarker_for_thinkorswim/](https://www.reddit.com/r/RealDayTrading/comments/xip2o8/pricelevelmarker_for_thinkorswim/)

\[ **EDIT**: Thanks for the great feedback! Updated script (v2.0) is posted [here](https://pastebin.com/wMMx32vs) \]

*v2.0 includes displaying overnight gap, Daily SMA on intraday charts and more configuration settings*

\------------------------

&#x200B;

I use DAS Trader Pro as my primary trading platform and it has an inbuilt study called PriceMarker that automatically plots different critical price levels on the chart such as Today's Open/High/Low, Yesterday's Close/High/Low etc. I've tried to re-create the same for ToS and added a few extra options. I like to share my script here.

Below is what the ToS script will automatically plot:

1. Today's Open
2. Today's High
3. Today's Low
4. Yesterday's Close
5. Yesterday's High
6. Yesterday's Low
7. High from two days ago
8. Low from two days ago
9. 52 Week High
10. 52 Week Low
11. 5 Year High
12. 5 Year Low

You can turn off whichever price level you don't care much about.

&#x200B;

[PriceLevelMarkers](<img src="cache/images/744b1ce49e642bcac1eeffce25483cae.jpg" alt="Reddit Image">)

Additional Info:

* This script will work only on intra-day timeframes
* Plot labels are enabled by default and appear on the far right of the chart, next to the price axis. If you don't see them on your chart, follow below instructions
   * Right click on chart. Select **Style->Settings->Time Axis** and look for **Expansion Area** on the right side. Set it to a minimum of 5.
   * This setting adds some space between the latest price candle and the price axis to allow the labels to fit comfortably and not overlap with the price candles.

[Style Settings Configuration](<img src="cache/images/2e674b66403c0d8a20decf77a3a622a9.jpg" alt="Reddit Image">)

Check top of this post for the latest ThinkScript code

&#x200B;

Note:I'm relatively new to ThinkScript and i appreciate any feedback. Much of what is in my script is also available elsewhere on the internet. i am aware that ToS already has inbuilt studies for DailyOpen and DailyHighLow. I stitched a bunch of studies together and tweaked it to my needs to work off of a single study instead of managing multiple studies. Hope someone finds this useful

&#x200B;

EDIT: Fixed typo