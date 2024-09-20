**Author**: u/ZanderDogz

**Posted on**: 2022-12-01

Original post: [https://www.reddit.com/r/RealDayTrading/comments/z9u03i/stacked_stocksectormarket_rsrw_arrows_for/](https://www.reddit.com/r/RealDayTrading/comments/z9u03i/stacked_stocksectormarket_rsrw_arrows_for/)

I took some existing code from this subreddit (credits should all be in the pinescript source code) and made an indicator for TradingView that displays arrows above/below a candle only if 1) the stock is RS to the market, the stock is RS to the sector, and the sector is RS to the market AND 2) the stock is above VWAP. Same deal on the short side (This has been called "stacked RS/RW" on this sub before). 

I wanted a cleaner way to immediately know if one of my daytrade positions still meets the stacked RS/RW criteria, so I made this small modification to existing code and figured I would share it. Having a quick visual way to see right on the candles that the stock still meets this set of criteria has helped me stay in winners longer and cut losers quicker. I've had good results entering good stocks on compression breakouts with volume, and staying in the position until I get a candle without an arrow, or my read of SPY price action changes. 

My portion of the pinescript is an absolute mess so lmk if anything doesn't work! Getting the arrows to show up has been a bit finicky - it should work but I will make adjustments if not. 

[Here](https://www.tradingview.com/script/HyarDxDP-Real-Relative-Sector-Strength-Arrows/) is the indicator. Hope it helps keep your charts clean!

EDIT:

Use [this](https://wtools.io/paste-code/bHD4) link to copy-paste the code into pinescript instead of the first link