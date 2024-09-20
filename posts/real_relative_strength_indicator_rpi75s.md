**Author**: u/WorkPiece

**Posted on**: 2021-12-27

Original post: [https://www.reddit.com/r/RealDayTrading/comments/rpi75s/real_relative_strength_indicator/](https://www.reddit.com/r/RealDayTrading/comments/rpi75s/real_relative_strength_indicator/)

I'm learning a lot from this sub, so I'd like to give back and contribute a little if I can.

I read through Hari's latest post on Real Relative Strength using ATR and have implemented his ideas in ThinkScript. It's actually easier than it sounds once you get down to just the simple formulas.  I've also taken the liberty of adding an optional colored correlation baseline to make it easy to see when a stock is shadowing or when it is independent of SPY.

There are many user concerns and suggestions in the comments, but I have only implemented Hari's original thoughts just to get the base concept down in code. I welcome some eyes on the code to make sure I've implemented it accurately. I consider this a starting point on which to expand on.

Original post: [https://www.reddit.com/r/RealDayTrading/comments/rp5rmx/a\_new\_measure\_of\_relative\_strength/](https://www.reddit.com/r/RealDayTrading/comments/rp5rmx/a_new_measure_of_relative_strength/)

&#x200B;

Below is a TSLA 5m chart. The green/red line you see is *relative* SPY (daily) overlaid. It is relative to TSLA here meaning when TSLA is above the (green) line then TSLA has *price* strength to SPY, and when TSLA is below the line (the line turns red) then TSLA has *price* weakness to SPY. You can see this relationship in the bottom "Relative Price Strength" indicator as well, although the indicator is showing 1 hour rolling length strength. This is based only on price percentage movement.

Now compare the "RelativePriceStrength" indicator (bottom) to the new "RealRelativeStrength" indicator above it. This new one is ATR length-based off of Hari's post.

<img src="cache/images/22aaa390d515c9e065112850dcc0b518.png" alt="Reddit Image">

On first impression - the output very closely resembles what I see in my regular length-based RS/RW script. The differences are obviously due to this being an ATR length-based script and the other being price percentage based, but the general strong RS/RW areas are similar to both.

Here is a link to the ToS study: [http://tos.mx/FVUgVhZ](http://tos.mx/FVUgVhZ)

And the basic code for those without ToS that wish to convert it to PineScript:

`#Real Relative Strength (Rolling)`

`#Created By u/WorkPiece 12.26.21`

`#Concept by u/HSeldon2020`

&#x200B;

`declare lower;`

&#x200B;

`input ComparedWithSecurity = "SPY";`

`input length = 12; #Hint length: value of 12 on 5m chart = 1 hour of rolling data`

&#x200B;

`##########Rolling Price Change##########`

`def comparedRollingMove = close(symbol = ComparedWithSecurity) - close(symbol = ComparedWithSecurity)[length];`

`def symbolRollingMove = close - close[length];`

&#x200B;

`##########Rolling ATR Change##########`

`def symbolRollingATR = WildersAverage(TrueRange(high[1], close[1], low[1]), length);`

`def comparedRollingATR = WildersAverage(TrueRange(high(symbol = ComparedWithSecurity)[1], close(symbol = ComparedWithSecurity)[1], low(symbol = ComparedWithSecurity)[1]), length);`

&#x200B;

`##########Calculations##########`

`def powerIndex = comparedRollingMove / comparedRollingATR;`

`def expectedMove = powerIndex * symbolRollingATR;`

`def diff = symbolRollingMove - expectedMove;`

`def RRS = diff / symbolRollingATR;`

&#x200B;

`##########Plot##########`

`plot RealRelativeStrength = RRS;`

`plot Baseline = 0;`

&#x200B;

`RealRelativeStrength.SetDefaultColor(GetColor(1));`

`Baseline.SetDefaultColor(GetColor(0));`

`Baseline.HideTitle(); Baseline.HideBubble();`

&#x200B;

`##########Extra Stuff##########`

`input showFill = {Multi, default Solid, None};`

`plot Fill = if showFill == showFill.Multi then RealRelativeStrength else Double.NaN;`

`Fill.SetDefaultColor(GetColor(5));`

`Fill.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);`

`Fill.SetLineWeight(3);`

`Fill.DefineColor("Positive and Up",` [`Color.GREEN`](https://Color.GREEN)`);`

`Fill.DefineColor("Positive and Down", Color.DARK_GREEN);`

`Fill.DefineColor("Negative and Down",` [`Color.RED`](https://Color.RED)`);`

`Fill.DefineColor("Negative and Up", Color.DARK_RED);`

`Fill.AssignValueColor(if Fill >= 0 then if Fill > Fill[1] then Fill.color("Positive and Up") else Fill.color("Positive and Down") else if Fill < Fill[1] then Fill.color("Negative and Down") else Fill.color("Negative and Up"));`

`Fill.HideTitle(); Fill.HideBubble();`

`AddCloud(if showFill == showFill.Solid then RealRelativeStrength else Double.NaN, Baseline,` [`Color.GREEN`](https://Color.GREEN)`,` [`Color.RED`](https://Color.RED)`);`

&#x200B;

`##########Correlation##########`

`input showCorrelation = yes;`

`def correlate = correlation(close, close(symbol = ComparedWithSecurity), length);`

`plot corrColor = if showCorrelation then Baseline else Double.NaN;`

`corrColor.AssignValueColor(if correlate > 0.75 then CreateColor(0,255,0)`

`else if correlate > 0.50 then CreateColor(0,192,0)`

`else if correlate > 0.25 then CreateColor(0,128,0)`

`else if correlate > 0.0 then CreateColor(0,64,0)`

`else if correlate > -0.25 then CreateColor(64,0,0)`

`else if correlate > -0.50 then CreateColor(128,0,0)`

`else if correlate > -0.75 then CreateColor(192,0,0)`

`else CreateColor(255,0,0));`

`corrColor.SetPaintingStrategy(PaintingStrategy.POINTS);`

`corrColor.SetLineWeight(3);`

`corrColor.HideTitle(); corrColor.HideBubble();`

&#x200B;

&#x200B;

&#x200B;

Update: Added PineScript version

&#x200B;

<img src="cache/images/b4ab6f995765fbfa1a971017e87a0260.png" alt="Reddit Image">

`// This source code is subject to the terms of the Mozilla Public License 2.0 at` [`https://mozilla.org/MPL/2.0/`](https://mozilla.org/MPL/2.0/)

`// © WorkPiece 12.28.21`

`//@version=5`

&#x200B;

`indicator(title="Real Relative Strength", shorttitle="RRS")`

`comparedWithSecurity = input.symbol(title="Compare With", defval="SPY")`

`length = input(title="Length", defval=12)`

&#x200B;

`//##########Rolling Price Change##########`

`comparedClose =` [`request.security`](https://request.security)`(symbol=comparedWithSecurity, timeframe="", expression=close)`

`comparedRollingMove = comparedClose - comparedClose[length]`

`symbolRollingMove = close - close[length]`

&#x200B;

`//##########Rolling ATR Change##########`

`symbolRollingATR = ta.atr(length)[1]`

`comparedRollingATR =` [`request.security`](https://request.security) `(symbol=comparedWithSecurity, timeframe="", expression= ta.atr(length)[1])`

&#x200B;

`//##########Calculations##########`

`powerIndex = comparedRollingMove / comparedRollingATR`

`RRS = (symbolRollingMove - powerIndex * symbolRollingATR) / symbolRollingATR`

&#x200B;

`//##########Plot##########`

`RealRelativeStrength = plot(RRS, "RealRelativeStrength",` [`color=color.blue`](https://color=color.blue)`)`

`Baseline = plot(0, "Baseline",` [`color=color.red`](https://color=color.red)`)`

&#x200B;

`//##########Extra Stuff##########`

`fill(RealRelativeStrength, Baseline, color = RRS >= 0 ?` [`color.green`](https://color.green) `:` [`color.red`](https://color.red)`, title="fill")`

&#x200B;

`correlated = ta.correlation(close, comparedClose, length)`

`Correlation = plot(0, title="Correlation", color = correlated > .75 ? #00FF00 : correlated > .50 ? #00C000 : correlated > .25 ? #008000 : correlated > 0.0 ? #004000 :correlated > -.25 ? #400000 :correlated > -.50 ? #800000 :correlated > -.75 ? #C00000 :#FF0000, linewidth=3, style=plot.style_circles)`