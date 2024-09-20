**Author**: u/Glst0rm

**Posted on**: 2022-11-08

Original post: [https://www.reddit.com/r/RealDayTrading/comments/ypao5a/sharing_my_tradingview_layouts_for_realdaytrading/](https://www.reddit.com/r/RealDayTrading/comments/ypao5a/sharing_my_tradingview_layouts_for_realdaytrading/)

Greetings!

I've been wanting to share my TradingView setup which lets me find and trade the highest-quality trading setups. I have created a robust layout that involves a watchlist + M5 + daily chart as well as a full-screen grid for active trading. The layout includes a number of indicators that I've either adopted or built with the help of our community. If you trade relative strength/weakness and use TradingView to chart - this post will get you started or hopefully show you a few new tricks.

The superpower of this setup is Trading View's ability to show indicators and data from multiple timeframes within one chart. This allows me to plot the M5 chart and include the daily 50/100/200 simple moving averages, daily support/resistance levels, and trendlines. Powerful stuff!

I'll introduce the main layouts, and then explain the indicators and settings below. Here are links to the layouts if you want to get started:

* Research Layout: [https://www.tradingview.com/chart/7ga75TOx/](https://www.tradingview.com/chart/7ga75TOx/)
* 8-Ticker Grid Layout: [https://www.tradingview.com/chart/hVKgKmZ4/](https://www.tradingview.com/chart/hVKgKmZ4/)

I hope this helps you find your groove with TradingView and RDT!

\- st0rm

ps - check out my other posts on my [custom volume, rsrw, rvol indicator](https://www.reddit.com/r/RealDayTrading/comments/wli2fw/volume_relative_volume_and_relative_volume_to_spy/) and a [semi-automatic buy/sell signal indicator](https://www.reddit.com/r/RealDayTrading/comments/vibfim/i_made_a_market_first_buysell_indicator_on/) that helps you with trade timing.

pps - check out [ZenScans](https://www.reddit.com/r/RealDayTrading/comments/zaast0/a_new_stock_screener_based_on_relative_strength/), my new stock screener focused on relative strength/weakness. It plays nice with TradingView and has all the stuff we care about.

#### Research Layout: Watchlist, M5, and Daily Chart

[Watchlist and Chart - flip charts and identify trades](<img src="cache/images/a5dc3fb5e3017cd76a462eb8168c1e87.png" alt="Reddit Image">)

This is my primary research view which allows me to rapidly flip charts on my watchlist and assess trading bona-fides. It involves a watchlist, M5, and D1 charts, and a blend of custom indicators that show:

* Relative strength graph and indicator
* Total volume (surprisingly hard in TradingView)
* ATR percent - percent of the stock price the ticker has moved in the last hour. I like to trade tickers with .40% or higher ATR
* Relative volume (RVOL) - the ticker's volume relative to the 10-day average at the same time
* Relative volume to SPY (RRVOL)
* VWAP
* D1 simple moving averages (50/100/200)
* D1 Horizontal support and resistance lines
* D1 Sloping trend lines

[5-minute chart](<img src="cache/images/7f0dc651c01d1b9220be0fa88ab3ff5b.png" alt="Reddit Image">)

[Daily Chart](<img src="cache/images/e4197d8237adfc053413dee3fe2f6dc8.png" alt="Reddit Image">)

I use the following indicators from the TradingView community (and a few that I custom build and have shared)

&#x200B;

**1: Relative Volume and Relative Strength Labels (my creation)**

[Indicator: Volume, RS\/RW, ATR, RVol, and candle strength](<img src="cache/images/dd9373df4dc33140b70f9665b18a47db.png" alt="Reddit Image">)

Shows current day's volume, relative strength/weakness, ATR percent of the price, relative volume, and relative volume to SPY. It also calculates the bar-by-bar strength of the ticker compared to each SPY bar.

Indicator: [https://www.tradingview.com/script/wWKsXxpH-Daily-Volume-RVol-RRVol-and-RS-RW-Labels/](https://www.tradingview.com/script/wWKsXxpH-Daily-Volume-RVol-RRVol-and-RS-RW-Labels/)

My Reddit post with more details: [https://www.reddit.com/r/RealDayTrading/comments/wli2fw/volume\_relative\_volume\_and\_relative\_volume\_to\_spy/](https://www.reddit.com/r/RealDayTrading/comments/wli2fw/volume_relative_volume_and_relative_volume_to_spy/)

&#x200B;

**2: Real Relative Strength (RRS) custom chart (custom, adapted from open source)**

[Indicator: Relative Strength\/Weakness Plot](<img src="cache/images/f6ead79b94039e0f30eb13f12e6e0382.png" alt="Reddit Image">)

[https://www.tradingview.com/script/90igqsBG-Real-Relative-Strength-Graph/](https://www.tradingview.com/script/90igqsBG-Real-Relative-Strength-Graph/)

Plot of the ticker's relative strength/weakness to SPY, adapted from work by /u/WorkPiece and /u/HurlTeaInTheSea.

&#x200B;

**3: Daily SMAs and prior day high/low**

[Indicator: Daily SMAs on M5 chart](<img src="cache/images/46ceae92e51baa155571038d4d45d749.png" alt="Reddit Image">)

Shows the prior day's high/low/open/close, and any nearby D1 simple moving average right on the M5 chart. This is so convenient and helps you pick entries and exits based on these natural support/resistance points. I created this indicator, adapted from open source:

[https://www.tradingview.com/script/NIfVNAp9-Daily-SMA-and-Prior-Day-Levels/](https://www.tradingview.com/script/NIfVNAp9-Daily-SMA-and-Prior-Day-Levels/)

&#x200B;

**4: Automatic display of trend lines (the real difference maker!)**

[Indicators: TrendLiner and TrendLines v2](<img src="cache/images/88114d6db345561cc4375b58261f3c27.png" alt="Reddit Image">)

I use the following ingenious indicators that plot trend, support, and resistance lines based on the D1 chart (some configuration required).

* TrendLiner [https://www.tradingview.com/v/CTYf8ACy/](https://www.tradingview.com/v/CTYf8ACy/)
* Trend Lines v2 [https://www.tradingview.com/v/eXUYLaGv/](https://www.tradingview.com/v/eXUYLaGv/)

Configure Trend Lines v2 to use the Daily chart, even when displayed on an M5 chart. This will display the D1 support/resistance lines on the M5.

&#x200B;

#### Grid View: M5 charts for active trades

I also combine these indicators into a powerful grid view that lets me monitor tickers for day trades and entries/exits.

[8-ticker Grid \(for monitoring active trades\)](<img src="cache/images/c8270e23df6ad8d2004a799c3cb68c13.png" alt="Reddit Image">)

#### Watchlist/Screener

TradingView lacks a robust scanner with parameters that are particularly useful for finding tickers with relative strength/weakness. I use a combination of OptionStalker ([https://oneoption.com/](https://oneoption.com/)) and [ZenScans](https://www.reddit.com/r/RealDayTrading/comments/zaast0/a_new_stock_screener_based_on_relative_strength/), a custom screener I wrote to identify tickers. I import my target tickers into TradingView to research, set alerts, and monitor trades.

&#x200B;

[Use the 'Import List' feature to pull in a comma-separated list of tickers](<img src="cache/images/492d6fd15edd581d5fd4a63aebbc8d29.png" alt="Reddit Image">)

Together these layouts and indicators form a powerful trading platform. I hope this helps you get started - please feel free to reach out with questions, and I can do my best to get you started.