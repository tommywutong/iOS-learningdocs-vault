---
title: 'Best iOS and Mac Development-Related Links: April 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/best-ios-and-mac-development-related-links-april-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:11679500ae391793'
translated: false
---

> 原文：[Best iOS and Mac Development-Related Links: April 2011](https://oleb.net/blog/2011/05/best-ios-and-mac-development-related-links-april-2011/)　·　Ole Begemann

# Best iOS and Mac Development-Related Links: April 2011

Here is my summary of the past month in links. I decided not to include any stories about Android and the other mobile platforms this time. I also don’t cover the iPhone’s hidden location database as I think it’s not really relevant for us developers.

# Programming

## Components

- ~~[`JTextView`](http://codaset.com/jer/jtextview) by Jeremy Tregunna is a rich-text editor component for iOS, using Core Text for rendering.~~ Update: This one doesn’t seem to be as good as it looked to me initially. There is still room for an awesome rich text editor component for iOS.
- [WEPopover](https://github.com/PaulSolt/WEPopover), an implementation of popover views for the iPhone with the same API as `UIPopoverController` on the iPad. Originally written by [Werner Altewischer](http://www.werner-it.com/index.php?lang=english) and improved by [Paul Solt](http://paulsolt.com/).
- David Linsin wrote [`DLWebView`](https://dlinsin.github.com/2011/04/24/DLWebView.html), a drop-in web browser component that adds a title bar, back and forward buttons, and an address bar to `UIWebView`. Should be useful for apps that need a built-in browser but where the browser is not an essential component.

  **Update May 5, 2011:** Guillaume Campagna suggests Samuel Vermette’s [`SVWebViewController`](https://github.com/samvermette/SVWebViewController) as a good alternative to `DLWebView`. Looks good, you should check both out.
- Michael Tyson has written drop-in replacements for `UITableView` and `UIScrollView` that solve a problem that nearly every iOS developer must deal with: [moving text fields out of the way of the keyboard](http://atastypixel.com/blog/a-drop-in-universal-solution-for-moving-text-fields-out-of-the-way-of-the-keyboard/) so that the user can actually see what she types.
- [QuincyKit](http://quincykit.net/) is a client and server component written by Andreas Linde that collects crash reports from your iOS and OS X apps. Based on the [PLCrashReporter framework](https://code.google.com/p/plcrashreporter/).

## How-tos and Tutorials

- In [Physics engines for dummies](http://www.wildbunny.co.uk/blog/2011/04/06/physics-engines-for-dummies/), Paul Firth explains in very simple terms how a physics engine works. Great tutorial for people like me who have always thought physics engines were some kind of magic.
- A good tutorial on how to [take photos with live video preview using AVFoundation](http://blog.red-glasses.com/index.php/tutorials/ios4-take-photos-with-live-video-preview-using-avfoundation/) in iOS 4 from someone named Adam.
- iDev Recipes has a post on [how to recreate the Twitter app’s side swiping table cells](http://idevrecipes.com/2011/04/14/how-does-the-twitter-iphone-app-implement-side-swiping-on-a-table/).
- As every month, Ray Wenderlich posted a bunch of great iOS tutorials on his site. The one I liked best: [How To Make A Simple Multiplayer Game with Game Center](http://www.raywenderlich.com/3276/how-to-make-a-simple-multiplayer-game-with-game-center-tutorial-part-12).

## Other

- This is cool: Dominic Szablewski wrote [iOS games entirely in Javascript](http://www.phoboslab.org/log/2011/04/ios-and-javascript-for-real-this-time) – but rather than running them in a `UIWebView`, he built Apple’s JavaScriptCore from source and uses it directly, rendering graphics with OpenGL. And Apple approved the apps.
- Mike Nachbaur criticizes Apple’s Core Data project templates and offers his own improved solution: [Smarter and more reusable Core Data](http://nachbaur.com/blog/smarter-core-data).
- Sometimes it can be confusing when and how often a certain Cocoa method is being called by the framework. Apple’s documentation should often be clearer about that in my opinion. Kevin Lohman has investigated [when `layoutSubviews` gets called](http://blog.logichigh.com/2011/03/16/when-does-layoutsubviews-get-called/). Very useful.
- The community of the highly popular Cocos2D game framework has begun to release beta builds of [CocosBuilder](http://cocosbuilder.com/), an Interface Builder-like app for Cocos2D apps.
- Many people have struggled with building “universal binary” static libraries for iOS in Xcode that include code for arm6, arm7 and i386 (for the iOS Simulator). To make this easier, Karl Stenerud has prepared [a project template for Xcode 4 to build a universal static framework for iOS](https://github.com/kstenerud/iOS-Universal-Framework).
- Mark Makdad has a look at the improved [unit testing support in Xcode 4 and how it stands up against the GHUnit framework](http://longweekendmobile.com/2011/04/15/unit-testing-in-xcode-4-use-ocunit-and-sentest-instead-of-ghunit/).
- James Hague: [Impressed by slow code](http://prog21.dadgum.com/98.html)

  > And that’s what’s impressive: code that is so easy to label as slow upon first glance, code containing functions that can–in isolation–be definitively proven to be dozens or hundreds of times slower than what’s possible on a given CPU, and yet the overall program is decidedly one of high performance.

# Design

- Ben Brooks: [Rules from a user to software developers](http://brooksreview.net/2011/04/rules/). A quick and easy list of points that will make your app better if you follow them.
- A leaked screenshot of the new iCal UI in the latest OS X Lion developer preview has provoked a lot of feedback, most of it negative. Ben Brooks makes the case to [not mimic real-world interfaces](http://brooksreview.net/2011/04/mimics/) in our apps.
- Because of its simple interface, the iPad is a great device for very young children. I’m sure you’ve seen the videos of two-year-olds using iOS devices expertly. Gabriel Weinberg wrote a cool article about [dos and don’ts when designing user interfaces for toddlers](http://www.gabrielweinberg.com/blog/2011/04/toddler-app-user-interface-guidelines.html). Best of all, most of the tips are also applicable to apps for people who can actually read.
- Peter Silfver has recommendations on [how best to use tab bars in your iOS app](http://www.significantpixels.com/2011/04/04/the-iphone-tab-bar/).
- [Lovely UI](http://www.lovelyui.com/), another site that collects screenshots of well-done UI designs. Nice collection.
- Justin Williams speaks against [Customization for customization’s sake](http://carpeaqua.com/2011/04/19/customization-for-customizations-sake/), noting that even the Tapbots, who invested so much effort into tweaking the Tweetbot UI, did not get everything right.

  > Never customize the interface of your application just for the sake of customization. Do it because you truly believe it offers a better experience over the standard iOS way for all of your users. There is a reason that Mac OS X and iOS don’t support theming out of the box and we have a deep seated hatred for cross-platform apps. Users expect apps to look and behave in a similar way no matter where they were developed.
- This has nothing to do with iOS but is one of my favorites of the month: Dropbox CEO Drew Houston turned an answer to the question [why Dropbox only syncs a separate folder](https://www.quora.com/Drew-Houston/What-was-the-genesis-of-requiring-a-Dropbox-folder-versus-allowing-me-to-designate-folders-like-documents-etc) into a great piece on user experience design. Initially done this way because it was the simplest way to do it, the “missing feature” quickly turned into Dropbox’s greatest strength: simplicity.

  > It’s also one of our core design principles to do fewer things rather than half-ass anything, and we couldn’t find a way to do multiple folders that wasn’t half-assed. Feature comparison lists and the like are foolish races to win for their own sake.

# App Store

- Companies monitoring the App Store rankings have noticed that Apple appears to have changed its ranking algorithm for free apps. Apparently Apple considers [more than just the number of downloads](http://arstechnica.com/apple/news/2011/04/apple-cleaning-up-app-store-rankings-by-deemphasizing-downloads.ars) to measure an app’s popularity. What other factors go into the calculation, I don’t know.
- Marco Arment talks about his experience when [he removed the free edition of Instapaper from the App Store](http://www.marco.org/2011/04/28/removed-instapaper-free). Not only did nobody complain, sales of the paid app also increased.

# Community

- Wil Shipley’s post [Success, and Farming vs. Mining](http://blog.wilshipley.com/2011/04/success-and-farming-vs-mining.html) was one of the most talked-about articles in my Twitter timeline this month.

  > If you’re building up a company for the sole purpose of looking good for one solitary moment – the day you go public – you’re not building for the future. You’re not (to waterboard my metaphor) maintaining the soil, making sure your animals are healthy and happy, and all that good husbandry stuff a good farmer does. Your only focus is looking like you’re going to achieve great sales in the future.
- In a very passionate post, Mike Lee makes a compelling case for [Appsterdam](http://mur.mu.rs/?p=1), his dream of making Amsterdam _the_ hub for app developers, the place where we go to for a working vacation or move to permanently:

  > I have traveled the world looking for the most livable city on earth, a place with the ideal balance of quality and price, history and vibrance, culture and innovation. That place is Amsterdam.

  I am seriously considering to see for myself and visit Amsterdam for a month (or two) this summer. Also see Mike’s follow-up post: [Appsterdam Revisited](http://mur.mu.rs/?p=82).
- Nice story by Matthew Panzarino for The Next Web: [Why you should want to pay for apps](http://thenextweb.com/apps/2011/04/24/why-you-should-want-to-pay-for-apps/?all=1). Includes opinions from the Tapbots and MarsEdit creator Daniel Jalkut who point out how and why the Apple community seems to be so different when it comes to paying for software.
