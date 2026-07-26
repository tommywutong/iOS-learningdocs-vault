---
title: 'iOS Development Highlights: December 2010'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/ios-development-highlights-december-2010/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:660a81f3f78d3960'
translated: false
---

> 原文：[iOS Development Highlights: December 2010](https://oleb.net/blog/2010/12/ios-development-highlights-december-2010/)　·　Ole Begemann

# iOS Development Highlights: December 2010

Despite the holidays, December has been a busy month in the iOS and Cocoa blogosphere. Here is a list of the posts I found most interesting this last month:

# Programming

- [iDev Recipes](http://idevrecipes.com/) is a great new site by Peter Boctor that aims to explain how to recreate certain features of popular apps in code. The first few posts are really promising. For instance, you can learn how to implement [the scroll-down-to-go-to-the-next-article feature found in Reeder](http://idevrecipes.com/2010/12/28/how-does-the-reeder-iphone-app-swipe-up-and-down-between-articles/).
- Matt Gemmell not only explains [how to make our apps accessible to visually-impaired users](http://mattgemmell.com/2010/12/19/accessibility-for-iphone-and-ipad-apps), but also presents a convincing argument why we should care: it takes surprisingly little effort and has the potential to improve many people’s lives considerably.
- Matt Gallagher presents [a framework to construct complex `UITableViews` with heterogenous cells](http://cocoawithlove.com/2010/12/uitableview-construction-drawing-and.html) without the need for lengthy `switch` statements.
- Mike Rundle wrote about [constructing rich text views with clickable links](http://flyosity.com/mac-os-x/clickable-tweet-links-hashtags-usernames-in-a-custom-nstextview.php) on the Mac (e.g. for a Twitter client). Gus Mueller then [improved Mike’s approach in another post](http://shapeof.com/archives/2010/12/customizing_links_in_an_nstextview.html). I am sure many people could use a control that did a similar thing on iOS.
- Brent Simmons explains his [pragmatic approach to writing multithreaded apps](http://inessential.com/2010/12/05/some_notes_on_threading). He comes up with some easy-to-understand rules on how background tasks should be encapsulated and communicate with each other that remind me a little of Apple’s memory management rules: stick to a few simple rules, and you’ll make your life a lot easier. I like it.
- Mike Ash: [Memory management and thread safety issues to consider when writing your own accessors](http://www.mikeash.com/pyblog/friday-qa-2010-12-03-accessors-memory-management-and-thread-safety.html). More Complicated Than You Might Think.\</li\>
- The great guys at Semi Secret [released the source code](http://blog.semisecretsoftware.com/nearly-25000-raised-for-charity-canabalt-goes) for [Canabalt](http://www.canabalt.com/), one of my favorite iOS games. Yay! Their disclaimer: We wanted to offer our condolences to everyone who downloads this and goes poking around in there. This was a rushed Flash game, ported, in a rush, to the iPhone, before iPads or iPhone4s even existed.

# Design

- [iOS Fonts](http://iosfonts.com/) is a useful new web site, showing the default fonts shipped on iPhone and iPad. The iPad comes with quite a few more typefaces.
- Jeremy Olson for UX Magazine: [10 Surefire Ways to Screw Up Your iPhone App](http://uxmag.com/design/10-surefire-ways-to-screw-up-your-iphone-app). Good list of design dos and don’ts.
- If you want to create a successful mobile app, it is not enough to have a “great idea”. Apps must also fit into the context where people actually use their phones, or they will probably fail. Dave Addey discusses what an app needs to be successful: [Apps that work](http://tmik.co.uk/?p=442).
- Milind Alvares [laments the trend in app design to modify the behavior of standard controls](http://smokingapples.com/opinion/standards-ui-higs/), thereby confusing users. There is nothing wrong with innovative and non-standard UI design, but we really should beware of creating controls that look like a tab bar but act like a toolbar.
- With the launch of the Mac App Store imminent, we are beginning to see the first successful iOS apps being ported to the Mac. One of the most prominent is RSS reader [Reeder](http://reederapp.com/). The [beta version of Reeder](http://madeatgloria.com/brewery/silvio/reeder) has triggered some discussion about its design and how the porting of iOS apps to OS X affects app design on the desktop. Opinions:

    - David Appleyard on AppStorm: [This is the Future.(Bringing iOS to the Desktop: Why You Should Get Excited)](http://mac.appstorm.net/general/opinion/bringing-ios-to-the-desktop-why-you-should-get-excited/)
    - Daniel Kennett’s verdict: [It doesn’t work.(Analysing a Touch-to-Desktop UI port using Fitt’s Law: Reeder for Mac Beta)](http://danielkennett.org/blog/2010/12/analysing-a-touch-to-desktop-ui-port-using-fitts-law-reeder/)

# The App Store and the Freelance Market

- App Store promo codes are now valid worldwide. Overdue.
- The Mac App Store opens on January 6, 2011.
- John Gruber on [The iOS and Android App Economies](http://daringfireball.net/2010/12/ios_android_app_economies:) given the similar market share of Android and iOS (at least in the US), the difference in developer adoption of the platforms is striking: iOS’s best apps could exist for Android but don’t. Android’s best apps couldn’t exist for iPhone. If you actually wish to sell apps, the Android Market does not seem the place to be. And the fact that even the developers of a top-selling game like Angry Birds (on iOS) say that [Free is the way to go with Android](http://technmarketing.com/iphone/peter-vesterbacka-maker-of-angry-birds-talks-about-the-birds-apple-android-nokia-and-palmhp/) might ensure it remains that way. John Gruber: The economy for Android apps may well trend toward resembling the economy of the web.
- Tim Bray, developer advocate for Android at Google, published his [Year-End View of the Mobile Market](http://www.tbray.org/ongoing/When/201x/2010/12/28/Mobile-Market), which is a look ahead to 2011 rather than a review of 2010. Interesting read.
- Brian Stormont writes about the results of [switching his free app to paid](http://blog.stormyprods.com/2010/12/switching-iphone-app-from-free-to-paid.html). It seems to have gone very well for him.
- The market for freelance app developers is a ongoing topic. Jeff LaMarche wrote [a long piece with tips for both sides (Non-Deterministic Problems aka Finding Talent)](https://iphonedevelopment.blogspot.com/2010/12/non-deterministic-problems-aka-finding.html:) how to find interesting work as a developer, how to find good developers as a client. Lucius Kwok tries to set clients’ expectations straight regarding [how much the development of an app will cost](https://felttip.tumblr.com/post/2350294498/so-you-want-to-hire-an-ios-developer).

Happy new year to all of you! Thanks for reading my blog.
