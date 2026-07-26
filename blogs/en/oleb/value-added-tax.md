---
title: Value-Added Tax
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/07/eu-vat-changes-2015/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:75bfc5022ed90920'
translated: false
---

> 原文：[Value-Added Tax](https://oleb.net/blog/2014/07/eu-vat-changes-2015/)　·　Ole Begemann

# Value-Added Tax

**Update December 18, 2014:** Apple yesterday [informed developers about the upcoming change](https://itunesconnect.apple.com/WebObjects/iTunesConnect.woa/wa/jumpTo?page=faqIndex&group=bankingandtax#eu_vat_apps). Apple chose option 2 below: consumer prices in the EU (incl. VAT) remain unchanged and developer proceeds (excl. VAT) will go down starting on January 1, 2015. How much your revenue will decline precisely depends on your apps’ sales distribution across the EU. A drop of 5% of your overall revenue from EU app sales is a reasonable estimate.

My accountant pointed me to an [upcoming change](http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2008:044:0011:0022:EN:PDF) in [EU value-added tax](https://en.wikipedia.org/wiki/European_Union_value_added_tax) (VAT) law that is relevant to app developers. Starting 2015, VAT on app sales in the European Union will effectively increase from 15% to 18–27%, depending on the country where an app is sold. It is not yet clear whether this will lead to higher consumer prices or lower per-app revenue for developers.

# The Current Situation

All App Store sales to consumers in the EU (and many other countries) are handled by iTunes [S.à r.l.](https://en.wikipedia.org/wiki/Soci%C3%A9t%C3%A9_%C3%A0_responsabilit%C3%A9_limit%C3%A9e), an Apple subsidiary based in Luxembourg. When a EU resident buys an app, iTunes S.à r.l. as the contracting partner[1](#fn:1) must charge VAT on the sale price. If the customer is also based in Luxembourg[2](#fn:2), Luxembourg’s VAT rate applies. If seller and buyer are in different countries, the EU has established rules that govern where VAT is collected. Simplified, they are as follows:

- Physical goods are taxed in the buyer’s country of residence.
- Most services (incl. software) are taxed in the country of the seller.

There are multiple exceptions to this that switch this arrangement around, and exceptions to the exceptions. But the gist of it is that, currently, apps sold to EU residents are always taxed in Luxembourg, regardless of the customer’s country of residence.

Since [VAT rates differ among EU countries](https://en.wikipedia.org/wiki/European_Union_value_added_tax#VAT_rates) and Luxembourg conveniently has the lowest rate of all (15%; Hungary has the highest with 27%), this effectively makes apps cheaper than they would be otherwise.

# The New Rules

As of January 1, 2015, this will change. Electronically supplied services (such as apps) sold to private customers will then be taxed in the buyer’s country of residence. This means an added administrative burden for Apple because iTunes S.à r.l. now has to declare the VAT it collects from consumers for each of the 28 EU member states separately.[3](#fn:3)

More importantly, the new legislation will have an effect on either consumer app prices in the EU or the proceeds Apple pays out to developers for sales of their apps in the EU.

# Possible Changes

## 1. Higher App Prices for Consumers

As an example, take an app that is priced at €0.89 (the equivalent of the $0.99 price tier) in the EU. It has a net price of `€0.89 / 1.15 = €0.77` (or $1.03 at [current exchange rates](https://www.google.com/search?q=0.77+EUR+to+USD)) after deducting the Luxembourg VAT rate (consumer prices in the EU are always quoted tax-inclusive).

If the net price remains unchanged, the same app in 2015 will cost €0.92 in Germany (where the VAT rate is 19%), €0.94 in Italy (22%), and €0.98 in Hungary (27%). In all cases, the amount paid out to the app developer will be `€0.77 × 70% = €0.54`, regardless of the country where the sale took place.

Note that I only look at the euro here. Apple charges for apps in euro even in most EU countries that are not part of the eurozone; only the App Stores in the UK, Sweden, and Denmark use the respective local currency. For these countries, the considerations are the same but app prices are harder to compare to other countries due to exchange rate fluctuations (although the variation in the exchange rate of the Danish krone and Swedish krona to the euro is extremely small).

## 2. Lower Proceeds for Developers

If Apple decides to keep the consumer price of €0.89 constant across the EU, the net price of the app will vary depending on the country where it was sold, resulting in a lower payout to the developer. Instead of €0.54, a developer might only receive €0.52 for an app sold in Germany, €0.51 in Italy, or €0.49 in Hungary.

# Conclusion

We don’t know yet which method Apple will choose. Keeping consumer prices constant across the EU would certainly be the least confusing option to App Store customers. For hardware sales in their own online store, Apple’s practice has generally been to reflect different VAT rates in consumer prices, however, albeit not exactly.[4](#fn:4)

If Apple chooses to keep consumer prices constant, developers may see their revenues from EU app sales decline by about 5% compared to current levels. If the tax increase leads to higher app prices for consumers, payouts to developers will remain constant on a per-app basis, but total revenue might drop due to a possible decrease in demand (which is hard to quantify).

1. iTunes S.à r.l. acts as [commissionaire](http://www.hmrc.gov.uk/manuals/intmanual/intm441040.htm) on behalf app developers. [↩︎](#fnref:1)
2. This is not very likely, given Luxembourg’s tiny population of 550,000. [↩︎](#fnref:2)
3. This will not be as hard as it sounds, however, since the tax office in the seller’s country will accept VAT payments on behalf of other member countries and remit the appropriate amounts to them. [↩︎](#fnref:3)
4. For example, the base MacBook Air model currently costs €883 in Luxembourg (15%), €899 in Germany (19%) and France (20%), €929 in the Netherlands (21%), Portugal (23%) and Finland (24%), and even €933 in Italy (22%). [↩︎](#fnref:4)
