---
title: Apple Changed App Store Prices
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/07/apple-changed-app-store-prices/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d7029a88f7a3063e'
translated: false
---

> 原文：[Apple Changed App Store Prices](https://oleb.net/blog/2011/07/apple-changed-app-store-prices/)　·　Ole Begemann

# Apple Changed App Store Prices

Two months ago I wrote about the fact that [Apple had never adjusted the foreign currency prices in the App Store](https://oleb.net/blog/2011/05/apples-system-of-fixed-exchange-rates-in-app-store/) since its inception in 2008. Over the past three years, fluctuating exchange rates have meant that app prices (and developer revenues) in countries around the world would vary by as much as 75% if measured in US dollars.

Yesterday, Apple finally made some adjustments to its international App Store prices, raising them in some countries and reducing them elsewhere. The overall result is that international prices are much more in line than before.

# Shifting Exchange Rate Risk to Developers

From a developer perspective, Apple changed even more. Before the change, the proceeds developers got from App Store sales in some countries were fixed in a different currency than the local prices.^[1](#fn:1) For instance, a Mexican customer would pay 10 pesos for an app but Apple would pay the developer US$0.70 (rather than 7 pesos). That has changed now: an app sold for 12 pesos (the new price in Mexico) yields the developer 8.40 pesos, which are then converted into the developer’s local currency. Essentially, Apple has shifted the peso-dollar exchange rate risk to the developers. The same happened for New Zealand (from Australian to New Zealand dollars), Switzerland and Norway (from euros to Swiss francs and Norwegian kroner).^[2](#fn:2)

# Don’t Forget Local Taxes (VAT)

When comparing App Store prices around the world, make sure you take taxes into account. Unlike the US, many countries require consumer prices to be quoted inclusive of sales tax or VAT. For example, Graham Spencer of MacStories yesterday [published a chart of international prices](http://www.macstories.net/news/itunes-connect-maintenance-could-mean-apple-is-eventually-recalibrating-international-itunes-prices/) without noting that the EU price of 0.79 € or £0.69 for a $0.99 app includes 15% VAT. As a result, the Euro price of an app before taxes is currently 3% lower than the US dollar price rather than 11% higher (as Graham pointed out). And nobody can seriously blame Apple for different tax systems and rates.

# Before/After Comparison

The following table illustrates the changes Apple made at current (mid-July 2011) exchange rates. To avoid the tax issue, I am comparing the the developer proceeds (after consumer taxes and Apple’s 30% cut) rather than the consumer prices.

| Region | Customer price | Developer proceeds | Converted to US$ | Difference to US | Change for consumers |  |
|---|---|---|---|---|---|---|
| US and Rest of World | $0.99 | $0.70 | $0.70 | – | (none) |  |
| Mexico | Before | MX$10.00 | $0.70^* | $0.70 | ±0% | +20% |
| After | MX$12.00 | MX$8.40^* | $0.72 | +3% |  |  |
| Canada | CA$0.99 | CA$0.70 | $0.73 | +4% | (none) |  |
| Europe | 0.79 € | 0.48 € | $0.68 | −3% | (none) |  |
| Switzerland | Before | 1.10 Fr | 0.48 €^* | $0.68 | −3% | −9% |
| After | 1.00 Fr | 0.65 Fr^* | $0.78 | +11% |  |  |
| Norway | Before | 6.00 Kr | 0.48 €^* | $0.68 | −3% | +17% |
| After | 7.00 Kr | 3.92 Kr^* | $0.70 | ±0% |  |  |
| UK | Before | £0.59 | £0.36 | $0.57 | −19% | +17% |
| After | £0.69 | £0.42 | $0.67 | −4% |  |  |
| Japan | Before | ¥115 | ¥81 | $1.02 | +46% | −26% |
| After | ¥85 | ¥60 | $0.76 | +9% |  |  |
| Australia | Before | AU$1.19 | AU$0.76 | $0.81 | +16% | −17% |
| After | AU$0.99 | AU$0.63 | $0.67 | −4% |  |  |
| New Zealand | Before | NZ$1.29 | AU$0.76^* | $0.81 | +16% | (none) |
| After | NZ$0.90^* | $0.74 | +6% |  |  |  |

Even though the change in prices means that customers in the UK, Mexico and Norway have to pay more now, it is hard to call this an unreasonable price increase by Apple. In fact, it is probably more fair to say that these countries got a discount in the past because prices did not reflect fluctuations in the exchange rates.

From a developer perspective, I don’t expect revenues to change much. Prices in the App Store are so low on average that customers are not likely to buy fewer apps because of a 10p price increase. And unless your app makes most of its sales in a single country like Japan, your biggest markets are probably the US and the Eurozone anyway, where App Store prices remained constant. Assuming constant sales numbers, the biggest influence on your App Store revenue is the exchange rate between the US dollar and the euro.

# Apple Makes It Easy for Consumers, Google for Developers

Although I think it was a good idea to eventually adjust the prices to changing exchange rates, the fact that Apple waited three years to do so says a lot about their focus on the end user: don’t confuse the consumer with ever-changing prices, especially given the overall low price level in the App Store. Contrast this to the Android Market where the price of an app ~~is~~ was fixed only in the developer’s local currency and the price in other currencies fluctuates daily with the exchange rate until Google changed this recently.^[3](#fn:3) Simpler for the developer, confusing for the consumer.

1. If you are an Apple developer, look up the Pricing Tier tables in Schedule 2 to the Paid Apps Agreement to see this. [↩︎](#fnref:1)
2. Curiously, Denmark and Sweden continue on the [sonderweg](https://en.wikipedia.org/wiki/Sonderweg): App Store prices are quoted in the local currency but proceeds are paid out to developers in euros. While the exchange rate risk is minimal, I wonder why Apple changed the rules for Norway but not for these two countries.

  **Update:** [Erik Lindberg suggested on Twitter](https://twitter.com/shadester/status/91493646750322688) that the reason could be that Denmark and Sweden are members of the EU while Norway and Switzerland are not, and I think that is a very good guess.

  [↩︎](#fnref:2)
3. Google [modified this rule in early 2011](http://www.androidpolice.com/2011/02/10/android-market-introducing-buyers-currency/) and offers Android developers in select countries (I don’t know which) the choice to [offer apps for sale in multiple currencies](https://www.google.com/support/androidmarket/developer/bin/answer.py?hl=en&answer=1169947). The prices you set in one currency are completely independent of prices in other currencies, again making this less clear for consumers in my opinion. [↩︎](#fnref:3)
