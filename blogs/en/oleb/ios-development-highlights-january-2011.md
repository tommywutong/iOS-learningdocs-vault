---
title: 'iOS Development Highlights: January 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/01/ios-development-highlights-january-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c26c42507754d063'
translated: false
---

> 原文：[iOS Development Highlights: January 2011](https://oleb.net/blog/2011/01/ios-development-highlights-january-2011/)　·　Ole Begemann

# iOS Development Highlights: January 2011

I am a little late for this month’s recap of the iOS and Cocoa blogosphere, but it’s still January 31st in some parts of the world, so I guess that qualifies. Here is the (long) list of the posts I found most interesting this past month:

# The Mac App Store

The Mac App Store opened on January 6th and was obviously the big story of the month for both Mac and iOS developers.

- David Frampton on [App pricing strategies in the Mac App Store](http://majicjungle.com/blog/461/):

  > The amount of time the developer has spent, other development costs, Apple’s percentage cut, emotional investment, or ideological concerns do not in any way affect the price point at which an app will make the most money. Developers will continue to price higher because they think app store prices should be higher, or because they spent 6 months on the damn thing so it is worth $20, but these developers are leaving money on the table.
- Tim Morgan criticizes the App Store app because it does not conform to Apple’s Human Interface Guidelines: [The failures of the Mac App Store’s UI, and that of its app, Twitter 2.0](https://riscfuture.tumblr.com/post/2626504717/app-store-twitter-ui-failures).
- John Gruber replies: [Uniformity vs. Individuality in Mac UI Design](http://daringfireball.net/2011/01/uniformity_vs_individuality_in_mac_ui_design).

  > The HIG is dead. It died long ago. And it was Apple that killed it.

# Programming

- Niels Joubert presents some very good ideas in [Design Principles for Structuring iPhone Apps](http://blog.njoubert.com/2010/12/structuring-iphone-apps-design-principles.html). Your code will be better if you follow these patterns.
- Oliver Drobnik has started [an open-source project to create an `NSAttributedString` from HTML code](http://www.cocoanetics.com/2011/01/uiwebview-must-die/), a feature that is available on OS X and sadly absent in the iOS SDK. This should make creating attributed strings much easier.
- Oliver also [open-sourced MyAppSales](http://www.cocoanetics.com/2011/01/opensourceing-myappsales/), his iPhone app for scraping iTunes Connect sales reports.
- Mike Ash of Friday Q&A fame has self-published [the Complete Friday Q&A Archive in e-book form](http://www.mikeash.com/pyblog/complete-friday-qa-now-available.html). If you want to have some of the best Cocoa knowledge around the Web in easily accessible form or just want to support Mike, I suggest you buy his e-book, although all the content is available for free on his website. Mike also posted about [his experience in creating the book](http://www.mikeash.com/pyblog/writing-the-complete-friday-qa.html).
- Some fairly complex game programming tutorials were published in January. Ray Wenderlich wrote a two-part tutorial on [How To Create A Mole Whacking Game with Cocos2D](http://www.raywenderlich.com/2560/how-to-create-a-mole-whacking-game-with-cocos2d-part-1), and Rob from mobile bros. published [one on an Angry Birds-style game](http://www.cocos2d-iphone.org/archives/1214), also using Cocos2D in conjunction with Chipmunk and SpaceManager.
- Ray Wenderlich published another iOS tutorial: [How To Make a Simple RSS Reader iPhone App](http://www.raywenderlich.com/2636/how-to-make-a-simple-rss-reader-iphone-app-tutorial).
- In a post from October 2010, Bill Bumgarner [introduces the Heapshot Analysis tool in Instruments](http://www.friday.com/bbum/2010/10/17/when-is-a-leak-not-a-leak-using-heapshot-analysis-to-find-undesirable-memory-growth/) and explains how to use it to find abandoned memory in your app. If you want to see it in action, I also highly recommend the video for WWDC 2010 Session 311, “Advanced Memory Analysis with Instruments”.

# UI Design

- In [The iPhone is not easy to use: a new direction for UX Design](http://johnnyholland.org/2009/08/17/the-iphone-is-not-easy-to-use-a-peek-into-the-future-of-experience-design/), Fred Beecher argues that the iPhone, the very device that has been heralded for its user interface since its introduction, actually is surprisingly difficult to use — and that it doesn’t matter:

  > Fun is the New Usable … As a user experience designer, I thought my job was to make things not suck. Until recently. … Now, my job is to make things people love. … This is a crucial change, the importance of which cannot be overstated.
- Good UI design is all about attention to detail. I love the attention to detail these authors spent in posting about great attention to detail:

    - [Little Big Details](http://littlebigdetails.com/), a new blog from Berlin that shows us many examples of great attention to detail (not focused on iOS).
    - Basil Safwat on [how the iPhone Mail app decides whether to scroll up or not when new mail arrives](http://theinvisibl.com/2011/01/24/iphonemail/). It all depends on where you are in the list.
    - Mike Lee has all details [on the Mac Finder’s selection behavior](http://le.mu.rs/motherfucker/Entries/2011/1/24_Legendary_Selections,_Dude.html).

# Distribution

- [Testflight](http://www.testflightapp.com/), the new hot way to distribute your iOS betas to testers, came out of beta. I haven’t tried it yet, but the Twittersphere is raving about it.
- As the iOS App Store approached 10 billion downloads this month, Horace Dediu took a great look at the numbers: [More than 60 apps have been downloaded for every iOS device sold](http://www.asymco.com/2011/01/16/more-than-60-apps-have-been-downloaded-for-every-ios-device-sold/).

  > The amazing story of this chart is not that apps are running at above 30 million download per day, but that the figure is growing. Growth like this is hard to get one’s mind around. Not only are downloads increasing, but the rate of increase is increasing.

  Good times ahead for iOS developers.
- Shane from Blue Lightning Labs on the benefits of [asking your customers for reviews on the App Store](http://blog.bluelightninglabs.com/2011/01/asking-for-app-reviews/) and how to do that in a Mac app.
- Chad Podoski wrote a very detailed and insightful post [about promoting his iPad app, Flickpad](http://mobileorchard.com/ipad-app-marketing-case-study-flickpad/).

# The Competition

- Justin Williams, an iOS and Mac developer, writes about [switching from the iPhone to Windows Phone 7, both from a user and a developer perspective](http://carpeaqua.com/2011/01/02/from-iphone-to-windows-phone-7/). His post makes me want to try out the Windows Phone platform myself. For what it’s worth, I’d much rather explore the capabilities of Windows Phone 7 than expand to Android development at the moment (not that I’d have time for either).
- [Amazon announced that they will open an Android App Store](http://techcrunch.com/2011/01/05/amazon-android-app-store-2/) themselves. I haven’t heard more about this since the announcement, but I’m curious when it will launch for customers and how it will be received. Amazon certainly knows how to sell stuff and, more importantly, they already have a huge customer base who trusts them. Amazon also plans to experiment with pricing and it will be interesting how that turns out.
- Kyle Baxter: [Android Isn’t About Building a Mobile Platform](http://www.tightwind.net/?p=2543):

  > Android isn’t an attempt to build the best mobile platform and sell it on its merits; it’s a play to control the vast majority of the mobile market, secure eyeballs for Google advertising and eliminate any threat to Google.
- Nice [Engadget interview with Matias Duarte](http://www.engadget.com/2011/01/07/exclusive-interview-googles-matias-duarte-talks-honeycomb-tab/), the guy who designed Palm’s webOS and is now at Google doing UI design for Android 3.0 (25 min video).

# Other

- [Great Rands in Repose interview with Marco Arment](http://www.randsinrepose.com/archives/2011/01/25/interview_marco_arment.html), developer of Instapaper. Marco has some good advice for us indie developers:

  > The biggest design decision I’ve made is more of a continuous philosophy: do as few extremely time-consuming features as possible.
- Related: Isaac Hall replies to a question on Quroa [why Dropbox is so much more popular than other similar services](https://www.quora.com/Dropbox/Why-is-Dropbox-more-popular-than-other-tools-with-similar-functionality/all_comments/Isaac-Hall):

  > In the end, it really came down to one incredibly genius idea: Dropbox limited its feature set on purpose. It had one folder and that folder always synced without any issues — it was magic.
- Brittany Tarvin: [13 Reasons Why Software Is Not Free](https://wildchocolate.tumblr.com/post/2943819131/13-reasons-why-software-is-not-free).
