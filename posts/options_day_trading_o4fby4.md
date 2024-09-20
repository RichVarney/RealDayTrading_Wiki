**Author**: u/HSeldon2020

**Posted on**: 2021-06-20

Original post: [https://www.reddit.com/r/RealDayTrading/comments/o4fby4/options_day_trading/](https://www.reddit.com/r/RealDayTrading/comments/o4fby4/options_day_trading/)

I went back and forth on how to write a post on Day Trading Options.  One can get very granular on this topic but ultimately it seemed to me that what most people wanted was a general guide.

I am going to assume that people here have a general understanding of what Options are, including the Greeks (*if not than this post will be of limited use to you as you* ***should not*** *be trading options unless you understand them).*  Thus, if the extent of your understanding is, "Use a Call when you think it is going up and a Put when you think it will go down..." you should probably skip the rest of this and learn the mechanics of Option Trading first.

While Options have many purposes, the ***primary purpose of using Options to Day Trade is - leverage.***  Otherwise you would simply use the stock directly which is far easier, and tends not to be subject to issues in liquidity.

Given this, the closer to parity with the underlying that you get on option pricing, the better (if you are buying options rather than selling them) -  ideally a stock worth $120 would have $100 Calls worth $20.  But since you are paying for time and volatility as well (not going to get into *Rho* here), you are getting charged a premium.  

Also, as a general rule, I do not hold Options over an earnings date.  Many people buy Calls or Puts on a stock right before earnings, and even when they get the move they were expecting their options did not increase in value - usually due to an **IV Crush**.  Option pricing is higher before earnings because there is more volatility around the predict future range of pricing for that stock.  If you add the price of the ATM Calls + Puts together you will get a rough idea of the +/- expected $ move post-earnings.  The larger that move is in proportion to the stock price, the higher the volatility.  Once those earnings are released, that volatility deflates, taking down the Option premium with it.    Earnings and the stocks response to earnings is simply too unpredictable, and also well outside the purview of Day Trading (as these occur pre or post-market).

This is how I Day Trade Options, it isn't the only way, it may not even be the *best* way, but it has worked for me - as always you need to explore what works best for yourself:

**1) High Delta - 1-3 WTE :**  I have a decent account balance but not 5,000 shares of NVDA "decent" and certainly not 5,000 shares of AMZN level.  So it is on stocks like these (usually priced over $500) that I will use to Options to Day Trade.  However, my NVDA may be your AAPL - so essentially, I am using Options when I cannot afford to get enough shares of the stock to make the trade worth it.  The temptation here is to go for the cheaper options which are going to be OTM or ATM - but I recommend against this.  The underlying position has to make a larger move to get those options close enough to parity to start overcoming what you paid in premium.  In the end your Risk/Reward is much better on the ITM options.  

*For example:  You want to go long AAPL using Options - You can either use the 2 weeks out options with a Delta of .8 or the ATM options that expire this week.*  

***Choice 1 - On Monday 6/21 you buy 5 123 Strike Calls on AAPL that expire 7/09 for $8.15 each, costing you $4,075.  Assuming the stock is at $130.46, you are paying .69 cent extra (123+8.15= $131.15-$130.46 = .69) in premium ($345). The Delta is .8 and Gamma is .03.***  

*Scenario A - The stock goes up $1.50 on Monday.  At the end of the day your option would now be worth (not using an Option Calculator so this is a rough estimate) - + $1.20 (Delta) + .015 (Gamma) - .01 (Theta) = $9.36 (roughly).  You made about $1.21 per contract, or roughly $605.*

*Scenario B - The stock stays the same - since the Theta on these options is only .06 you can hold them overnight with minimal loss ($30 total).*

*Scenario C - The stock declined $1.50 - as the stock declines you have room on the Delta to weather the decrease.  With the stock now at $128.96, your options would be worth roughly $6.85 (although a decline like this would most like increase volatility, further cushioning the drop) a loss of $1.30 per option, which*   
*is roughly $650 total.  However, you can still hold this option if you believe AAPL will recover enough in the next 2-3 weeks.*

***Choice 2 - On Monday 6/21 you buy ATM (130 strike) options on AAPL for $1.80.  Because they are cheaper, you get 23 of them for $4,140 (roughly the same cost as 5 options in Choice 1).  Assuming the stock is at $130.46 you are paying an extra $1.34 (130+1.80 = 131.80-130.46 = $1.34) in premium ($3,082).***  

*Scenario A - The stock goes up $1.50 on Monday.  At the end of the day your option would now be worth (not using an Option Calculator so this is a rough estimate) - + .78 (Delta) + .04 (Gamma) - .09 (Theta) = $2.53 (roughly).  You made about $.73 per contract, or roughly $1,679.*

*Scenario B - The stock stays the same - since the Theta on these options is .15 it now cost you $330 (roughly) to hold these overnight in additional time decay.* 

*Scenario C - The stock declined $1.50 - and you are now screwed.  Your options are worth about .75 cents each, you've lost roughly $2,415 on them, and if you hold them overnight they will continue to decline rapidly with time decay kicking in faster.*

Compare the Risk/Reward on both of these choices (*Choice 1 - $650/$605, Choice 2 - $2,415/1679)* \- and while these are rough guesses they aren't too far off from what would happen (a good Option Calculator can help here).  

**Choice 1 is better.**

*Less contracts - Higher Delta - More Time to Expiration.*

*Naturally this applies to Puts as well.*

You are looking for the following attributes in the stock you are want to Day Trade with Options:

*Strong Intra-Day Chart -* Ideally you want a stock that is strong vs the market (SPY) or weak vs the market (SPY), depending on if you are doing calls or puts.  The stock should be through any significant support/resistance (e.g. you do not want to do calls on a stock that is at 119.75 if their SMA 100 on the daily chart is at 120, you need to see it go through that and hold, first).  Relative volume usually needs to be above 1.5, and you should using VWAP to guide you as well.

*Strong Daily Chart -* Obviously the Daily chart will be important in telling you where significant support/resistance lies, but you also want to see an overall strong directional trend (bullish or bearish depending on your desired position).  I like to see HA candles in a continuation (e.g. flat bottomed) at least two in a row, and orderly trends without parabolic moves.  If you choose the right options and the stock hasn't violated any major areas of S/R, you can hold them overnight.

Your exit should be similar to the exit you would have used if you were trading the stock - the same principles apply.

**2*****)*** **Selling Premium -** This is rarely used a Day Trading method and for good reason, you are usually not going to get much bang for the margin you are spending if you only plan to flip them within the same day.  As a general rule I only sell Put on a stock I wouldn't mind owning at that price.  If I get assigned, I am perfectly happy with it, and if I keep the credit, I am also happy with that.  Overall, I  would not recommend this strategy for Day Trading as you are removing the primary benefit of selling premium - *theta decay.*

**3) Debit Spreads -** Call Debit Spreads(CDS') are an acceptable and widely used method to Day Trade Options, particularly among those that are risk adverse.  Here are some simple rules to follow that will help increase your odds:

*A) Find stocks that are making significant moves on that day - note, I am not talking about low float cheap morning gappers - rather I am referring to stocks like ROKU, ZM, ABNB or stocks like SNAP or NIO (these stocks are examples as they are capable of making and sustaining big daily moves, but their are many like these).  Basically you want a stock that is up more than 3-5% and holding those gains after an hour into trading.  They should be strong against the market, meaning if the market (SPY) is going down, this stock is staying strong either still going up or compressing.  There is usually at least one stock a day that qualifies, sometimes two or three.  Volume will of course taper off, but you do want to see Relative Volume over 1.5.*

*B) You are looking for the ATM Options to do the CDS' and they expire* ***this*** *week - so on Friday a stock like ROKU would have been perfect.  Around 10:25 SPY started to drop and ROKU continued to build on already strong gains.  In this case you would want something like the 360/365 or 360/362.5 spread.  You* ***never*** *want to pay more than 50% of the distance between the strikes.  If you were doing the 360/365 Spread, you want to pay less than $2.50 for that spread - obviously, the lower the better.* 

*C) The moment you put the spread in, you put in your order to receive your credit.  The day of the week matters here - On a Monday put in an order to get 10% profit, Tuesday would 15% profit, Wednesday - 20-25% profit, Thursday - 25%-40% profit, and Friday - 40% - 75% profit.  Rarely do I keep these until expiration unless the stock just blows through the strikes.  The reason the day matters is that these spreads only start to really move when you are close to expiration, it is difficult to get more than these percentages on those days.  If you took that ROKU spread on a Monday (360/365) and paid a $2.00 debit, you should look to get a $2.20 credit, but on Friday (since it is expiring that day) you could have gotten at least a $3.00 credit.*

I see traders that do this type of spread as their primary trade type, and by the end of the week they would have executed roughly 20-25 of them, with over a 95% win rate.  These are usually very safe spreads, but of course with low risk also comes low returns; however, they are consistent.  The stock doesn't have to make much more of an upward move to hit your target, and considering how strong they were to begin with it is very rare to miss with these.  Obviously there is always a stock like NVDA which on Friday if you did a 765/770 spread in the morning, it would have made perfect sense, but quickly reversed.  In those cases you should recognize the reversal and take the loss (e.g. if you paid $2.00 for NVDA, you should accept a $1.50 credit,  do not let the stock drop to where the credit is lower than that, just take the  loss).

**4) Lotto Trades**  \- These are the most fun, and are specific to Friday.  What you are looking for are stocks that have options expiring that day.  In the final hour of trading, the ATM options are going to be very close to parity.  So a stock that is $119.80 cents, will have $120 call options worth roughly .05-.10 cents with an hour left.  What you are looking for are stocks that are either relatively strong (or weak if you are doing this with Puts) to the market and a market tailwind (in the direction of your options).  You are looking for these options to get into the money, but even if they don't you can still do quite well with them.  On Friday for example, back to NVDA, it began dropping and the 750 Puts were worth roughly .20 cents with 25 minutes remaining and NVDA at around 755.  The stock was weak compared to the market (on the 5 minute chart when SPY went up, NVDA went down), and SPY began to drop with volume (tailwind).  If you bought 25 of those Puts ($500), within 10 minutes they would have been worth $3.60 an 1,800% increase.  Your $500 would now be worth $9000.    You won't find a better Risk/Reward play than lotto options.  However, note, you shouldn't be making large financial plays here as a many of these won't work, but the ones that do more than pay for the ones that did not.  Many times I take max loss on these; however, since these can turn very quickly, I have also taken that smaller loss only to see the stock soar or plummet in those final ten minutes.  Either way, these are really fun (I have a more detailed post on this).

So there you have it, like I said, there are many other ways to Day Trade Options (would like to hear them), but this is how I like to do it and it has worked well for me over the years.