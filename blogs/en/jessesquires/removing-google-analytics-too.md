---
title: Removing Google Analytics, too
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2018/04/22/removing-google-analytics-too/'
original_language: en
published: 2018-04-22
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b7d03d8f79a5f438'
translated: false
---

> 原文：[Removing Google Analytics, too](https://www.jessesquires.com/blog/2018/04/22/removing-google-analytics-too/)　·　Jesse Squires

I’ve removed Google Analytics from this site. I was in a similar situation as Ash Furrow, who [just wrote about doing this](https://ashfurrow.com/blog/removing-google-analytics/). I’m removing it because it simply causes more harm than good.

Like Ash, I hadn’t looked at this data for awhile. Probably _years_. I added it when I first built the site because adding analytics is _“just what you do”_ when you make a site or an app. Google Analytics was the popular, easy, and “free” choice. In the beginning, I checked the data occasionally. I was only really interested in the number of visits — not all of the creepy, privacy-invasive demographic data that Google harvests. But eventually, I stopped checking. I acknowledged long ago that it wasn’t that valuable to me. But I kept it, thinking _maybe one day_ I’ll need or want this data and I’ll do something with it. It’s clear that isn’t going to happen soon.

#### * * *

And of course, Google Analytics was never “free”. A “free” service isn’t really **free**. It simply means _you are the product_ and the currency with which you are paying is your personal data and right to privacy. In this case, I was volunteering to have my site be commandeered by Google’s JavaScript tracking code.

They’ve convinced anyone from large publishers to indie bloggers to participate in tracking users and collecting users’ data across the entire web. For the benefit of whom? Who owns this data? Why should we allow a private corporation to seize a vast portion of websites that they do not own to execute their arbitrary, proprietary tracking code? What else is this data used for outside of “analytics”?

#### * * *

As a side note, it looks like [Matomo (formerly Piwik)](https://matomo.org) is a great alternative. It’s open source, built with privacy in mind, and you own the data. You can self-host it on your own server for free — as in beer, _and_ [as in speech](https://en.wiktionary.org/wiki/free_as_in_speech). Maybe I’ll try this one day. Maybe not. But if you are interested in replacing Google Analytics, it seems worth checking out.

#### * * *

Ash asked some poignant questions at the end of [his post](https://ashfurrow.com/blog/removing-google-analytics/).

> Who does it help? Who might it hurt?

Rarely, if ever, have I heard these questions asked regarding modern software — especially in Silicon Valley. Ash didn’t elaborate on his answers. But I think the answers are clear.

**Who does this help?** This helps Google. Their analytics product is used on [tens of millions of sites](https://techcrunch.com/2012/04/12/google-analytics-officially-at-10m/), an alarming number when you consider how they might use (misuse?) this data to [monitor an individual’s activity across the web](https://en.wikipedia.org/wiki/Privacy_concerns_regarding_Google#Tracking). When combined with [Google Search](https://www.jessesquires.com/blog/2018/02/25/replacing-google-with-duckduckgo/) and their other “free” services — for developers and users — the potential depth and breadth of this tracking is even more striking. What do I gain by volunteering my website to collect and deliver this data to Google for free?

**Who might this hurt?** Anyone on the web, potentially. Any reader of this blog. We have little reason to [trust](http://www.googletransparencyproject.org) a private corporation like Google, with its targeted advertising revenue model, its [litany of privacy concerns](https://en.wikipedia.org/wiki/Privacy_concerns_regarding_Google), and its [problematic involvement with the US government](https://www.nytimes.com/2018/04/04/technology/google-letter-ceo-pentagon-project.html).

I’m not comfortable with either of those answers. So, [Google Analytics tracking has been completely removed from this site](https://github.com/jessesquires/jessesquires.com/commit/ca9d1d70007be7809f316fb1f2f4b98b0f7d502e).
