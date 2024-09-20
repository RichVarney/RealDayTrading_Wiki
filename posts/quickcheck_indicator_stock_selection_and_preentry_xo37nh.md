**Author**: u/--SubZer0--

**Posted on**: 2022-09-25

Original post: [https://www.reddit.com/r/RealDayTrading/comments/xo37nh/quickcheck_indicator_stock_selection_and_preentry/](https://www.reddit.com/r/RealDayTrading/comments/xo37nh/quickcheck_indicator_stock_selection_and_preentry/)

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

\[UPDATE: v1.5 of this indicator is now available  - Code for ThinkOrSwim is [here](https://pastebin.com/KsLJ5TF4) : Usage and details [here](https://www.reddit.com/user/--SubZer0--/comments/z1j7j1/quickcheck_indicator_workflow_and_usage_draft/). After you import this study, disable the sidebar in ToS and shrink the window to see just the readouts\]

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

&#x200B;

&#x200B;

We repeatedly hear u/HSeldon2020,  u/onewyse or  u/OptionStalker or the mods enforce criteria for stock selection, what not to do and when not to enter a trade. For starters, the most [important criteria](https://www.reddit.com/r/RealDayTrading/comments/v8rp1y/five_simple_rules_for_trading_right_now/) (if you’re not consistently profitable) that has been consistently hammered into our heads is to not short when market is up and not go long when market is down. There are many other criteria that are part of our checklist to select stocks (e.g VWAP, YHigh/YLow, Open, YClose, Daily SMAs) before entering a trade and it can be easy to forget them at times. How do we remember to check everything, each time we look at a ticker?

&#x200B;

*Note: If you’re not sure what all this means, read the wiki and search this sub for posts from others that discuss their criteria and lessons from the experts.*

&#x200B;

#### QuickCheck Indicator

I'm in both the OS and the Reddit chatrooms. There are many tickers called out and many of them do not show up in my scanner and i am naturally curious about some of them. I usually load that ticker in ToS and manually go through my checklist and see if it is worth considering. All those manual checks take time and sometimes i miss some critical ones. To avoid all that manual work and save time, I created a ToS indicator that gives me a bird’s eye view of what that stock is doing and where it is currently with respect to the criteria I pay attention to. Whenever a ticker is called out, i load it in ToS and can very quickly get the information i need. This indicator gives me a quick snapshot of:

&#x200B;

* If SPY is up or down for the day. (I use the most basic check for this. If SPY is above YClose, it is up, otherwise it is down)
* If the stock is up or down for the day
* If the stock and SPY don’t align with direction
* If  stock has relative strength or weakness (Thanks to u/WorkPiece)
* If stock price is above or below intra-day VWAP
* If stock price is above or below today’s open
* If stock price is above or below YHigh/YLow
* If stock's ATR is above or below my criteria
* If stock price is above or below the Daily SMA (50/100/200)
* If the RVOL is higher or lower than 100% (Thanks to u/HurlTeaInTheSea)
* If the current volume is higher or lower than the average of  past n days
* If the n day average volume is less than my criteria
* How far the price is from any given criteria’s price level (e.g. difference between current price and 100SMA)
* If you’re possibly going to trade against the market and warns you

Once i parse through this information, i then decide if i want to add it to my watchlist or not.

&#x200B;

Here is how the indicator looks like. It does not have any price plot, just read-outs with colored boxes and is best used in a separate, small-sized window.

&#x200B;

[QuickCheck Indicator](<img src="cache/images/3bd0260caab6ff5bfbe38f690af4d23e.png" alt="Reddit Image">)

&#x200B;

Here is what the colored boxes mean:

* **Red**: Symbol is down for the day
* **Green**: Symbol is up for the day
* **Cyan**: Indicates current price meets the requirement for that stock's criteria and the stock is moving in the same direction as SPY
* **Orange**: Indicates current price meets the requirement for that stock's criteria but that stock is moving in the opposite direction of SPY. Orange boxes are a warning that you’ll be trading against the market. If you’re experienced and consistently profitable, this could be a positive confirmation for you but for most people, it would mean to tread with caution and wait for those boxes to turn cyan, or just look for other stocks
* **Gray**: Indicates current price does not meet requirement for that stock's criteria regardless of whether SPY and stock are moving in the same direction or not. E.g. if stock is up for the day, you'd ideally want it to also be above VWAP. If price is below VWAP, that box will be gray till price moves above VWAP
* **White**: Indicates neutral data that is not tied to any criteria and is just used for reference. E.g.: Current Price (reserved for future use)

&#x200B;

&#x200B;

**How to interpret this indicator?**

The best way to use this indicator is: ***Most of the boxes need to be cyan colored*** to even consider this stock to trade. Cyan boxes mean the stock is trading in the same direction of SPY and meets the criteria listed for that stock. The more cyan boxes you have, the better your odds are that this might be the right stock. Your individual strategy will determine which of those cyan boxes are critical to you and which ones are lower priority and can be ignored.... and this can be different for everyone.

In the screenshot above, SPY is down, OXY is down, this is good as both are in the same direction. OXY has relative weakness of -2.24 (which is very nice), it is way below YClose, today's Open, YHigh, YLow, 50SMA and 100SMA (all nice things to have for shorting a stock). It is however very close to VWAP and i usually don't enter trades in that zone as the price can chop a bit around VWAP. It is also above 200SMA. Can i ignore that? Because the RVOL is high, the current vol is 120% of the 20day average volume, we are \~4.5 bucks away from the 200SMA and SPY has been providing a nice tailwind, i will ignore that gray box and will add OXY to my watchlist.

For me to trade a stock, **I need to see as many cyan boxes as possible**. There might be a few gray boxes i am willing to overlook if other conditions are met. Of course this is not the only criteria I use for making a decision to enter, this needs to be combined with a confluence of other indicators such as volume, algo lines, trend lines, support and resistance levels, daily chart, market structure, trend and most importantly price action for the stock and for SPY.

&#x200B;

Below is an example of a stock that is moving in the opposite direction of the market.

&#x200B;

[QuickCheck Indicator - SPY and HD are in opposite directions](<img src="cache/images/ec81420166c9387a53a8265319db9a66.png" alt="Reddit Image">)

In this screenshot, SPY is down but HD is up, which explains all the orange lights lighting up in the indicator.  Although many indicators are lining up for HD, it's price action wasn't strong enough to break YHigh and was trading range-bound for most of the day. The orange lights are basically warning me that i can't be trading this because it is going against the market. If SPY was green, those boxes would've turned cyan and i would've set alerts for HD above YHigh and then consider taking a long trade if it breaks YHigh.

&#x200B;

#### Download:

**Link:** See top of this post for latest thinkscript code

After you import:

* Resize/Shrink your chart window to fit the contents and make window compact
* Link this chart to your main chart. This way, whenever you load something in your main chart, this window will also automatically update. If you don't know how to link charts, click on this option (screenshot below) and select the same color for your main chart and this window.

&#x200B;

[Linking Charts to keep them in sync](<img src="cache/images/3dd5adc31564d482b17a1d4bd1e94aa9.png" alt="Reddit Image">)

&#x200B;

&#x200B;

#### Usage:

* This indicator should be used on a separate chart window and is designed to be viewed in a compact form. It will hide the price plot and you will not see anything except the criteria boxes
* This script uses the [RealRelativeStrength study](https://www.reddit.com/r/RealDayTrading/comments/rpi75s/real_relative_strength_indicator/) created by u/WorkPiece and the [RelativeVolume study](https://www.reddit.com/r/RealDayTrading/comments/ue4ujq/tostv_timebased_relative_volume_rvol_a_better/) created by u/HurlTeaInTheSea. The chart timeframe is set to M5 to work with those studies. I have not tested this with other timeframes
* If you’re trading the SPY or want to see what the SPY is doing, this indicator will also allow you to add SPY and see its metrics
* The number of days to be used on the chart depends on how far you want to look when calculating some of the metrics. In my case, I use 20D worth of data to calculate average volume and RVOL. Because these calculations do not include data from current day, you need to set your chart period to longer than 20D. In my chart, I have it set to 25D 5M to make enough data available for these calculations. ***This might not work on all systems if you have limited system resources, as loading data for 25 days might involve quite a bit of memory overheads***
* You could also use this indicator inside a flexible grid and get a birds eye view of multiple stocks at the same time, like screenshot below. ***Keep in mind though, these indicators are processor heavy and could slow your system down if you have two many of these dashboards.***

&#x200B;

&#x200B;

[QuickCheck inside a ToS flexible grid](<img src="cache/images/3081e8d34ea5e21984d3c5d0685defcd.png" alt="Reddit Image">)

After seeing the readout from AMD, i would add this to my watchlist and set alerts below VWAP and watch price action before entering. Looks like a good stock to trade that day

&#x200B;

#### Configuration:

<img src="cache/images/0a363c35923a4c3c7e04c35069478a69.png" alt="Reddit Image">

* **Show Distance From Level**: This shows a delta between the current price and the criteria's price level (e.g. price delta between current price and the 50SMA price level). You can turn off the deltas if you don't want to see them
* **Symbol Up/Down**: This is the text that precedes the labels to indicate above or below. I suggest not changing and leaving it as is because it makes the visual layout messy if changed
* **RRS Length**: This is the input to the [RealRelativeStrength study](https://www.reddit.com/r/RealDayTrading/comments/rpi75s/real_relative_strength_indicator/) created by u/WorkPiece. This determines how many bars to use for calculating RRS. Because this is used on a M5 chart, 12 bars would mean one hour's worth of rolling data for calculating RRS and this has been the de-facto setting used in this community
* **ATR Length**: This is on a daily timeframe and is used to calculate the daily ATR average over 14 days
* **Desired ATR**: I don't trade stocks that have ATR(14D) less than $2.5. This setting helps me see if the stock has ATR higher than what i am looking for
* **Show Volume Metrics**: This hides the bottom section related to volume metrics if you don't wish to see them
* **N Day Average**: This parameter is the input to the [RelativeVolume study](https://www.reddit.com/r/RealDayTrading/comments/ue4ujq/tostv_timebased_relative_volume_rvol_a_better/) created by u/HurlTeaInTheSea. I use 20 days to calculate relative volume because it aligns with the other platforms that I use.
* **Desired Average Volume**: We want to trade stocks that have a decent daily volume and move during the day. Default is set to minimum 5M shares daily over 20 days (controlled by N Day Average)

&#x200B;

#### Disclaimer:

I’m not a financial professional and you should use your discretion in using this indicator and interpreting what it means for your strategy and entry criteria. All this indicators does is to automate a bunch of checks that I was doing manually and saves me a lot of time.  By all means, this indicator does not give you a signal to trade, you should rely on your strategy and other indicators to make a decision whether to enter a trade or not

&#x200B;

I had fun developing this indicator because it automates quite a bit of manual checks for me and has been very helpful. I hope it helps you too. As i am still learning ThinkScript and relatively new to this community, please feel free to give feedback if something i have here isn't aligned with what the community preaches or if other boxes can be added to make this indicator even better. Also, feel free to modify the code to suit your needs and don't forget to share it with the community here.