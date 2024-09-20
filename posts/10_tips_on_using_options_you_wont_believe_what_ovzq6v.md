**Author**: u/HSeldon2020

**Posted on**: 2021-08-01

Original post: [https://www.reddit.com/r/RealDayTrading/comments/ovzq6v/10_tips_on_using_options_you_wont_believe_what/](https://www.reddit.com/r/RealDayTrading/comments/ovzq6v/10_tips_on_using_options_you_wont_believe_what/)

Sorry about the title, couldn't resist (although I bet you will check #9)

I have been asked about this a lot recently - And I will try to keep this as basic as possible.

**1) Know How much premium are you really paying:** 

**For In-The-Money Options:** (*Strike Price + Option Price) - Stock Price = Premium being paid over real value.*

**For Out-Of-The-Money Options:** *Option Price = Premium being paid*

**2) Stop thinking of Delta as "Probability":**  

***You will often hear that a stock with a Delta of .85 (arbitrary) has an 85% likelihood of finishing In-The-Money.***  

Yes this may be true historically, but it also has little pragmatic value for you, as it is no way references the chance you will be in *profit* and while your platform can run a profit probability analysis, it subject to an ever changing market.  Instead just think of Delta as this: *For every dollar the stock moves, this option will move .85 cents (again arbitrary).*

**3) Stop Buying Out-Of-The-Money Options:** 

Let's say you find the daily chart for **AMD** Bullish (it is btw) and want to buy call options on it now that earnings has past.  The first thing you want to do is give yourself some breathing room.  Look for an expiration of Aug 13th at the *earliest.*  Next you want to look for a Delta of *at least* .7 or higher.  Remember, the higher the Delta, the lower the Theta, and when buying options, Theta is not your friend.  And since you are most likely using the options for leverage you want to mirror the stock price moves as close as possible.

Yes, I know the Out-Of-The-Money options are cheaper, and you can get many more contracts - *they are cheap for a reason.* **You aren't getting a deal here, what you are doing is gambling.**

Some notable exceptions to is would be the rare times you can find an ATM option running at parity - meaning the stock price is $100.50 and the $100 strike is going for .50 cents.  This gives you 100% leverage.  Another exception is Lotto Friday's and I have another post dedicated to that.

**4) Make Sure Your Option Has Volume:**

If you buy an option that has extremely low volume you are most likely paying the penalty of a wide bid-ask spread.  There is also a reason that option has low volume - nobody wants it.  

**5) Don't Sell A Put Unless You Want To Own The Stock:**

Selling Premium is one of the smarter moves you can make when using options.  Whenever possible you want to be the "house", and writing option contracts makes you just that.  However, too many people get burned with the Wheel Strategy which is akin to Martingale strategy in gambling (keep doubling your bet until you win) - it works until it doesn't and when it doesn't you get burned, badly.  Still, if you sell Puts, always have the attitude that you *want* the stock at that price - if you just keep the credit, great - but that is not the goal.  

**6) For The Love Of God Stop Buying Options Over Earnings**

Yes there is always that one person that is going to post that gain-porn about how they had 200 OTM Puts on AMZN, but the *overwhelming majority* who try this play - lose.  There is one thing you absolutely know for certain - the IV is going to drop (crush) and drag down the over-inflated contract price with it - which means that not only do you have to guess correctly on the stocks reaction to earnings (e.g. beating earnings expectations does not always lead to an increase in stock price), but you also have to get the magnitude of that move correct.  Since IV is dragging down the price of the option, the change in stock price has to be strong enough to overcome that. 

*There are some exceptions here, and if you are experienced enough then you know them and do not need this post.* 

**7) Spreads Are Good - Get To Know Them**

It is not always as simple as thinking the stock is going up or going down.  There are degrees of magnitude, degrees of uncertainty, the overall market, the overall sector, etc.

I will give a few situations - 

*Situation 1:* Stock XYZ is at $100, it has strong support at $97 in the SMA 50, $96.50 in the SMA 100 and $95.75 in horizontal support. You are bullish on the stock but want a safe play - 

*Use an Out-of-the-Money Put Credit Spread around 95/94 and make sure you get a 25% ROI (this translates into making you sure get 20 cents credit for the spread for every $1 between the strikes).  To get this credit you will most likely have to go out 3-4 weeks out in expiration, but you really do not want to go out further than that.  The stock can go up, stay the same or even go down some and this spread will still maintain maximum profit as long as XYZ stays above $95.*

*Situation 2:*  Stock XYZ is at $350, opening up $8 that day on a bullish market - you believe it will continue to go up but the premium to buy calls is high.

*Use a Call Debit Spread of $350/$355 for a debit of less than $2.50 (50% of the strike price difference) that expires this week.  Immediately put in an order for a Credit (roughly 10-20% higher on Monday-Tuesday, 20%-40% higher on Wednesday-Thursday, and 40%+ on Friday).*

Maybe you are neutral on a stock and want to use an Iron Condor/Butterfly?  In other words no matter what your outlook there are typically spreads that accommodate it.  I highly recommend going here to learn about all of them: 

[https://www.optionsplaybook.com/option-strategies/](https://www.optionsplaybook.com/option-strategies/)

*Personally I think the Poor Man's Covered Call or Fig Leaf is an underused strategy - an example of that would be buying the Sept 2022 AMZN 2950 Call at $625 and then every week selling a .10 Delta call for $10.  I would not advocate for this until AMZN finds support btw.*

**8) Learn ATR - Average True Range and Bollinger Bandwidth:**

Basically you want to know how much the stock moves over a given time period.  The ATR will tell you how much +/- the stock moves over X number of periods.  BBandwidth will indicated how wide or narrow the stock's volatility currently is, recognizing that as the distance between the bands gets more narrow, the higher likelihood that volatility will soon increase. 

Why is this important?  Well say you want to do a covered call on your stock that you own 500 shares of at $200 a share.  The 5-day ATR on this stock is +/- $2.50, which means that by the end of the week the stock will be within a range of $197.5 and $202.50 - so you would probably want to sell your call at the very least over $202.50.  

**9) Stocks vs Options:**

In general, stock is better - you can buy at the bid, sell at the ask, and do not have to worry about price decay.  And if you have unlimited funds, you would probably always use the stock as your instrument of choice if you have a clear directional bias.

Generally though, the decision to use an option over stocks comes down to two things: **Leverage** or **Strategy**.  Strategy we already discussed in the section on spreads.  There are sometimes where you are bullish on a stock but unsure about the magnitude or you may believe the stock will not move much overall and the high volatility is not justified.  All of these analytical findings have a home in a corresponding spread that are better fits than just going long or shorting the stock.   However, most people buy options for the **Leverage**.  

Actually, most people are buying OTM options on volatile stocks hoping for a payday (e.g. the $60 strike Calls on AMC for Aug 13th are only .50 cents??  To. The. Moon.!!  200 Contracts (e.g. $10,000).  It should go without saying, but I will say it anyway - Don't do that.  Honestly.  Go to a casino instead with that money.

The rest of you are looking at a stock like **HD,** you like the technical setup and are bullish on the stock (this is just an example, **HD** really should break through $330 before you go long).  However, you can't buy many shares of a stock valued at $328, so how would you play this?  Here are some ways:

*A) Buy* ***Straight Calls*** *at the 320 strike that expire on 8/13 for $10. The current price of* ***HD*** *is $328.19, meaning you are only paying $1.81 in premium.* ***HD*** *reports earnings on 8/17 meaning the calls will retain their value as the IV is likely to increase as you get closer to expiration compensating somewhat for time decay.  And the Delta is .74, meaning you will get decent leverage for every $1 move up in the price of the underlying.  Plus, the theta of -.16 is fairly modest, showing a daily decrease of 16 cents a day.*  

*B) Do a* ***Put Credit Spread*** *of $225.50/$220 for .56, which gives you a 28.86% ROI.  This is a fairly risky play as you are only relying on the horizontal support at $324, and the benefit of the first option (holding the value) becomes the detriment of this one as this spread is likely to drop in value much slower.  However, a drop in* ***HD*** *below this support level most likely would be a serious breakdown in the sector which would allow you to leg out.  The reduced amount of time (only two weeks) is also in your favor here - however, this is a* ***risky*** *play.*

*C) Do a* ***Call Debit Spread*** *of $330/$335 that expires 8/6 for a debit of $1.50.  If* ***HD*** *opens higher on Monday I doubt you will get this price, and if it opens lower you most likely would not want to use this strategy.  But if* ***HD*** *opens up $3, and you can get this spread for less than $2.50 debit, it is still a decent option (pun intended and unavoidable at the same time).  This allows you to basically buy the ATM call for a reduced price, and limits your risk.  However, it also caps your upside.*  

Out of these three options, I would chose A.  Once again, **HD** has not yet shown confirmation of a bullish trend, so I am just using it as an example.  But this is the thought process you should use when deciding between buying a stock and an option, particularly if you are Day Trading.

**10) The Market**

While this list is not in any particular order, the **Market** should be of primary concern.  Just like with stocks, you need always be cognizant of what the market is doing and if your position is running *with* or *counter* to the market.  You also should be looking at the sector ([Finviz.com](https://Finviz.com) has an excellent graphic that shows the S&P 500 stocks by sector, color coded for the day, and adjustable by time frame), and how the underlying is performing relative to other stocks in the same arena.  Keep an eye on VXX as well, as that is a reflection on option pricing.   Overall though, much like stocks, you only want to choose options on underlying properties that have strong *Relative Strength* or *Weakness* to **SPY**, irrespective of whether that stock is in that index or not.  If on Monday **SPY** opens flat and **HD** is up $3, that is an earlier indication that **HD** has strong *RS.* However, if on Monday **SPY** opens up $2 and **HD** is up $3, **HD** may not have good *RS* and may only be reflecting the bullish conditions on the day.  Watch how the stock moves relative to **SPY** and get a good sense of its' *RS/RW* before deciding on an option strategy.  *Remember - Relative Strength/Weakness* ***is not*** *RSI or Beta*.  

I hope these were helpful.  Obviously they assume a certainly underlying (pun again) knowledge on options (the greeks, spreads, etc.).

All the best, 

H.S.