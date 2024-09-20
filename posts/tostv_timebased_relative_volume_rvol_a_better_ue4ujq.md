**Author**: u/HurlTeaInTheSea

**Posted on**: 2022-04-28

Original post: [https://www.reddit.com/r/RealDayTrading/comments/ue4ujq/tostv_timebased_relative_volume_rvol_a_better/](https://www.reddit.com/r/RealDayTrading/comments/ue4ujq/tostv_timebased_relative_volume_rvol_a_better/)

Among the helpful content on this sub, I was recently inspired by /u/lilsgymdan's excellent post on important trading criteria. One of which is making sure a stock has high relative volume to confirm price action with TC2000's Volume Buzz.

Original post: [https://www.reddit.com/r/RealDayTrading/comments/ua7rm4/these\_trade\_criteria\_work\_really\_really\_well/](https://www.reddit.com/r/RealDayTrading/comments/ua7rm4/these_trade_criteria_work_really_really_well/)

My research tells me "Volume Buzz" works by multiplying average volume by the percentage of the trading day. But then I came across StockBeep's post on the RVol indicator used in their screener (which Hari uses in his "How to Find Stocks to Trade" video).

What's great about RVol is it accounts for the **intraday volume profile** to get a "truer" relative volume for any time of day.

RVol divides the cumulative volume up to the current time by the average cumulative volume up to that time of day. Above (below) 1.0 means higher (lower) relative volume. I've scripted RVol to the exact specs by StockBeep. Take a look at how it reacts to FB's false earnings leak on 2022/04/27:

&#x200B;

<img src="cache/images/61749bc14f01987df90492ca7bb41441.png" alt="Reddit Image">

We see an abrupt change in volume midday that caused relative volume to end over 50% higher than average EOD. What's great is you can clearly see the **direction** of relative volume. For FB, it continued to rise after the spike, leveled off from 14:30-15:30 then rose again near EOD.

It's important to look at direction because a single high volume spike can prop up high RVol for the rest of the day. In theory, rising RVol, rising price and exhibiting RS should be a positive signal for the stock - macro market allowing.

I'm very interested in your thoughts on RVol, whether you've used this or something similar. Hope you'll share any improvements/findings with the community.

**Script features (TOS & TV)**:

* Customize high volume highlight threshold like in StockBeep's screener
* Customize highlight color or color based on previous close
* Customize days moving average (default is 5 to match StockBeep)
* Works on D1 (turns into classic relative volume)
* Painfully tested with DST changes, PM/AH bars, time zones, thin-volume tickers

**TOS**:

    # This source code is subject to the terms of the MIT License at https://opensource.org/licenses/MIT
    # /u/HurlTeaInTheSea v1.1
    
    # v1.1 (2022-12-27)
    # - Fixed bug where days before first bar are counted (if any)
    # - Added warning if not enough days in history
    
    # v1.0 (2022-04-28)
    # - Initial release
    
    # Intraday Relative Volume (RVol) indicator:
    # https://stockbeep.com/blog/post/how-to-calculate-relative-volume-rvol-for-intraday-trading
    
    declare zerobase;
    declare lower;
    
    # still works on higher timeframe but it's not a "day" average anymore, so throw error to avoid confusion
    addlabel(GetAggregationPeriod() > AggregationPeriod.DAY, "RVol is only valid for daily timeframe or lower");
    
    input _nDayAverage = 5;
    input _rVolHighlightThres = 1.0;
    input _colorBasedOnPrevClose = no;
    
    def days = Max(_nDayAverage, 1);
    def rVolThres = Max(_rVolHighlightThres, 0);
    
    # detect new session of day
    def isNewDay = GetYYYYMMDD() != GetYYYYMMDD()[1];
    
    def cVol;               # cumulative volume
    def beforeNewDayBars;   # save bar number before new day
    def len;                # count number of new days
    if isNewDay {
        cVol = volume;
        beforeNewDayBars = BarNumber() - 1;
        len = len[1] + If(BarNumber() >= 1, 1, 0);
    } else {
        cVol = cVol[1] + volume;
        beforeNewDayBars = beforeNewDayBars[1];
        len = len[1];
    }
    
    # starting from last bar of previous session, go back in time and accumulate volume up to current time relative to trading day
    # stop after N day cumulative volume average collected
    def skip = BarNumber() - beforeNewDayBars;
    def aVol = fold i = skip to Max(skip, BarNumber())
        with v = 0
        while BarNumber() >= days + 1 && len >= days + 1 && len - 1 - GetValue(len, i) < days
        do If(GetTime() - RegularTradingStart(GetYYYYMMDD()) >= GetValue(GetTime(), i) - RegularTradingStart(GetValue(GetYYYYMMDD(), i)), v + GetValue(volume, i) / days, v);
    
    def _rVol = if aVol > 0 then cVol / aVol else Double.NaN;
    
    # visuals
    def upColorCondition = if _colorBasedOnPrevClose then close >= close[1] else close >= open;
    
    Plot RVol = _rVol;
    RVol.DefineColor("Up", Color.GREEN);
    RVol.DefineColor("Down", Color.RED);
    RVol.DefineColor("Up-Dim", Color.DARK_GREEN);
    RVol.DefineColor("Down-Dim", Color.DARK_RED);
    RVol.AssignValueColor(if _rVol >= rVolThres then if upColorCondition then RVol.Color("Up") else RVol.Color("Down") else if upColorCondition then RVol.Color("Up-Dim") else RVol.Color("Down-Dim"));
    RVol.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);
    
    # mark new sessions on intraday charts
    AddVerticalLine(isNewDay && GetAggregationPeriod() < AggregationPeriod.DAY, "", Color.GRAY, curve.SHORT_DASH);
    
    Plot Ref = 1;
    Ref.DefineColor("Reference", Color.GRAY);
    Ref.AssignValueColor(Ref.color("Reference"));
    Ref.HideBubble();
    Ref.HideTitle();
    
    Plot Zero = 0;
    Zero.DefineColor("Zero", Color.GRAY);
    Zero.AssignValueColor(Zero.color("Zero"));
    Zero.HideBubble();
    Zero.HideTitle();
    
    # Warn if not enough days
    addlabel(len < days + 1, "At least " + (days+1) + " days worth of bars needed");

**TV (You may need a NYSE/NASDAQ/Arca subscription for better intraday volume data)**:

    // This source code is subject to the terms of the MIT License at https://opensource.org/licenses/MIT
    // /u/HurlTeaInTheSea v1.1
    
    // v1.1 (2022-12-11)
    // - Fixed edge case where new session begins near midnight of previous day (symbol: DE40, timezone: London/Europe)
    
    // v1.0 (2022-04-28)
    // - Initial release
    
    // Relative Volume (RVol) indicator:
    // https://stockbeep.com/blog/post/how-to-calculate-relative-volume-rvol-for-intraday-trading
    
    //@version=5
    indicator(shorttitle="RVol", title="Relative Volume at Time", precision=2, max_bars_back=5000)
    
    // still works on higher timeframe but it's not a "day" average anymore, so throw error to avoid confusion
    if not (timeframe.isintraday or timeframe.isdaily) or timeframe.isseconds
        runtime.error("RVol is only valid from minute to daily timeframe")
    
    var UP_COLOR = #26a6a4
    var DOWN_COLOR = #ef5350
    
    var UP_DIM_COLOR = #26a6a480
    var DOWN_DIM_COLOR = #ef535080
    
    days = input.int(5, minval=1, title="N Day Average")
    rVolThres = input.float(1.0, minval=0.0, step=0.1, title="RVol Highlight Thres.")
    colorPrevClose = input.bool(false, title="Color based on previous close")
    
    var cVol = 0.0
    var newDayBars = array.new_int()
    
    // detect new session of day
    isNewDay() =>
        t = time('D') // by default, time() follows symbol's session
        na(t[1]) and not na(t) or t[1] < t
    
    if isNewDay()
        // reset cumulative volume
        cVol := 0
        
        // save new bars in circular array of length days + 1
        array.push(newDayBars, bar_index)
        if (array.size(newDayBars) > days + 1)
            array.shift(newDayBars)
        
        if timeframe.isintraday
            // mark new sessions on intraday charts
            line.new(bar_index, 0, bar_index, 0, extend=extend.left, color=color.gray, style=line.style_dotted)
    
    // session start time, which is at regular intervals
    timeSessionStart = time('D')
    
    // cumulative volume
    cVol := cVol + volume
    
    // calculate relative volume
    relativeVolume(cumVol) =>
        aVol = 0.0
        // check enough days saved in history to run (current day also saved)
        len = array.size(newDayBars)
        if len >= days + 1
            // SMA of historical cumulative volume up to but not including current time of day
            for i = 0 to len - 2
                b1 = array.get(newDayBars, i)
                b2 = array.get(newDayBars, i + 1)
                
                // use historical date but carry over current hour, minutes, seconds (this method is exact and avoids DST bugs)
                daysBetweenSessions = math.round((timeSessionStart - timeSessionStart[bar_index - b1]) / (24 * 60 * 60 * 1000))
                tLookup = timestamp(year(time), month(time), dayofmonth(time) - daysBetweenSessions, hour(time), minute(time), second(time))
                
                // get latest bar clamped in range [b1, b2) that is equal to or precedes given time (binary search for speed)
                int lo = math.max(0, b1) - 1
                int hi = math.max(0, b2)
                while 1 + lo < hi
                    int mi = lo + math.floor((hi - lo) / 2)
                    if (tLookup < time[bar_index - mi])
                        hi := mi
                    else
                        lo := mi
                lo := lo < b1 ? hi : lo
                bClosest = b1 < b2 ? lo : -1
                
                // add cumulative volume to SMA calculation
                tClosest = time[bar_index - bClosest]
                aVol := aVol + (tLookup >= tClosest ? cumVol[bar_index - bClosest] / days : 0)
        aVol > 0 ? cumVol / aVol : na
    
    rVol = relativeVolume(cVol)
    
    // visuals
    upColorCondition = colorPrevClose ? close >= close[1] : close >= open
    hline(1.0, title="Reference", color=color.silver, linestyle=hline.style_dotted)
    highlightColor = rVol >= rVolThres ? (upColorCondition ? UP_COLOR : DOWN_COLOR) : (upColorCondition ? UP_DIM_COLOR : DOWN_DIM_COLOR)
    plot(rVol, style=plot.style_columns, color=highlightColor)

**Footnotes**:

* There may be discrepancies in intraday volume data depending on your exchange data provider. Read [this post](https://www.reddit.com/r/RealDayTrading/comments/ubys3i/psa_check_your_exchange_data_source_tradingview) if you're using TV.
* In theory RVol should match exactly for the final bar of the day in all timeframes. But it doesn't because of data provider differences.
* Holidays and shortened days will skew the indicator if it's part of the day moving average. Beware of this limitation.

StockBeep's in-depth post on how RVol is calculated: [https://stockbeep.com/blog/post/how-to-calculate-relative-volume-rvol-for-intraday-trading](https://stockbeep.com/blog/post/how-to-calculate-relative-volume-rvol-for-intraday-trading)