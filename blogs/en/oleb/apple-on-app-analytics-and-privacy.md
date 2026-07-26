---
title: Apple on App Analytics and Privacy
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/apple-app-analytics-privacy/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6c8e2d163eeb0d90'
translated: false
---

> 原文：[Apple on App Analytics and Privacy](https://oleb.net/blog/2014/06/apple-app-analytics-privacy/)　·　Ole Begemann

# Apple on App Analytics and Privacy

One more tidbit from Apple’s updated iOS Developer Program License Agreement. In the [Platforms State of the Union session](https://developer.apple.com/videos/wwdc/2014/) at WWDC yesterday, Apple announced that they are going to offer app analytics in iTunes Connect to developers later in 2014:

[![Slide from the Platforms State of the Union session at WWDC 2014 presenting app analytics in iTunes Connect](https://oleb.net/media/wwdc-2014-slide-app-analytics.png)](https://oleb.net/media/wwdc-2014-slide-app-analytics.png)

> These analytics will tell you how many users visited your store pages; how many users went on and purchased your app; how many remained active over time. And best of all, collecting all this information is built right into iOS and is completely automatic.

It remained unclear whether this enumeration is a complete list of the data Apple will provide, or if they will share other data, such as referrers from other websites or the search terms by which users find your app.

Whatever the case may be, this is a great feature, especially since only Apple can provide data on App Store visits and conversion (unlike app usage data).

# Analytics Data Sharing Restrictions

The [Developer Program License Agreement](https://developer.apple.com/programs/terms/ios/standard/ios_program_standard_agreement_20140602.pdf) explicitly forbids sharing the analytics data with third parties, especially for the purpose of aggregation between apps from multiple developers:

> **6.4 Analytics**
> 
> To the extent that Apple provides an analytics service, You agree to use any data provided through such service solely for purposes of improving Your Applications and related products. Further, You agree not to provide such information to any third parties (except for a third-party service provider who is assisting You in processing and analyzing such data on Your behalf and who is not permitted to use it for any other purpose or disclose it to any other party). For clarity, **You must not aggregate (or permit any third-party to aggregate) analytics information provided to You by Apple for Your Applications as part of this service with other developers’ analytics information, or contribute such information to a repository for cross-developer analytics. You must not use the analytics service or any analytics data to attempt to identify or derive information about any particular end-user or device.**

Emphasis mine. Depending on the type of data that Apple makes available, such data could potentially be used to track individual users across apps, be it for targeted advertising or other purposes.

It’s good to see that Apple [still has user privacy in mind](https://oleb.net/blog/2013/12/app-store-rules-on-data-collection-and-privacy/).
