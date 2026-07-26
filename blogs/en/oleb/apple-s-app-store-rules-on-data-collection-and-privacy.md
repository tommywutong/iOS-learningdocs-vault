---
title: 'Apple''s App Store Rules on Data Collection and Privacy'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/12/app-store-rules-on-data-collection-and-privacy/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f258d2245b3c7e63'
translated: false
---

> 原文：[Apple's App Store Rules on Data Collection and Privacy](https://oleb.net/blog/2013/12/app-store-rules-on-data-collection-and-privacy/)　·　Ole Begemann

# Apple's App Store Rules on Data Collection and Privacy

It is worth re-reading Apple’s rules that all iOS apps in the App Store must comply with from time to time. I did so the other day as part of my research for [my previous article](https://oleb.net/blog/2013/12/apples-inter-app-sharing-dilemma/). In this post, I would like to revisit Apple’s guidelines on data collection and privacy because I think they warrant a broader discussion.

# App Store Review Guidelines

There are two documents in which Apple lays down the rules of the App Store. The [App Store Review Guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html) (you need to be a registered iOS developer to access this link) [came quite late](http://appleinsider.com/articles/10/09/09/apples_app_store_review_guidelines_we_dont_need_anymore_fart_apps) to the scene in September 2010, more than two years after the opening of the App Store. The Review Guidelines are written in a very clear, non-legalese language and include both broader themes that guide the app review process and very specific rules. Section 17 is concerned with privacy. This is the most relevant part:

> **17.1** Apps cannot transmit data about a user without obtaining the user’s prior permission and providing the user with access to information about how and where the data will be used[.]

# iOS Developer Program License Agreement

The very first rule in the Review Guidelines makes clear that they do not replace the other document every iOS developer must agree to, and that is the iOS Developer Program License Agreement. As a registered and paying iOS developer, you can find the Program License Agreement in [Apple’s Developer Member Center under Legal Agreements](https://developer.apple.com/membercenter/index.action#agreements). The License Agreement is a long contract that is much harder to read. Section 3.3 lists the rules apps must comply with. It includes more rules about privacy and data collection:

> **3.3.8** Any form of user or device data collection, or image, picture or voice capture or recording (collectively “Recordings”), and any form of data, content or information collection, processing, maintenance, uploading, syncing, storage, transmission, sharing, disclosure or use performed by, through or in connection with Your Application must comply with all applicable privacy laws and regulations as well as any related Program Requirements, including but not limited to any notice or consent requirements. …
> 
> **3.3.9** You and Your Applications (and any third party with whom you have contracted to serve advertising) may not collect user or device data without prior user consent, and then only to provide a service or function that is directly relevant to the use of the Application, or to serve advertising in accordance with Sections 3.3.12 and 3.3.13. You may not use analytics software in Your Application to collect and send device data to a third party. Further, neither You nor Your Application will use any permanent, device-based identifier, or any data derived therefrom, for purposes of uniquely identifying a device.
> 
> **3.3.10** You must provide clear and complete information to users regarding Your collection, use and disclosure of user or device data, e.g., a link to Your privacy policy on the App Store. … If a user ceases to consent or affirmatively revokes consent for Your collection, use or disclosure of his or her user or device data, You (and any third party with whom you have contracted to serve advertising) must promptly cease all such use.

It goes on with specific rules for advertising, specifically restrictions for the use of the [`advertisingIdentifier`](https://developer.apple.com/library/ios/documentation/AdSupport/Reference/ASIdentifierManager_Ref/ASIdentifierManager.html#//apple_ref/doc/uid/TP40012654-CH1-SW4) API (Apple’s replacement for the removed unique device identifier) for identification or tracking purposes.

# What Does It Mean?

We can obviously argue endlessly about the meaning of specific terms. What is meant by “user data” or “device data”? Does user data include anonymized usage stats? Are the OS version or the device model identifier examples of device data in the context of these rules? My answer would be yes on both counts but Apple does not define those terms.

Regardless, I think the intention of the rules is quite clear: Apple cares about the privacy of their users[1](#fn:1) and app developers are supposed to respect it, too. Read that quote again:

> You … may not collect user or device data without prior user consent, and then only to provide a service or function that is directly relevant to the use of the Application, or to serve advertising …. You may not use analytics software in Your Application to collect and send device data to a third party.

Now check out [the kinds of data an analytics service like Flurry collects](http://support.flurry.com/index.php?title=Analytics/Overview/Lexicon) from the hundreds of thousands of apps[2](#fn:2) that use it:

- Device (model, OS version) and carrier information
- User demographics: age, gender, personas and interests (estimated from Flurry’s wealth of data)
- Language settings of your users
- Geographic distribution of your users
- Number of active users
- Frequency of use
- Session length
- Visited screens and other custom-defined events

(I am not certain [if and how Flurry and similar services still manage to track users across multiple apps in iOS 7](https://oleb.net/blog/2013/12/apples-inter-app-sharing-dilemma/). Unless they abuse the advertising identifier or employ some kind of [fingerprinting](https://en.wikipedia.org/wiki/Device_fingerprint), they may not be able to now that Apple has removed the ability to share named pasteboards.)

![Flurry Analytics Feature Set](https://oleb.net/media/flurry-analytics-feature-set.png)

<sub>The feature set of Flurry Analytics. Source: [Flurry](http://support.flurry.com/index.php?title=Analytics/Overview/RestrictedFeatureSet).</sub>

Although the data is anonymous – at least in the sense that the user’s name is unknown, and only unless you send the user’s id (if your app requires login) along with the usage data, an option that [Flurry supports](http://support.flurry.com/sdkdocs/v3/iOS/interface_flurry.html#a7f1e93aa12021d864af31e327ea368e0) – I find it hard to argue that this dataset does not include both “user” and “device” data.

# Do the Right Thing

What does this mean in practice? Unfortunately (from the perspective of a user who is concerned about privacy), the answer is, next to nothing, because Apple doesn’t seem to enforce these rules very actively, if at all.

While I currently do not use any analytics in my apps[3](#fn:3), I have worked for clients that do and I am not against the data collection per se. I do realize that things like usage stats, OS versions and language preferences of your user base can be extremely useful to steer the development of an app into the right direction. And let’s face it, the monitoring of users’ every move won’t go away anyway, and neither is the collection of such data by aggregators; building and running your own analytics service is not trivial.

Nevertheless, I would love if this post causes some developers to think harder about the integration of analytics in their apps. If you just sign up for a third-party service like Flurry or Google Analytics, download their SDK and embed it in your app with one line of code, that’s not good enough. If your next client asks you to do just that, please argue with them for more transparency.

Let us all make an effort to do the right thing:

**Tell your users what kinds of data you collect and whom you share it with.** The [standard EULA](http://www.apple.com/legal/internet-services/itunes/appstore/dev/stdeula/) or a link to your privacy policy may legally be all you need and sadly, even Apple says it’s good enough (see 3.3.10 above). But let’s be honest: we all know [nobody reads the fine print](http://tosdr.org). Add a section to the settings screen in your app where you tell users in clear and candid language what stats you collect. Make clear where and by whom the data is stored if you use a third-party analytics service.

**Give users the option to opt out.** This should be simple switch in your app’s settings screen. Assuming most users don’t change the default settings and you count the percentage of users that have opted out, I believe the predictability of your dataset won’t even degrade significantly. Stop calling your analytics package’s init method in `applicationDidFinishLaunching:` for users that have opted out.

Your users will appreciate it.

1. And yes, perhaps they care even more about the privacy of the model identifiers of next year’s iPhone and that is why they explicitly forbid the transmission of “device data” to third parties whereas “user data” is not mentioned. [↩︎](#fnref:1)
2. Flurry itself claims that it is being [used by 400,000 apps](http://www.flurry.com/big-data.html). Assuming that half of them are iOS apps, Flurry Analytics is integrated in approximately 20% of all apps in the App Store. [↩︎](#fnref:2)
3. Disclaimer: this website is currently tracking you through Google Analytics, though I plan to remove it. [↩︎](#fnref:3)
