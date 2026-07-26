---
title: Status bars matter
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2014/08/03/status-bars-matter/'
original_language: en
published: 2014-08-03
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:21627c675d2de100'
translated: false
---

> 原文：[Status bars matter](https://www.jessesquires.com/blog/2014/08/03/status-bars-matter/)　·　Jesse Squires

You have spent countless hours, days, months, or maybe even [years](http://www.polygon.com/2014/2/6/5386200/why-it-took-a-year-to-make-and-then-break-down-an-amazing-puzzle-game) perfecting your app. There has been plenty of blood, sweat, and tears. Your relationships and your health have [suffered through](http://blog.jaredsinclair.com/post/93118460565/a-candid-look-at-unreads-first-year) the development process. You are ready for 1.0 and the time has arrived to prepare all of your content for the App Store — app icon, keywords, description, localizations, and screenshots (and soon [app previews](https://developer.apple.com/support/appstore/app-previews/)).

##### [Update](#updated-13-october-2014)  _13 October 2014_

[Shiny Development](http://shinydevelopment.com) has removed Status Magic from the App Store. Find out why on [their blog](http://shinydevelopment.com/blog/status-magic-and-iphone6-screen-sizes/) and how you can still get perfect status bars with OS X Yosemite and iOS 8.

But even with all of Dan Counsell’s [excellent advice](http://dancounsell.com/articles) on how to promote your app and refine your App Store presence, I continue to see iOS developers make one glaring mistake in their screenshots. This common flaw is even overlooked in Dan’s article on [_Designing Great App Store Screenshots_](http://dancounsell.com/articles/designing-great-app-store-screenshots), which should be required reading for all iOS developers. But what does it fail to mention? **The status bar.**

![iOS status bar](https://www.jessesquires.com/img/blog/statusbar.jpg)

<sub>iOS status bar</sub>

#### Sore thumbs

Status bars matter. If configured well, they go unnoticed. But if they are sloppily ignored, they stick out like a sore thumb. And sadly, there are a lot of sore thumbs in the App Store. Below are actual status bars taken from the screenshots of three different apps curently in the App Store. All apps were on one of the top charts within the top 50.

![Status bar example 1](https://www.jessesquires.com/img/blog/statusbar-bad1.jpg)

<sub>Sample 1: status bars seen in the App Store</sub>

![Status bar example 2](https://www.jessesquires.com/img/blog/statusbar-bad2.jpg)

<sub>Sample 2: status bars seen in the App Store</sub>

![Status bar example 3](https://www.jessesquires.com/img/blog/statusbar-bad3.jpg)

<sub>Sample 3: status bars seen in the App Store</sub>

There’s a lot of information in an untamed status bar. In _Sample 1_ it looks like someone is from Canada, and working late through the evening. At least she had good reception and an adequate power supply. In _Sample 2_ the developer lives in the UK, and has extremly poor reception. She needs to charge her iPhone soon, but at least she knows her current location. _Sample 3_ is by far the most interesting. We can see AT&T’s typically poor reception, thus the developer is in the US. This guy was up late, but at least he remembered to set his alarm so that he could wake up in the morning to take more screenshots and charge his device.

Status bars seem negligible until you notice how unsightly and distracting they can be. Luckily, the mistakes above can be easily avoided.

#### Preparing your screenshots

We know that screenshots are one of the most important parts of the App Store content for which you are responsible. Users _rarely_ read app descriptions in their entirety, but they _always_ look at screenshots. If the status bar is visible in the screenshots that you provide, then it better be clean and uniform across every single one. It should have full cell reception bars, no carrier text, full Wi-Fi bars, and a fully charged battery. Each screenshot should also display **the exact same time**. _No exceptions_. Finally, depending on your app’s functionality, it might make sense to show the GPS location or Bluetooth indicators, but use sparingly. Also remember that you can remove the status bar altogether.

#### Raising the (status) bar

You can automate all of this with an awesome utility app called [Status Magic](http://shinydevelopment.com/status-magic/), which adds perfect status bars to your screenshots or removes them completely. It is worth every penny, and it will get your screenshots looking clean and consistent in no time.

The only aspect of the status bar that you should customize, aside from the colors, is the time. Apple uses `9:41 AM`. Choose something reasonable — for example, [Clear](https://itunes.apple.com/us/app/clear-tasks-to-do-list/id493136154) uses `10:00`. I like to use `7:06 AM`. If you cannot decide on a time that is meaningful to you, then Apple’s `9:41 AM` will work beautifully and you will fit right in.

Don’t let your app be a victim of status bar neglect. This is about polishing your app and its presentation in the App Store to the highest degree. **Status bars matter**, and every detail counts.
