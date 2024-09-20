**Author**: u/--SubZer0--

**Posted on**: 2022-09-27

Original post: [https://www.reddit.com/r/RealDayTrading/comments/xps3i6/quickcheck_indicator_for_tradingview/](https://www.reddit.com/r/RealDayTrading/comments/xps3i6/quickcheck_indicator_for_tradingview/)

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

 \[UPDATE: v1.5 of this indicator is now available - code for TradingView is [here](https://pastebin.com/bnCmrrfM) : Usage and details [here](https://www.reddit.com/user/--SubZer0--/comments/z1j7j1/quickcheck_indicator_workflow_and_usage_draft/)\] 

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

&#x200B;

I [recently posted](https://www.reddit.com/r/RealDayTrading/comments/xo37nh/quickcheck_indicator_stock_selection_and_preentry/) an indicator in this sub. It automates a bunch of manual checks i used to perform on a ticker to align with my stock selection and entry checklist and shows a dashboard with different colors. There was a lot of good feedback and multiple requests to port this to TradingView. I have to caution you that i know nothing about pine script but took this as a challenge and a learning opportunity to try out something new. As a result, my code might be sloppy and not upto your standards, but it works. I appreciate any feedback on the indicator or if code has issues. Also appreciate ideas to make this indicator better.

&#x200B;

Check [here](https://www.reddit.com/r/RealDayTrading/comments/xo37nh/quickcheck_indicator_stock_selection_and_preentry/) for more details on this indicator and how to use it.

&#x200B;

Few things to note:

* **Very important**: Indicators such as this, RVOL and RRS heavily rely on the datafeed that you have as part of your TradingView subscription. The speed of data updates coming through also matter. If you are using the free datafeed and don't pay for extra data sources in TradingView, the output might not be accurate. Discrepancies can be observed on volume (both intra-day and daily), VWAP, and sometimes the latest bid, ask open and close prices. You will see these discrepanices clearly when you compare it with other platforms that have better datafeeds (e.g. ToS).
* The RRS and RVOL indicators are optimized for the M5 timeframe, please keep this indicator on your M5 charts. I have not tested this as much with other timeframes
* TradingView does not support popping out a separate window and use it as a floating dashboard, like ToS does (it kinda does, but it is very cluttered). The best way right now is to use this indicator inside a chart as an overlay

&#x200B;

Here is how it looks.

&#x200B;

&#x200B;

[QuickCheck - Stock and SPY are in same direction](<img src="cache/images/9f75a967c288d25f34ae1b14785d0ec0.png" alt="Reddit Image">)

&#x200B;

[QuickCheck - Stock and SPY are in opposite direction](<img src="cache/images/aa12383e11ef320bc89ab0d60d7e4711.png" alt="Reddit Image">)

&#x200B;

&#x200B;

[QuickCheck - Configuration](<img src="cache/images/1791752ae299c6063e108a56b5338877.png" alt="Reddit Image">)

&#x200B;

&#x200B;

[QuickCheck - This is how it appears on your chart. The position is configurable](<img src="cache/images/935f683572a2933c1a5381bdfa69f84c.png" alt="Reddit Image">)

&#x200B;

&#x200B;

&#x200B;

[QuickCheck - Works in multiple charts at the same time in a grid](<img src="cache/images/b202901eda7244d2d11beb39ee8ed28f.png" alt="Reddit Image">)

&#x200B;

TradingView has a richer infrastructure for managing visual layouts, text alignment and string operations in general as compared to ToS, which is what made it possible to have a cleaner output. It also supports unicode, which allows using fancy icons for the up/down status. They're configurable, use whatever works for you!!

&#x200B;

The same disclaimers apply from my previous post. Please use this at your own discretion having understood limitations of the datafeed inside TradingView and how this adapts to your strategy.

&#x200B;

EDIT: Check top of this post for latest version of source code

&#x200B;

Let me know if you have questions or feedback... and special thanks to u/SilverDollarDan for helping me test this indicator.