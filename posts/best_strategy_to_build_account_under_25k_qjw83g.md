**Author**: u/HSeldon2020

**Posted on**: 2021-10-31

Original post: [https://www.reddit.com/r/RealDayTrading/comments/qjw83g/best_strategy_to_build_account_under_25k/](https://www.reddit.com/r/RealDayTrading/comments/qjw83g/best_strategy_to_build_account_under_25k/)

Even though this is a Day Trading sub I recognize that many of you are trying to get above $25K currently.   Many of you have told me that you would like to see some more strategies for accounts that are below the PDT level, so yesterday I posted one, and now here is another:

First let me qualify this - there are many ways one can define "best".  For the purposes of this post, "best" is defined as the most *consistent* method with the *highest rate of success*.  

The drawback to the method I am about to outline?  It is slow and definitely not "exciting".  Not necessarily a "drawback", but I suppose it is to some.

For sure there are many quick ways to build an account, but all of them come with a significant level of risk.  I can do other posts that detail out what those are - but first let's talk about this one:

**OTM Bullish Put Spreads**

A *Bullish Put Spread* by definition is executed when you sell a Put option and then Buy a Put Option at a lower strike price for the same expiration date.  An example:

**Stock**: XYZ 

**Current Price**: $200

You Sell the $200 Put (expiring 11/5)  and Receive $10 in Credit

You Buy the $195 Put (expiring 11/5) and Pay $7 

**Total credit** = $3 (i.e. $300) per contract

Simple enough - you received more money than you spent, so you get a credit for the trade.  Also if you were to just Sell the $200 Put Contracts naked, not only would that be very risky, but it would take up a significant amount of margin.  When you go long the $195 Puts you have capped your loss to $5 a share (minus the credit received).

There are three potential outcomes to the trade:

**Stock XYZ finishes the week above $200**:  In this case, both the 200 Put you sold and the 195 Put you bought expire worthless.  Thus, you keep the entire $300 credit per contract.

**Stock XYZ finishes the week below $200 but above $195 - Let's say $196:**  This is the riskiest outcome with these spreads, as your $195 Put expires worthless, but your $200 Put is worth -$4.  You would owe $400 per contract minus the $300 your received in credit = net loss is $100 per contract.  This is risky because if you do not close the $200 Put before expiration it will get assigned.

**Stock XYZ finishes the week below $195 - Let's say $190:**  This represents a max loss scenario for the trade.  Your $200 Puts are worth -$10 and your $195 Puts are worth $5.  The broker uses one contract to cancel out the other (i.e. exercising $200 Puts means you are buying 100 shares of **XYZ** at $200 a share, exercising the $195 Put means you are selling **XYZ** at $195 a share - total loss of $5 a share, minus the $3 credit = net loss is $200 a contract (which is your max loss here).

Now that you get the idea behind it (hopefully), here is the twist on this method:

Under certain market conditions you can create these spreads with the right combination of *probability of success* and *ROI* on the trade to execute a strategy that has the highest chance of building your account.

What are those market conditions?  You need a pullback in **SPY** to begin with - much like we had at the end of September/Early October.  Next you need to see **SPY** recover to the point that you have confidence we have returned to a bullish pattern - October 18th would be a good example of this, second day in a row where **SPY** opened and closed above the SMA 50.

Next you need to find strong stocks, with bullish daily charts that doesn't have earnings for the next 3-4 weeks - look at **NVDA** on 10/18 - that would be a perfect candidate.  Nice gap up two days prior, held the gap, with a convincing bounce off the SMA 50.  Look for stocks that are above their SMA's 50, 100 and 200, and have HA continuation candles on the Daily chart.  *I stress again - make sure there are no earnings announcements for at least 3-4 weeks.*  

Now you want to find your short strike price (this is price you will be selling your short Put).  You are looking for a price that has at least two major areas of support above it.  You are trying to get as close as you can to the current price, but still far enough away that you would need a significant drop to occur in order to endanger your spread.  For **NVDA** on 10/18 that would be a price of roughly $210.  That price is below the both the 50 SMA *and* the gap up - meaning in order for **NVDA** to drop below $210, it would have to break-through both those areas of support.  

Stocks do not just drop below their major support lines without a significant technical breakdown in either the market or the stock itself, and the likelihood of that happening within a 3-4 week timeframe is very slim.  

So in this example (and I am not using a current day example because the market setup is not right for this play, but it may be very soon), the $210 strike would be your Short Put.  Most likely this would have been a Delta of roughly -.15 to -.20 on your Option Chain.

Next up is the credit you need to receive for the trade.  You are looking for 20 cents credit for every dollar between the strikes (or 10 cents for every 50 cents between the strikes).  You will find there is not much difference between doing a $210/$205 *Bullish Put Spread* for a $1 Credit or a $210/$207.5 *Spread* for a .50 cent credit.  Both scenarios give you a ***25% ROI*** on your money.  Meaning in the $210/$205 Spread you are putting up $4 in Risk to make $1 in Profit.   Normally, this is not a good deal for you, right?  

*Here's the kicker*: as long as your spread has a win probability of more than 80% you will make money.  If you did this trade 100 times and it worked 80 times - you made $80 (+$1 per win), and it didn't work 20 times (-$4 per loss), you lost $80 - breakeven.  So you need to be successful more than 80% for this play to be worth it.  The 20 cents credit per dollar in the spread figure is calculated because if done correctly these plays work 95% of the time, more than enough to be very successful with the method.

In order to get that type of credit that far out-of-the-money you will usually need to go 3 to 4 weeks out.  

Remember, time decay is key to these spreads - every day that passes where the stock price stays above the short strike price, these options are losing value (which is a good thing in a credit spread).  The closer you get to the expiration date the faster Theta does its job.  

In 2020, we did over 300 of these spreads with a win rate above 96.5%.  Here's why:

Let's say you took the **NVDA** spread which expired in three weeks (11/5), when the stock was at a price of $220 a share.  The stock can drop $9 a share and your spread still makes full value.  The stock can stay right at $220 and your spread still gets full value.  Or the stock can go up and your spread still gets full value.

The only way your spread gets into danger is if it dropped more than $10 a share, broke through two levels of support, and remained below $210 on expiration day.  However, even if that happens, this method is designed with a parachute - *legging out*.  

Keep in mind, *legging out* of *Bullish Put Spreads* is dangerous, and need to be done correctly - if you are new to this, or somewhat unsure of how to *leg out,* it is better just to take the loss, but, for the sake of being comprehensive, here is how:

Let's say you get unlucky, and it is one of those 5-10% of the times that the stock or the market has a major technical breakdown before your expiration date and **NVDA** is experiencing a significant drop.  If **SPY** is in the red and your stock is falling below your short strike, you can buy back the short strike and let the Long Put run until you match the price you bought back the Short Put.  What would that look like?  Something like this:

On the week of expiration, **NVDA** drops to $215.  You are getting a bit worried, but it is Monday and you are still $5 above the short strike.  On Tuesday the market opens lower again, and **NVDA** remains weak, now dropping to $210.50.  You are hoping support holds - but suddenly you see **NVDA** break support and fall below $210.  

In that case, you can either close the trade for a loss of roughly $1(at this point your $210 Put is most likely worth around $4 and your $205 Put is worth around $2 - meaning you lose $2 in the difference, but you still have your $1 credit - total loss is $1)  This means even though you took a loss, you did not take the full loss of $4 that you could have taken.

Or you can buy back your short strike (for $4) and now your Long Put of $205 which is worth $2 should continue to go up in value as **NVDA** drops.  This is why it is important that you have both a weak market and weak stock.  Because if the market and/or stock reverses, and **NVDA** stops dropping, you risk losing both the $4 you spent to buy back the Short Put and the $2 in value of the Long Put taking your max loss from $4 to now $6.  However, if you time it right - you can put in a sell order of the Long Put ($205) for the same price you bought back the Short Put ($210) - $4.  If you hit that target than the two will cancel each other out and you get the full value of the trade - $1 or $100 per contract.  Obviously you need to monitor this closely - if you see **NVDA** (in this example) drop more and the $205 Puts are worth $3.50 now, but the stock finds support and begins to rebound, you might want to close the trade, take the .50 cent loss on the difference, plus the $1 credit original received = .50 cent total profit.

A $10,000 account can have 4 of these types of spreads running at the same time, each spread worth roughly $500 in profit (or 2 spreads each worth roughly $1K in profit), with $1K left over for cushion.  10 Contracts for a Profit of $1 each is worth $1K in profit and takes $4K in margin.  

If you manage them correctly, than most of the time you will increase your balance to $12K in the first month.  The next month you can do 3 of these for $1K each (or 6 for $500 each) with $2K in cushion and get to $15K.  Etc..Etc..

 It may take a few readings of this to fully get it, but the next time you see the market go into a sustained drop, and then find support you should start looking for good *Bullish Put Spread* candidates*.  Be patient and make sure SPY is bouncing back up as these spreads do not work when SPY is in a bearish stretch.* 

Best, H.S.

Follow us on Twitter: https://twitter.com/RealDayTrading