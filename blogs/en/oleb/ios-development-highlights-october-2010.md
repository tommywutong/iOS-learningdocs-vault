---
title: 'iOS Development Highlights: October 2010'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/10/ios-development-highlights-october-2010/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8cb6b1b20b25a6d5'
translated: false
---

> 原文：[iOS Development Highlights: October 2010](https://oleb.net/blog/2010/10/ios-development-highlights-october-2010/)　·　Ole Begemann

# iOS Development Highlights: October 2010

Here are some of the things from across the iOS blogosphere I found interesting this past month.

- The hottest topic, of course, was Apple’s _Back to the Mac_ event, which gave us the first glimpse of OS X Lion (including some iOS design patterns) and the Mac App Store. Some opinions from the community:

    - Anil Dash [encourages the Mac community to build an open app store on the Mac](http://dashes.com/anil/2010/10/how-to-make-an-open-app-store-on-the-mac.html) as a counterweight to Apple’s.
    - Wolf Rentzsch [applauds the Mac App Store but is concerned about Apple’s guidelines for acceptable App Store apps](https://rentzsch.tumblr.com/post/1369652253/mac-app-store) (no trials, no refunds).
    - Jim Dovey [asks Apple to review apps based on their benefit to the users](https://quatermain.tumblr.com/post/1370053291/rentzsch-tumblr-com-mac-app-store) and not on bureaucratic rules like no use of private APIs and no need for root privileges.
    - Marco Arment: [The Mac App Store isn’t for today’s Mac developers](http://www.marco.org/1432156914), but rather for the (probably much larger) group of future OS X developers who are drawn to Mac development by the App Store’s appeal. Most apps will probably be inexpensive and “low-risk”, much like today’s iOS apps.
    - Martin Pilkington [disagrees with Marco](http://pilky.me/view/10) because in his opinion, users expect more (features, functionality) from desktop apps. Such apps would have to be more expensive and the current app store model (no trials, no upgrade pricing) does not cater for pricier software.
    - Lukas Mathis [hopes that Apple uses the App Store to highlight high-quality software](http://ignorethecode.net/blog/2010/10/24/lion/) instead of going for sheer volume.
- Jeff LaMarche has been working on a book on OpenGL ES 2.0 development for iOS. [The book has been put on hold](https://iphonedevelopment.blogspot.com/2010/10/opengl-es-20-book.html) for the time being, but thankfully, his publisher has allowed him to publish the finished chapters on his blog. So far, [chapter 1](https://iphonedevelopment.blogspot.com/2010/10/opengl-es-20-for-ios-chapter-1.html), [chapter 2](https://iphonedevelopment.blogspot.com/2010/10/opengl-es-20-for-ios-chapter-2-meet.html), and [chapter 3](https://iphonedevelopment.blogspot.com/2010/10/opengl-es-20-for-ios-chapter-3.html) have been posted.
- Wil Shipley writes about a security flaw of the App Store: [“Curated” doesn’t necessarily mean “secure”](http://blog.wilshipley.com/2010/09/curated-doesnt-necessarily-mean-secure.html).
- Matt Rix, developer of the hugely successful iOS game [Trainyard](http://www.trainyard.ca/), writes about [the story behind the game](http://struct.ca/2010/the-story-so-far/) and how it gained traction on the App Store. The interesting part: sales were quite low during the first three months of Trainyard’s life and exploded when he released a free Lite version of the game and not only bloggers around the world picked it up, but Apple also featured the paid version on the App Store.
- Oliver Reichenstein from Information Architects on the pros and cons of two common design patterns on the iPad: [Scroll or Card?](http://www.informationarchitects.jp/en/ipad-scroll-or-card/)
- Joshua Johnson on AppStorm: [30 examples of stunning iPad app interface design](http://iphone.appstorm.net/roundups/design/30-examples-of-stunning-ipad-app-interface-design/). Good inspiration.

These articles are older, but I only discovered them recently:

- Mark Dalrymple on [block retain cycles](http://borkwarellc.wordpress.com/2010/09/06/block-retain-cycles/). These have been mentioned on various blogs already, but Mark created a very nice and simple example to demonstrate the problem. Something to look out for in your own code.
- Stephen Lombardo demonstrates [how to encode your app’s data in a custom URL](http://mobileorchard.com/lite-to-paid-iphone-application-data-migrations-with-custom-url-handlers/) to help users migrate from a free to a paid version of the same app. Reportedly, this works even when the amount of data you need to transfer is pretty substantial.
- W. Dana Nuon wrote [a conical deformation algorithm in OpenGL to mimic Apple’s page curl transition](https://wdnuon.blogspot.com/2010/05/implementing-ibooks-page-curling-using.html). Looks beautiful.
