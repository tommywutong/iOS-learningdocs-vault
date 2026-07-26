---
title: At What Time Is an App Released on the App Store When Set to a Specific Release Date?
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/at-what-time-is-an-app-released-on-the-app-store-when-set-to-specific-release-date/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1668c0d61b5b7665'
translated: false
---

> 原文：[At What Time Is an App Released on the App Store When Set to a Specific Release Date?](https://oleb.net/blog/2011/05/at-what-time-is-an-app-released-on-the-app-store-when-set-to-specific-release-date/)　·　Ole Begemann

# At What Time Is an App Released on the App Store When Set to a Specific Release Date?

When you submit an app to Apple for review, you have the option to set a specific release date. You can only specify a day, not a time, however. So at what time on the specific date will the app actually be released? At midnight GMT? When the folks in Cupertino come to the office? At a random time during the day? Will the app appear in all App Stores in all time zones at the same time?

It turns out that an app with a specified availability date appears on an international App Store roughly at midnight in the store’s local time zone. So New Zealand will have a 16-hour head start on the United States.

To illustrate this, let me document some tweets from the day the [Tapbots](http://tapbots.com/) released [Tweetbot](http://tapbots.com/software/tweetbot/) recently.

At midnight (local time), Tweetbot appears on the App Store New Zealand. Tweetbot developer Paul Haddad begins to wonder what’s up. Federico Viticci has the explanation:

> F*ckin' Timezones. How do they work?

> [@tapbot_paul](https://twitter.com/tapbot_paul/status/58182894492975105) The App Store's timezone system sucks. App is rolling out at 12AM internationally.

> [@viticci](https://twitter.com/viticci/status/58183093101658114) I figured that might happen but for some reason thought it would start at midnight GMT

> [@tapbot_paul](https://twitter.com/tapbot_paul/status/58183489949929472) Nah. It always begins in Japan and New Zealand, then slowly rolls out basing on timezone.

A few hours later, Tweetbot says Hello to Japan as it is released on the Japanese App Store. Meanwhile, Paul has to answer lots of questions from users for whom Tweetbot is not yet available:

> Konichiwa!

> For folks upset Tweetbot isn't available in your store yet blame Sandford Fleming and the International Date Line. Or Apple, I suppose.

Just after 11 pm GMT (midnight in the UK and 1 am in Western Europe), Tweetbot has appeared on the European App Stores.

> Looks like its midnight in Europe and the UK stores. Only US/Canada/World left.

US users still have to wait:

> [fwdr.org/yu8v](http://fwdr.org/yu8v) Can somebody please tell me why the FUCK Tweetbots isn't showing up for me no matter what I do? Kthx. cc: [@tapbot_paul](https://twitter.com/tapbot_paul)

> [@rockets](https://twitter.com/rockets/status/58323067927150592) not out in the US yet, you have to wait a few more hours.

Finally, 16 hours after New Zealand, Tweetbot goes live on the US App Store:

> Tweetbot is live in the US App Store, our review is up! [mcstr.net/fkW2Vn](http://mcstr.net/fkW2Vn)

**Update #1 May 6, 2011:** Ben Zotto wonders [whether this policy also applies to other App Store dates such as price changes or holiday shutdown deadlines](https://twitter.com/bzotto/status/66284027589566464). I don’t know, though I believe at least the daily sales numbers are also calculated based on each international App Store’s local time. I guess that’s one reason why Apple releases the daily sales numbers only around 1:00–2:00 pm GMT the next day (a few hours after the day ended in the “last” App Store).

**Update #2 May 6, 2011:** Bob Koon notified me on Twitter that he had [already blogged about this in October 2010](http://www.appsizematters.com/2010/10/track-your-appstore-launch-across-the-globe/). In his post, Bob also includes a handy spreadsheet that can tell you for all 90 international App Stores when your app will go live.
