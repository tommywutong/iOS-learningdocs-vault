---
title: 'Best iOS and Mac Development-Related Links: February 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/03/best-ios-and-mac-development-related-links-february-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2dd69ad7afa5a070'
translated: false
---

> 原文：[Best iOS and Mac Development-Related Links: February 2011](https://oleb.net/blog/2011/03/best-ios-and-mac-development-related-links-february-2011/)　·　Ole Begemann

# Best iOS and Mac Development-Related Links: February 2011

_(My end-of-the-month summary of interesting posts from across the blogosphere has become a regular thing, but I needed a new name for it. Now that I am officially [also a Mac developer](http://blueplanetapp.com/), it’s not just about iOS anymore.)_

A lot has happened in February: The Verizon iPhone came out. Apple announced App Store subscriptions and with them new rules for content publishers regarding In-App purchases. HP announced the TouchPad and Google launched Honeycomb a. k. a. the first Android version for tablets. Nokia adopts Windows Phone 7. And last but not least, we got the first developer seed of Mac OS X 10.7 Lion.

Here is my summary of the past month in links:

# OS X Lion

Apple released the first preview version of [Mac OS X 10.7 Lion](http://www.apple.com/macosx/lion/) to registered Mac developers. Interestingly, they use the Mac App Store to distribute the preview build (and I thought beta software was not allowed on the App Store!).

If you have access to the developer seed, you should really try it out, there is a lot of great new stuff in there. I absolutely love Lion already! Required reading:

- [What’s New in Mac OS X v10.7 Lion](http://developer.apple.com/library/prerelease/mac/#releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_7.html#//apple_ref/doc/uid/TP40010355-SW5)
- [Mac OS X v10.6 to v10.7 API Diffs](http://developer.apple.com/library/prerelease/mac/#releasenotes/General/MacOSXLionAPIDiffs/index.html#//apple_ref/doc/uid/TP40010630)

One especially interesting tidbit from the many thing that have already leaked about Lion is that apparently, Apple is going to ditch the vision of resolution independence and going the “Retina” display route on the desktop, as well: [people found @2x version of images in Lion](http://www.macrumors.com/2011/02/24/mac-os-x-lion-building-in-support-for-super-high-resolution-retina-monitors/).

Before the Lion preview came out, Andy Ihnatko [speculated about a future OS X/iOS mashup OS he calls iX](http://www.macworld.com/article/157824/2011/02/apple_ix.html). Interesting read.

# Programming

- Apple recently published a tech note titled [iOS Debugging Magic](http://developer.apple.com/library/ios/#technotes/tn2010/tn2239.html) that contains a lot of lesser-known tips and tricks. One example that made the rounds on Twitter is the undocumented method `-recursiveDescription` on `UIView` that prints out an entire view hierarchy. Reading this document will make you a better programmer.
- Colin Wheeler explains some [Practical Design Patterns with Blocks and Grand Central Dispatch](https://cocoasamurai.blogspot.com/2011/02/practical-design-patterns-with-blocks.html).
- Matt Gallagher on drawing gradients, glyphs and gloss effects on the Mac: [Advanced drawing using AppKit](http://cocoawithlove.com/2011/01/advanced-drawing-using-appkit.html).
- Mike Ash talks about [Compound Literals in C](http://www.mikeash.com/pyblog/friday-qa-2011-02-18-compound-literals.html). The first comment on the post mentions a neat trick: `someView.frame = (CGRect){ .size = someSize };`Any member you don’t specify is zero-ed out for you.
- The popular game development framework [Cocos2D](http://www.cocos2d-iphone.org/) now has a 3D companion: [Cocos3D](http://brenwill.com/cocos3d/).
- Lisa Bettany explains on the tap tap tap blog [how they develop a photo effect for Camera+](http://taptaptap.com/blog/creating-a-camera-plus-fx/). The best part: code included!
- Evan Coyne Maloney has some good tips on [potential starting points for performance optimization in iOS apps](http://tech.gilt.com/post/3187131303/tips-for-optimizing-iphone-ipad-applications).
- [RestKit](http://mobile.tutsplus.com/tutorials/iphone/restkit_ios-sdk/) looks like a nice library for interfacing with RESTful web services from your iOS app.
- Ray Wenderlich wrote a three-part tutorial series about managing memory in Cocoa and Objective-C: [Memory Management](http://www.raywenderlich.com/2657/memory-management-in-objective-c-tutorial), [How To Debug Memory Leaks with Xcode and Instruments](http://www.raywenderlich.com/2696/how-to-debug-memory-leaks-with-xcode-and-instruments-tutorial), and [Using Properties](http://www.raywenderlich.com/2712/using-properties-in-objective-c-tutorial). Highly recommended for beginners. Related: Keith Harrison’s post about properties, [Understanding your (Objective-C) self](https://useyourloaf.com/blog/2011/2/8/understanding-your-objective-c-self.html)

# UI Design

- [iOS Inspires Me](http://iosinspires.me/), “Showcase of the best looking iPhone & iPad app icons, app interfaces, app websites & resources”.
- [Android Patterns](http://www.androidpatterns.com/wiki) is cool site that lists common UI design patterns on the Android platform. It is sort of like Apple’s Human Interface Guidelines, but extensible. Does anyone know of a similar site for iOS design patterns?
- In this great post from November 2010, George Kokkinidis shows [Remnants of a Disappearing UI](http://news.designlanguage.com/post/1611663345): how fingerprints on the iPad touchscreen can reveal which app was used.
- [Langwich](https://languagesandwich.com/), an interesting new service to help translate your app into other languages.

# The App Store

- [Apple launches subscriptions on the App Store](http://www.apple.com/pr/library/2011/02/15appstore.html).
- So much has been written about Apple’s intent to enforce the rule that app developers who provide access to paid content also have to offer In-App Purchase of the content, at the same or a lower price as outside the app, while still having to pay Apple its customary 30 % commission.

  Some of the many posts on the topic:

    - How it all began: [Apple rejects Sony’s reader app and wants a cut of e-book sales](http://arstechnica.com/apple/news/2011/02/apple-responds-to-app-store-furor-says-it-wants-a-cut-of-e-book-sales.ars)
    - [Readability’s Open Letter to Apple](http://blog.readability.com/2011/02/an-open-letter-to-apple/) after their app got rejected.
    - Marco Arment: [Subscriptions and the new In-App Purchase requirement](http://www.marco.org/3437484678) asks, how does this rule affect services like Evernote and Dropbox or even third-party clients for these services? Probably not at all if [this email from Steve Jobs is legit](http://www.macrumors.com/2011/02/21/steve-jobs-email-suggests-in-app-subscriptions-dont-apply-to-software-as-a-service/), but the wording of the rule is not clear.
    - Matt Drance: [About This Whole Subscription Hubbub](http://www.appleoutsider.com/2011/02/22/omgiapbbq/)Apple has changed the game on people. … Whatever the fine print says, Apple is no longer letting developers do things it had been letting them do — and build businesses on — for almost two years, and many developers are quite understandably upset about that.
    - John Gruber argues [the policy is overall good for the users](http://daringfireball.net/linked/2011/02/23/app-store-subscriptions), which I suppose is true unless it leads to higher prices or an exodus of content apps from the App Store.
    - Kontra defends Apple’s right to discriminate against their competitors like Amazon and Sony and to change the App Store rules on the fly: [Apple’s Ambiguity: There’s an app for that](http://counternotions.com/2011/02/02/ereader/).
    - Manton Reece is troubled about Apple’s tight control over the single distribution platform for a huge number of devices: [30% of the future](http://www.manton.org/2011/02/30_of_the.html).

  At this point, no one can be 100 % sure whom this rule will eventually affect and how, so I guess we’ll just have to wait until the June 30th deadline Apple has given developers to modify their apps.
- Marco Arment, who has occasionally (rightly) criticized Apple’s review process, feels it is time for an [Ode to the App Review team](http://www.marco.org/3100131471) for the great work they do and for the fact that the App Store mostly works to the users’ and developers’ advantage. I agree in principle, although it was a disappointment to have [my Mac app Blue Planet in review for nearly three weeks](https://oleb.net/blog/2011/02/announcing-blue-planet-for-mac/) recently.
- David Frampton shares some [very interesting graphs about the sales performance of his successful iOS apps](http://majicjungle.com/blog/479/), Chopper, Chopper 2, and DuckDuckDuck.
- Similarly, the guys from 2D Boy share their [learnings from the iPad launch of World of Goo](http://2dboy.com/2011/02/08/ipad-launch/).

# The Competition

- Rarely has a big-corporation CEO been so honest in his assessment of his company’s situation as [Nokia CEO Stephen Elop in his memo to Nokia employees](http://www.engadget.com/2011/02/08/nokia-ceo-stephen-elop-rallies-troops-in-brutally-honest-burnin/). A few days later, former Microsoft executive Elop announced that Nokia would adopt Windows Phone 7. Matt Drance in [Microsoft Buys Nokia for $0B](http://www.appleoutsider.com/2011/02/11/nokia/): We like to think of Steve Ballmer throwing chairs when his executives leave. I think this time he told Elop, Fine. Go get me some hardware I can own. Elop did.
- Techcrunch has a [first look at Honeycomb](http://techcrunch.com/2011/02/02/android-honeycomb-ipad/), the first Android version that is focused on tablets.
- Nice [roundup of HP’s webOS and TouchPad introduction event](http://blog.cocoia.com/2011/hp-webos-event-roundup/) by Sebastiaan de With. The TouchPad looks good. Too bad we will have to wait another six months until it will be available.
- The grass isn’t always greener on the other side; developers on other platforms have been complaining:

    - Ian Beck writes a [Love letter to WebOS](http://beckism.com/2011/02/love-letter-webos/) that quickly turns into a rant about the stunning disregard for their app developers that HP exhibited at their latest event.
    - Jamie Murai: [You Win, RIM!](http://blog.jamiemurai.com/2011/02/you-win-rim/) An open lament about the setup, installation and deployment process of RIM’s SDK. [RIM replies](http://devblog.blackberry.com/2011/02/thanks-for-the-open-letter-to-rim-developer-relations/).
- The Android Market grew by an impressive 860 % in 2010, but it is [still behind RIM’s and Nokia’s app stores](http://techcrunch.com/2011/02/21/861-5-percent-growth-android-puny/) in terms of revenue. No wonder most developers are sticking with iOS, despite Android having a similar market share. Monetization matters.
