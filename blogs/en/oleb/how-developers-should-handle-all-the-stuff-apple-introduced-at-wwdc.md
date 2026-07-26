---
title: How Developers Should Handle All the Stuff Apple Introduced at WWDC
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/how-developers-should-handle-stuff-apple-introduced-at-wwdc/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9c47d82b467ac086'
translated: false
---

> 原文：[How Developers Should Handle All the Stuff Apple Introduced at WWDC](https://oleb.net/blog/2011/06/how-developers-should-handle-stuff-apple-introduced-at-wwdc/)　·　Ole Begemann

# How Developers Should Handle All the Stuff Apple Introduced at WWDC

Yesterday was a big news day for Apple developers. In the [WWDC keynote](http://www.apple.com/apple-events/wwdc-2011/), Apple showed off [Mac OS X Lion](http://developer.apple.com/technologies/mac/whats-new.html) (again), introduced [iOS 5](http://developer.apple.com/technologies/ios5/) and their new [iCloud service](http://developer.apple.com/icloud/). Right after the keynote, they released a new developer preview of Lion and the first beta of iOS 5 and the iOS 5 SDK.

That’s a a lot of stuff. If you’re like me, you feel more than a little overwhelmed, looking at a good 15-20 gigabytes of new downloads. How to digest all this? How should you deal with it most effectively? Here is my suggestion.

# Three all-important keynote slides

Although WWDC is a developer event, the keynote focused mainly on the new consumer features in Lion and iOS. The most important information for developers is contained in these three all-important slides:

![Steve Jobs introducing iCloud Storage APIs at WWDC 2011](https://oleb.net/media/wwdc-2011-keynote-icloud-storage-apis.png)

<sub>(1) iCloud will have storage APIs so we can use it in our apps. This is HUGE.</sub>

![Scott Forstall introducing new developer features in iOS 5 at WWDC 2011](https://oleb.net/media/wwdc-2011-keynote-ios5-developer-features.png)

<sub>(2) New developer features in the iOS 5 SDK.</sub>

![Phil Schiller introducing new developer features in Mac OS X Lion at WWDC 2011](https://oleb.net/media/wwdc-2011-keynote-lion-developer-features.png)

<sub>(3) New developer features in Lion.</sub>

# Study the release notes and API diffs

To learn more about the new APIs, you should dive into the developer documentation. With each SDK release, Apple publishes two documents that you absolutely have to read (only for registered iOS developers):

1. [What’s New in iOS 5](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS5.html). This document gives you an easy-to-read overview of the most important changes in the new release, together with links to more detailed guides and the reference documentation.
2. [iOS 5 API Diffs](https://developer.apple.com/library/prerelease/ios/releasenotes/General/iOS50APIDiff/index.html). This is a loooong list that mentions every new framework and, for existing frameworks, every single API that has been added, changed or removed. I know it’s boring to go through this document but if you don’t, you will miss a lot of new stuff that Apple didn’t mention in the keynote or anywhere else. Who knows, one of these new APIs may offer exactly what you want for your app. Feel free to skip sections that aren’t relevant to you, though. For any API that catches your interest, follow the link to the reference docs and/or inspect the header file where it is defined. Even if documentation for a new API is not yet available, there are often nice explanatory comments in the headers.

If you are a Mac developer, here are the corresponding documents for Lion. Besides minor modifications, they have been available since we got the first developer release of Lion so you hopefully already know them inside and out.

1. What’s New in Mac OS X Lion
2. Mac OS X Lion API Diffs

Now that you have an overview of the new capabilities (both those that are publicly known and the ones only developers see in the beta SDK), you should plan which ones you want to use and how.

# Plan your next app

If you currently have time to start a new project and are looking for an idea (or a way to make your current idea even more awesome), I suggest you pick one of the new iOS features and build a great app around it. Or, if you already have a great app idea, look for ways to make it awesome by supporting one or more of the new APIs. Now you’ve got a few months to develop your app. Release your app on the day when iOS 5 comes out (Apple said iOS 5 will be released this fall, so plan to finish by mid-September if possible). You now have:

1. A newsworthy app release because you are among the first apps to support a new feature.
2. An app that does something that people have requested (because Apple says the implement new features based on user or developer demand; so it is likely that multiple people have asked Apple to include this new feature).
3. A competitive advantage over late-comers.

Don’t worry about not supporting older OS versions. Every device Apple has sold in the last 2 years can run iOS 5. Don’t worry about other developers doing the same thing, either. With 500,000 apps in the App Store, competition is a fact of life. And the vast majority of developers is either incompetent or too lazy to check out what’s new or so deeply entrenched in work that they haven’t got the capacity to start a new app right now. By following this strategy, your chances to get noticed are a lot better in my opinion.

Of course, your app still has to be awesome. Don’t think my focusing on features means that this is about supporting as many of the new features as possible. It isn’t. It’s important to support _one_ new thing that hasn’t been possible before (to get the newness benefit) but as soon as you’ve got that covered, focuse on _awesome_, not on features.

# Or bring your existing one to the next level: iCloud everywhere

If you don’t have time for a new project right now and you have to support an existing app, consider which of the new features are a fit for your app. Use the time until iOS 5 is released to integrate those new things into your app and try to have it ready on day one. That way, you also have the chance to get a lot of press and new users. You will probably have to support iOS 4 for a while but if your app still runs on iOS 3, now is the time to cut off support for it.

Especially, take a thorough look at the iCloud storage APIs. Nearly every app can benefit from supporting iCloud, if “only” to sync its preferences between devices. It won’t be long until users expect iCloud support in every single app. Don’t make yours the one that users ditch because it does not integrate iCloud.
