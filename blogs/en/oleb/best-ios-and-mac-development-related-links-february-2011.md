---
title: 'Best iOS and Mac Development-Related Links: February 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/03/best-ios-and-mac-development-related-links-february-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
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

- What’s New in Mac OS X v10.7 Lion
- Mac OS X v10.6 to v10.7 API Diffs

One especially interesting tidbit from the many thing that have already leaked about Lion is that apparently, Apple is going to ditch the vision of resolution independence and going the “Retina” display route on the desktop, as well: [people found @2x version of images in Lion](http://www.macrumors.com/2011/02/24/mac-os-x-lion-building-in-support-for-super-high-resolution-retina-monitors/).

Before the Lion preview came out, Andy Ihnatko [speculated about a future OS X/iOS mashup OS he calls iX](http://www.macworld.com/article/157824/2011/02/apple_ix.html). Interesting read.

# Programming

- iOS Debugging Magic

  that contains a lot of lesser-known tips and tricks. One example that made the rounds on Twitter is the undocumented method

  on

  that prints out an entire view hierarchy. Reading this document will make you a better programmer.
- Practical Design Patterns with Blocks and Grand Central Dispatch

  .
- Advanced drawing using AppKit

  .
- Compound Literals in C

  . The first comment on the post mentions a neat trick:
- Cocos2D

  now has a 3D companion:

  Cocos3D

  .
- how they develop a photo effect for Camera+

  . The best part: code included!
- potential starting points for performance optimization in iOS apps

  .
- RestKit

  looks like a nice library for interfacing with RESTful web services from your iOS app.
- Memory Management

  ,

  How To Debug Memory Leaks with Xcode and Instruments

  , and

  Using Properties

  . Highly recommended for beginners. Related: Keith Harrison’s post about properties,

  Understanding your (Objective-C) self

# UI Design

- iOS Inspires Me

  , “Showcase of the best looking iPhone & iPad app icons, app interfaces, app websites & resources”.
- Android Patterns

  is cool site that lists common UI design patterns on the Android platform. It is sort of like Apple’s Human Interface Guidelines, but extensible. Does anyone know of a similar site for iOS design patterns?
- Remnants of a Disappearing UI

  : how fingerprints on the iPad touchscreen can reveal which app was used.
- Langwich

  , an interesting new service to help translate your app into other languages.

# The App Store

- Apple launches subscriptions on the App Store

  .
- So much has been written about Apple’s intent to enforce the rule that app developers who provide access to paid content also have to offer In-App Purchase of the content, at the same or a lower price as outside the app, while still having to pay Apple its customary 30 % commission.

  Some of the many posts on the topic:

    - Apple rejects Sony’s reader app and wants a cut of e-book sales
    - Readability’s Open Letter to Apple

      after their app got rejected.
    - Subscriptions and the new In-App Purchase requirement

      asks, how does this rule affect services like Evernote and Dropbox or even third-party clients for these services? Probably not at all if

      this email from Steve Jobs is legit

      , but the wording of the rule is not clear.
    - About This Whole Subscription Hubbub
    - the policy is overall good for the users

      , which I suppose is true unless it leads to higher prices or an exodus of content apps from the App Store.
    - Apple’s Ambiguity: There’s an app for that

      .
    - 30% of the future

      .

  At this point, no one can be 100 % sure whom this rule will eventually affect and how, so I guess we’ll just have to wait until the June 30th deadline Apple has given developers to modify their apps.
- Ode to the App Review team

  for the great work they do and for the fact that the App Store mostly works to the users’ and developers’ advantage. I agree in principle, although it was a disappointment to have

  my Mac app Blue Planet in review for nearly three weeks

  recently.
- very interesting graphs about the sales performance of his successful iOS apps

  , Chopper, Chopper 2, and DuckDuckDuck.
- learnings from the iPad launch of World of Goo

  .

# The Competition

- Nokia CEO Stephen Elop in his memo to Nokia employees

  . A few days later, former Microsoft executive Elop announced that Nokia would adopt Windows Phone 7. Matt Drance in

  Microsoft Buys Nokia for $0B

  :
- first look at Honeycomb

  , the first Android version that is focused on tablets.
- roundup of HP’s webOS and TouchPad introduction event

  by Sebastiaan de With. The TouchPad looks good. Too bad we will have to wait another six months until it will be available.
-   - Love letter to WebOS

      that quickly turns into a rant about

      at their latest event.
    - You Win, RIM!

      An open lament about the setup, installation and deployment process of RIM’s SDK.

      RIM replies

      .
- still behind RIM’s and Nokia’s app stores

  in terms of revenue. No wonder most developers are sticking with iOS, despite Android having a similar market share. Monetization matters.
