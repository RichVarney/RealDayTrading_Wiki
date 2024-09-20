**Author**: u/HSeldon2020

**Posted on**: 2021-12-26

Original post: [https://www.reddit.com/r/RealDayTrading/comments/rp5rmx/a_new_measure_of_relative_strength/](https://www.reddit.com/r/RealDayTrading/comments/rp5rmx/a_new_measure_of_relative_strength/)

This post is going to be a bit of real-time mental workshop - in other words, I do not know how it will turn out, I am writing as I think.

Properly identifying ***Relative Strength and Weakness vs. SPY*** is one of the most powerful edges you can have while trading.  We know this, use this and have proven it.  Great....but something about it still bothers me.  

Essentially, what RS/RW really does is highlight *Institutional* activity within an equity.  Removing the market dynamics as a factor, the remaining price action is generally due to heavy buying and selling, on a level that retail traders can rarely achieve.  

However, we have all seen stocks have RS at one point, then lose it, then have it again, only to reverse and become RW at some point - all within the same trading day. 

To begin with I believe simply measuring the rate of change of a stock vs the rate of change for SPY in an inadequate method of measuring RS/RW.  At the very least ATR needs to be taken into account.  Currently we look at RS/RW as something like this:

RS = (S) P1-P2/P1 / (M) P1-P2/P1

Where:

(S) = Stock

(M) = SPY

P1 = Initial Price 

P2 = Price at end of Period

This alone gives an index.  So if you are looking at the RS for Stock A, and P1 = $100 and P2 = $101, then it moved $1 during the time period, which = a 1% change.  If during that period SPY went from $370 to $371, it will have also moved $1, but that would be a .2% change.  So Stock A over-indexes here by 500%, or a, 5.

Next let's quickly talk about the time period. I do not believe the time period examined should be the same for RS on a 5-minute basis as it is for a daily basis.  For the sake of this post, let's say that on a 5-min basis we want to look at the RS over the last 12 periods, or last hour.  And for a daily basis it would be the last 5 periods, or 5 days.

However, this type of analysis (whether you index it as I did, or simply do a subtraction as is normally done) has an inherent flaw - that can be illustrated as follows:

RATR  = (S) P(C)/ATR50 (H) / (M) P(C)/ATR(H)

RATR = Relative ATR

P(C) = Price change in the stock, defined above as P1-P2

ATR50(H) = ATR of the stock over the last 50 periods, with each period being 1 hour (which is the twelve 5-minute periods we measured RS), or in other words, what is the average price movement of the stock in any given hour over the last 50 hours of trading.  So let's say on average the stock in this example moves 20 cents an hour.  But in this case, it moved $1, so the stock moved 5 times more in the past hour than it usually does.

Next run the same equation on **SPY**, which let's say the ATR50(H) for SPY is 50 cents, meaning SPY moved 2 times greater than its hourly average.

Now we have:

RATR = (S) P(C)/ATR50 (H) / (M) P(C)/ATR(H) = 5/2 = 2.5

In other words, the stock moved five times greater than its' expected average, while SPY moved two times greater than its' expected average, so overall the stock moved 2.5X more than expected given SPY.

The first question here is, which number is a better indicator of *real* RS?  For example, let's say **SPY** moved $2.50 during the past hour, which is 5 times its' normal rate of 50 cents, and the stock moved $1 dollar during that period, which as before is also 5 times its' normal rate of 20 cents.  

If we used the regular definition of RS we would get a 1% change in the stock and a .06% change in **SPY**, which would be a RS of 1.66, *but* we also know that **SPY** moved five times more than average and so did the stock, so does the stock *really* have RS here, or did it just move at the same rate that **SPY** did?

There is a way to control for this as follows:

What is the *expected* change in the stock given the change in **SPY**?  If we are really controlling for **SPY** here, than if SPY moves 5 times its' norm, one would expect stocks to also move 5 times their norm, and deviation from that would be movement that is independent from **SPY**.

Thus, if **SPY** dropped $2 in an hour, and the hourly ATR of **SPY** is .50 cents, than **SPY** dropped 4X's more than would be expected.  So the *SPY Power Index* *(new term)* here is -4.0

That means the *Expected Change* in stocks would be -4.0X its' normal hourly ATR.  If a stock typically moves 10 cents in an hour, and the *SPY Power Index* is -4.0, one would expect that stock to drop 40 cents. Make sense?  

Back to our example, if the stock had an hourly ATR of .20 cents, than the *Expected* *Change* given the *SPY Power Index* of -4.0 would be -.80 cents.  Or:

*SPYPI \* SATR = -.80*

(SPY Power Index times Stock's ATR)

However, if the stock consolidated during this time, and had a net change of only -.20 cents, than it would have defied the *expected changed.*  

So the equation than becomes:

PC (-.20) - EPC (-.80) = .60 / SATR (.2) = 3.0

In other words, the stock dropped 20 cents, but it *should* have dropped .80 cents.  Meaning it was .60 cents stronger than expected.  If you divide that by the stocks ATR or .20, than it out-performed **SPY** by a multiple of 3.0

That gives the stock a RRS (Real Relative Strength) of 3.0

Another example: If **SPY** went up $1.50, than it has a *SPY Power Index* of 3.0, that means the stock in our example *should* have gone up .60 cents.  But what if it only went up .20 cents? Then:

.20 - .60 = -.40 / .20 = -2.0 

The stock would have a *Real Relative Strength (or in this case - Weakness)* of -2.0.  It should have gone up 60 cents, but instead it went up 20 cents, which is 40 cents below expectations, divided by the ATR of .20 cents equals -2.0.

Let's now take this even further - how do we combat the problem of stocks losing their RS/RW?  

What if a stock had one strong 5-min candle (a huge buy order perhaps) that accounted for most of the price change?  That would result in a false RS reading, right? 

If Stock A (ATR of .20 per hour) started at candle 1 at $100 and the following happened over 12 periods with each period representing 5 minutes vs. SPY (ATR of .50 per hour):

Period 1: $100 (ending price of candle), SPY $370.05

2: $100.02, SPY $370.15

3: $100.0, SPY $370.20

4: $ 100.04, SPY $370.30

5: $101.01, SPY $370.31

6: $101.02, SPY $370.46

7: $100.99, SPY $370.55

8: $101. 01, SPY $370.65

9: $101.02, SPY $370.60

10: $101.04, SPY $370.75

11: $101.03, SPY $370.88

12: $101, SPY $371

In this example, almost all of the gains came from candle 5, otherwise, the stock is basically flat, but as you can also see, SPY is steadily rising as well. But if you were to just look at the change in prices, the stock went up 1% and SPY only went up .2%.  If you were to do the *Real Relative Strength* it would look like *SPY Power Index* would be 2.0, which means the stock *should* have gone up .40 cents, however it went up $1, which mean the *Real Relative Strength* would be $1 - .40 = 60 cents / .20 = 3.0

However, since the stock remains flat after that jump up in price, as the candles tick on, eventually that Relative Strength number would drop, and if SPY continued to go up while the stock remained flat, it would in fact soon turn negative.  And there you have your case of a stock that seemingly had RS strength and lost it.

But now what if we took the *Real Relative Strength* as a constantly *rolling average* off the previous 12 candles?  Meaning, if you started looking at the stock at candle 12 above, you would see the stock went up $1 and SPY went up $1 over the past hour, and you would get either a RS reading as it currently stands of around 1.66 or a *Real Relative Strength* of 3.0.  **But** if you look at the average of all 12 candles before it then it might look something like this:

*Real Relative Strength* rolling (plugged in numbers assuming not much changed in the prior candles):

1  = -.05

2 = -.4

3 = -.3

4 = -.5

5 = 4.6

6 = 2.5

7 = 2.2

8 = 1.9

9 = 1.6

10 = 1.5

11 = 1.1

12 = .9

The *Rolling Real Relative Strength* here would 1.25 - In other words, the *Rolling Real Relative Strength* would penalize those one candle bursts, but would remain stronger and more consistent if the stock was moving in a consistent fashion relative to SPY.

This somewhat stream of consciousness might be confusing, but I am sure this is a far superior method to measure a stocks Relative Strength.

Thoughts? Additions? Critiques?  

Best, H.S.