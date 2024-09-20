**Author**: u/HurlTeaInTheSea

**Posted on**: 2022-09-08

Original post: [https://www.reddit.com/r/RealDayTrading/comments/x9dwv0/real_relative_strength_to_sector_indicator_auto/](https://www.reddit.com/r/RealDayTrading/comments/x9dwv0/real_relative_strength_to_sector_indicator_auto/)

This indicator shows the stock, sector and market RS/RW all in one place. It's a faithful but very late \[1\] adaptation of u/lilsgymdan's TC2000 indicator in his video \[2\]\[3\]. See how they compare (this indicator is on the right):  


<img src="cache/images/1b3a44af76e9423b5c87e6ed4bcbcb3c.png" alt="Reddit Image">

As many traders here know by now, sector RS/RW analysis gives us these insights:

* Is the stock simply being driven by the sector?
* Is the stock a standout from its sector?
* Is the sector strong or weak against the market?
* Is a sector rotation happening?

By choosing the strongest (weakest) stocks in the strongest (weakest) sectors, we further stack things in our favor.

**How to Read This Indicator**

This indicator typically shows two or more plots:

* the power index the stock (white in bold)
* the power index of the market (gray)
* the power index of each matching sector, if any (color)

How does the power index \[4\] relate to RS/RW? If the stock's power index is above (below) the market/sector, it has real relative strength (weakness). If we subtract the market's power index from the stock's, we get the original RealRelativeStrength (RRS) indicator \[5\]. Breaking things down into their constituent power index values tells us whether that strength comes from i) flying in a rising market, ii) flying in a falling market or iii) treading water in a sinking market. It means we get additional context behind the green hills and red valleys of the RRS indicator.

For example, here is today's (2022-09-08) 5m chart of TSLA with this indicator in the middle and RRS at the bottom. We can see the midday strength was from not tanking with the market, while strength at day's end was pure outperformance with respect to the Consumer Disc. sector and the market.  


<img src="cache/images/62a07e76f33a8c68bf56a3dc276deeb5.png" alt="Reddit Image">

**Where Sectors Come From**

Sector plots are drawn from the SPDR ETFs that represent the 11 GICS sectors:

* Communication Services: XLC
* Consumer Discretionary: XLY
* Consumer Staples: XLP
* Energy: XLE
* Financials: XLF
* Health Care: XLV
* Industrials: XLI
* Materials: XLB
* Real Estate: XLRE
* Technology: XLK
* Utilities: XLU

I've programmed in S&P 500 stocks to auto-select the right sector. I also added Semiconductors with SMH as the baseline. You're free to add/remove/change sectors and mappings - see the post footer for details.

Since all sectors are already in the script, I thought it would be useful to have a "show all" toggle for analyzing sector rotations in terms of RS/RW.

<img src="cache/images/a86ee3550cbe541868cbbdf85e2ba969.png" alt="Reddit Image">

As always you're free to use/change/improve the scripts however you like. I hope you'll share your improvements with the community.

**Script Features**:

* Automatic sector selection for S&P 500 stocks (as of 2022-08-29)
* Customize sector colors with matching sector tags
* Toggle to always show individual sectors or ALL sectors
* Add new sectors and mappings without coding - up to 20 slots (TV only)
* Customize the two RealRelativeStrength period params (Defaults to 12/12)

**TradingView (TV) script source**: [https://www.reddit.com/user/HurlTeaInTheSea/comments/x9dqe4/real\_relative\_strength\_to\_sector\_indicator\_auto/](https://www.reddit.com/user/HurlTeaInTheSea/comments/x9dqe4/real_relative_strength_to_sector_indicator_auto/)

**Thinkorswim (TOS) script source**: [https://www.reddit.com/user/HurlTeaInTheSea/comments/x9dr3c/real\_relative\_strength\_to\_sector\_indicator\_auto/](https://www.reddit.com/user/HurlTeaInTheSea/comments/x9dr3c/real_relative_strength_to_sector_indicator_auto/)

**How to Add New Sectors and Mappings**

**TV**. Go to the indicator's settings page and add the sector symbol and a comma-separated list of symbols that should map to your new sector. Or look in the script for the "Sector Symbol Definitions" section to permanently add your changes. It should be very straightforward.

**TOS**. Unfortunately the TOS scripting language is very limiting and I couldn't find a nice solution. The most you can do from the study settings screen is change the symbol that represents an existing sector. For advanced changes you'll need to code your way through. But I think you'll figure out very quickly where to make your changes by looking at how I added the semiconductors sector.

**References**

\[1\] u/hariseldonSTAN has already written a similar indicator for TOS earlier: [https://www.reddit.com/r/RealDayTrading/comments/wb3x7c/relative\_strength\_to\_stock\_and\_sector\_indicator/](https://www.reddit.com/r/RealDayTrading/comments/wb3x7c/relative_strength_to_stock_and_sector_indicator/)

\[2\] lilsgymdan's video explaining how to use original TC2000 version of this indicator: [https://www.reddit.com/r/RealDayTrading/comments/vc12j6/why\_your\_short\_didnt\_work\_yesterday/](https://www.reddit.com/r/RealDayTrading/comments/vc12j6/why_your_short_didnt_work_yesterday/)

\[3\] TC2000 RRS indicator by lilsgymdan: [https://www.reddit.com/r/RealDayTrading/comments/rrfpud/did\_i\_make\_a\_better\_tc2000\_rsrw\_indicator/](https://www.reddit.com/r/RealDayTrading/comments/rrfpud/did_i_make_a_better_tc2000_rsrw_indicator/)

\[4\] HSeldon2020 explains power index: [https://www.reddit.com/r/RealDayTrading/comments/rp5rmx/a\_new\_measure\_of\_relative\_strength/](https://www.reddit.com/r/RealDayTrading/comments/rp5rmx/a_new_measure_of_relative_strength/)

\[5\] Original RealRelativeStrength indicator by u/WorkPiece: [https://www.reddit.com/r/RealDayTrading/comments/rpi75s/real\_relative\_strength\_indicator/](https://www.reddit.com/r/RealDayTrading/comments/rpi75s/real_relative_strength_indicator/)