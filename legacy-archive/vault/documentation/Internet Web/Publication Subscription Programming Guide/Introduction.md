---
title: Publication Subscription Programming Guide
apple_id: TP40004945
resource_type: Guide
platform: macOS
topic: null
technology: PublicationSubscription
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/PubSub/Introduction/Introduction.html
archived_at: '2026-07-15T07:43:34.145475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Understanding%20Feeds.md)

# Introduction

Introduced in OS X v10.5, Publication Subscription is a technology that offers developers a way to subscribe to web feeds from their applications. Web feeds are documents that contains frequently updated information. You can use Publication Subscription to allow your applications to subscribe to podcasts, photocasts, and any other feed-based document. Plus, Publication Subscription handles all the feed downloads and updates automatically. This document explains how feeds work and how to use them in your application.

Before reading this document, you should have some experience with Objective-C and be familiar with XML.

This book contains the following chapters:

- [Understanding Feeds](Understanding%20Feeds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqmznknltk) describes what feeds are and how they work.
- [Publication Subscription Overview](Publication%20Subscription%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqnjnknltk) explains the architecture of Publication Subscription.
- [Subscribing to a Feed](Subscribing%20to%20a%20Feed.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqnbnknltg) explains how to use Publication Subscription to subscribe to a feed.
- [Viewing and Retrieving Content](Viewing%20and%20Retrieving%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqnrnknltg) describes how to read the data in a feed.

For an in-depth description of the Publication Subscription framework, read:

- _Publication Subscription Framework Reference_

For more information about some of the technology areas used by Publication Subscription, refer to:

- _[Core Foundation Design Concepts](../../Core%20Foundation/Core%20Foundation%20Design%20Concepts/Introduction%20to%20Core%20Foundation%20Design%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezde2i)_ to learn more about the Cocoa design patterns
- _[Tree-Based XML Programming Guide](../../Cocoa/Tree-Based%20XML%20Programming%20Guide/Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrz)_ to learn more about XML and how to use it in Cocoa

There are also a number of good websites about the different feed standards supported by Publication Subscription:

- For more information about the RSS 0.9, RSS 1.0 and RSS 2.0 formats, read [http://en.wikipedia.org/wiki/Really_Simple_Syndication](http://en.wikipedia.org/wiki/Really_Simple_Syndication).
- For more information about the Atom Syndication Format, read [http://en.wikipedia.org/wiki/Atom_%28standard%29](http://en.wikipedia.org/wiki/Atom_%28standard%29).
[Next](Understanding%20Feeds.md)

