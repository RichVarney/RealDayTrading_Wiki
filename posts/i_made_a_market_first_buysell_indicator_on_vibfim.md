**Author**: u/Glst0rm

**Posted on**: 2022-06-22

Original post: [https://www.reddit.com/r/RealDayTrading/comments/vibfim/i_made_a_market_first_buysell_indicator_on/](https://www.reddit.com/r/RealDayTrading/comments/vibfim/i_made_a_market_first_buysell_indicator_on/)

Hi everyone!

I've adapted my market-first algo-trading signal (I named it ZenBot - hah!) into a nifty TradingView indicator that shows buy, sell, short, cover, and relative strength/weakness changes for any ticker. I'm super excited at how well it's working and wanted to share it with everyone here. It's been super exciting watching it in action signaling the trades we take in the daily chat.

[https://www.tradingview.com/script/QjPGnEB3-Market-First-Signals-Relative-Strength-Weakness/](https://www.tradingview.com/script/QjPGnEB3-Market-First-Signals-Relative-Strength-Weakness/)

This weekend I learned some PineScript and built a TradingView indicator version of my algo's signals. It monitors multiple timeframes (M1, M3, M5) for solid trends to follow, volume, and relative strength/weakness to SPY. It also estimates the potential profit to be taken

[Indicator signals from 6\/22 Long on SNOW, Short on SI](<img src="cache/images/b8d66aa18806a83e1225df3be2bdb6bf.png" alt="Reddit Image">)

[My TradingView post](https://www.tradingview.com/script/QjPGnEB3-Market-First-Signals-Relative-Strength-Weakness/) gives all the details, but basically:

* Uses RS/RW against SPY and minimum volatility to suggest trades
* Shows 'Gained RS', 'Lost RS', etc. when the ticker loses its edge
* ADX DI trend, Parabolic SAR, EMAs, and above-average volume used for entries
* Exit is Parabolic SAR with multiple timeframes and ADX DI trend ending
* Uses basic principles from the WIKI - Longs above VWAP, shorts below, etc.
* Alerts

\*\* 6/22 update: thanks for all the feedback! I've added some customizable options:

&#x200B;

[New input options](<img src="cache/images/521076d09d396da0d5f2bd3473cb7f59.png" alt="Reddit Image">)

\*\* 6/23 update: added a live P/L label when a trade is on:

&#x200B;

<img src="cache/images/0c234f1916a24b15c3abe6e0683ca42f.png" alt="Reddit Image">

\*\* 6/30 update: Lots of tweaks to allow winning trades to run longer and make RS/RW detection less jumpy (thanks for all the feedback!). Also gave you the option to take trades only with VWAP and market direction.

&#x200B;

<img src="cache/images/5132c97c1fe3205539f57c89d44f1df5.png" alt="Reddit Image">

\--------------------------------------------------

Here are some screenshots of the indicator in action on tickers brought up in the chat:

[Buy and sell signals for SNOW 6\/22 \(notice the 'Lost RS' subsequent sell signal\)](<img src="cache/images/1afd32311f8a309abc355100f6b89574.png" alt="Reddit Image">)

[Indicator going short on CAT 6\/22](<img src="cache/images/3ed6ac3c199302331684a1a1cc09dc41.png" alt="Reddit Image">)

&#x200B;

[SI is a nice short today \(6\/22\)](<img src="cache/images/79b79a82d75911a25ee0c5ffa3772956.png" alt="Reddit Image">)