---
title: 'iOS Development Highlights: December 2010'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/ios-development-highlights-december-2010/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:660a81f3f78d3960'
translated: false
---

> 原文：[iOS Development Highlights: December 2010](https://oleb.net/blog/2010/12/ios-development-highlights-december-2010/)　·　Ole Begemann

# iOS Development Highlights: December 2010

Despite the holidays, December has been a busy month in the iOS and Cocoa blogosphere. Here is a list of the posts I found most interesting this last month:

# Programming

- iDev Recipes

  is a great new site by Peter Boctor that aims to explain how to recreate certain features of popular apps in code. The first few posts are really promising. For instance, you can learn how to implement

  the scroll-down-to-go-to-the-next-article feature found in Reeder

  .
- how to make our apps accessible to visually-impaired users

  , but also presents a convincing argument why we should care: it takes surprisingly little effort and has the potential to improve many people’s lives considerably.
- a framework to construct complex `UITableViews` with heterogenous cells

  without the need for lengthy

  statements.
- constructing rich text views with clickable links

  on the Mac (e.g. for a Twitter client). Gus Mueller then

  improved Mike’s approach in another post

  . I am sure many people could use a control that did a similar thing on iOS.
- pragmatic approach to writing multithreaded apps

  . He comes up with some easy-to-understand rules on how background tasks should be encapsulated and communicate with each other that remind me a little of Apple’s memory management rules: stick to a few simple rules, and you’ll make your life a lot easier. I like it.
- Memory management and thread safety issues to consider when writing your own accessors

  .

  .\</li\>
- released the source code

  for

  Canabalt

  , one of my favorite iOS games. Yay! Their disclaimer:

# Design

- iOS Fonts

  is a useful new web site, showing the default fonts shipped on iPhone and iPad. The iPad comes with quite a few more typefaces.
- 10 Surefire Ways to Screw Up Your iPhone App

  . Good list of design dos and don’ts.
- Apps that work

  .
- laments the trend in app design to modify the behavior of standard controls

  , thereby confusing users. There is nothing wrong with innovative and non-standard UI design, but we really should beware of creating controls that look like a tab bar but act like a toolbar.
- Reeder

  . The

  beta version of Reeder

  has triggered some discussion about its design and how the porting of iOS apps to OS X affects app design on the desktop. Opinions:

    - This is the Future.(Bringing iOS to the Desktop: Why You Should Get Excited)
    - It doesn’t work.(Analysing a Touch-to-Desktop UI port using Fitt’s Law: Reeder for Mac Beta)

# The App Store and the Freelance Market

- App Store promo codes are now valid worldwide. Overdue.
- The Mac App Store opens on January 6, 2011.
- The iOS and Android App Economies

  given the similar market share of Android and iOS (at least in the US), the difference in developer adoption of the platforms is striking:

  If you actually wish to sell apps, the Android Market does not seem the place to be. And the fact that even the developers of a top-selling game like Angry Birds (on iOS) say that

  Free is the way to go with Android

  might ensure it remains that way. John Gruber:
- Year-End View of the Mobile Market

  , which is a look ahead to 2011 rather than a review of 2010. Interesting read.
- switching his free app to paid

  . It seems to have gone very well for him.
- a long piece with tips for both sides (Non-Deterministic Problems aka Finding Talent)

  how to find interesting work as a developer, how to find good developers as a client. Lucius Kwok tries to set clients’ expectations straight regarding

  how much the development of an app will cost

  .

Happy new year to all of you! Thanks for reading my blog.
