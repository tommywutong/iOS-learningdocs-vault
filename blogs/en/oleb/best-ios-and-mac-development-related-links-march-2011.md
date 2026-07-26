---
title: 'Best iOS and Mac Development-Related Links: March 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/04/best-ios-and-mac-development-related-links-march-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4917197872d36a31'
translated: false
---

> 原文：[Best iOS and Mac Development-Related Links: March 2011](https://oleb.net/blog/2011/04/best-ios-and-mac-development-related-links-march-2011/)　·　Ole Begemann

# Best iOS and Mac Development-Related Links: March 2011

**Update April 4, 2011:** I forgot to include some links when I first published this article. Late additions are marked as updates just as this paragraph.

Here is my summary of the past month in links:

# Inside Apple

[Bertrand Serlet](https://en.wikipedia.org/wiki/Bertrand_Serlet), longtime colleague of Steve Jobs and one of the most important engineers on NeXTSTEP and OS X, leaves Apple.

- [David Cásseres remembers how it was working for him](http://web.mac.com/casseres/Site/Blog/Entries/2011/3/23_Bertrand_Serlet_Leaves_Apple.html) in the early 2000’s, exposing a few interesting culture clashes between Apple and NeXT.
- [Wil Shipley also shares his impressions](http://blog.wilshipley.com/2011/03/celebrating-betrand-serlet-and-craig.html) of working with Serlet and his successor at Apple, Craig Federighi. Very good reading.
- A commenter on a Hacker News post [shares another great Serlet story](http://news.ycombinator.com/item?id=2359335):

  > So I typed in “Bertrand Serlet” into the search, and the first thing that popped up? malloc.c.
  > 
  > Seriously! The rest of the list was equally impressive including the original implementation of NSObject, a bunch of CoreFoundation, and on, and on. Avi Tevanian often gets credit for the work that he did on Mach, but Bertrand was most of the brains behind Cocoa.

WWDC 2011 got announced and sold out within 10 hours! For those lucky enough to get a ticket, be sure to read Jeff LaMarche’s [WWDC First Timer’s Survival Guide](https://iphonedevelopment.blogspot.com/2011/03/wwdc-first-timer-survival-guide-2011.html) and also Borkware’s very funny [First-Timer’s Guide to WWDC](http://borkwarellc.wordpress.com/2011/03/28/borkwares-first-timers-guide-to-wwdc/):

> The labs where you can chat with Apple engineers are an invaluable resource. It is a scarce, shared resource, so treat it like you would computationaly: pretend to be a mutex. You walk into the lab you want and shout “I AM ATTEMPTING TO OBTAIN A LOCK ON THE MEDIA PLAYER FRAMEWORK ENGINEERS”. If an engineer is free, you’ll hear “LOCK SUCCEDED” from the back, and you can go to the engineer who just shouted and ask your questions.

# Xcode 4 and a new OS X Lion Build

Apple released Xcode 4.0 at the beginning of the month, and the first bugfix release came out a few weeks later in the form of Xcode 4.0.1. I’ve been using Xcode 4 exclusively for nearly 3 months now and despite giving the impression that it’s not quite as finished and stable as a version 1.0 should be, I find it’s definitely an improvement over Xcode 3.2.

- Martin Pilkington wrote a [massive review of Xcode 4](http://pilky.me/view/15). Short of the Xcode 4 Transition Guide, it’s probably the most detailed overview of what’s new.
- Mike Clark from Pragmatic Studio has produced [10 free Transitioning to Xcode 4 videos](http://pragmaticstudio.com/screencast-tags/xcode4). Short and to the point, worth watching.
- Craig Hockenberry on how [Apple fucked up the documentation viewer](http://furbo.org/2011/03/17/great-writing-terrible-reading/) in Xcode 4.
- The LLVM 2.0 compiler in Xcode 4 apparently contains a bug that generates crashing code for the ARM6 architecture. See [this thread in the Apple developer forums](https://devforums.apple.com/thread/92279?start=0&tstart=0) for details (Apple developer account required).

A few days ago, Apple released the second developer preview of Mac OS X 10.7 Lion. To upgrade from the first developer seed, [be sure to run Software Update first](http://www.macstories.net/news/apple-releases-lion-developer-preview-update-1/), which contains a small update that enables you to download the new build from the Mac App Store. TechCrunch claims that internally, [Apple considers this build to be a “GM1”](http://techcrunch.com/2011/03/30/os-x-lion-new-build/), indicating that Lion is nearing release quality.

# Programming

- Sean Heber of the Iconfactory has reimplemented a substantial amount of iOS’s UIKit on Mac OS X, thereby providing OS X with an iOS-compatible, modern layer-based view system. The project that was originally built to port Twitterific from iOS to Mac OS X was now [made open source under the name Chameleon](http://chameleonproject.org/). I wonder if and when Apple will come out with something along these lines.
- Drew McCormack writes in great detail about the [evolution of a custom control](http://www.macresearch.org/cocoa-scientists-xxxiv-scrapbook-advanced-core-animation-view) for his app from paper draft to final code. This is a great post to learn about class design, Core Animation techniques, and performance optimization from a real-life example.
- Matt Long describes a very cool technique on [how to take advantage of `CATiledLayer`](http://www.cimgf.com/2011/03/01/subduing-catiledlayer/): just tell your view to use `CATiledLayer` as its layer and draw in `drawRect:` what it tells you to draw.
- Justin Williams: [Edge Cases Are Bugs Yet to Be Squashed](http://carpeaqua.com/2011/03/30/edge-cases-are-bugs-yet-to-be-squashed/)

  > Software development is about dealing with those edge cases gracefully and ensuring that an app has a fairly decent experience for a person who has 24 files and someone who has 2,400. It is our job to hate our code and find every which way to break it.
- Matt Gallagher provides [a history of iOS media APIs](http://cocoawithlove.com/2011/03/history-of-ios-media-apis-iphone-os-20.html) from iPhone OS 2.0 to iOS 4.3.
- Ray Wenderlich wrote a long [tutorial on how to implement in-app-purchases](http://www.raywenderlich.com/2797/introduction-to-in-app-purchases) in your app.
- [Mike Ash on random numbers](http://www.mikeash.com/pyblog/friday-qa-2011-03-18-random-numbers.html).
- Chris Murphy has written some insightful posts about the inner workings of Git and how you can use them to your advantage: [Git 102](http://cmurphycode.posterous.com/git-102) and [Git 201](http://cmurphycode.posterous.com/git-201-slightly-more-advanced).

## Late Additions

- The Mental Faculty Blog lists a very good example [what you could use Core Data’s user info table for](http://www.mentalfaculty.com/mentalfaculty/Blog/Entries/2011/3/8_On_the_Usefulness_of_Core_Datas_User_Info.html): here, specifying per-property actions for the copy & paste process.
- A couple of open-source Cocoa code directories seem to have popped up recently. [Cocoa Controls](http://cocoacontrols.com/) looks very good to me.
- [Eero](http://eerolanguage.org/from-objective-c-to-eero/) is a new Objective-C dialect developed by Andreas Arvanitis. Andy’s design goal: Removing the “Slum of Braces” from Objective-C. What I find interesting about this is not so much the new language itself but the fact that Andreas developed it with LLVM/Clang, showing how extensible Apple’s new compiler platform is.

# UI Design

- Om Malik [bemoans the state of iPad app design](http://gigaom.com/2011/03/05/ipad-may-be-magical-apps-arent-heres-why/). Where’s the magic? Malik hopes that the wonderfully-designed [GarageBand](http://www.apple.com/ipad/from-the-app-store/garageband.html) for iPad will bring the whole industry to lift iPad app design to a new level.
- In [The Evolution of Discoverability](http://uxmag.com/design/the-evolution-of-discoverability), Suzanne Ginsburg talks about how UI design for big touchscreen devices like the iPad has already improved from the first attempts a year ago. I like [Josh Clark’s comments](http://globalmoxie.com/blog/evolution-of-touchscreen-discoverability.shtml) about Suzanne’s post:

  > It’s useful to conceive of our [touchscreen] designs as infant-ready interfaces. Let your toddler lead the way. … Buttons are a hack.
- Danny Greg writes about his NSConference 2011 experience and how it focused very much on design: [Designers in Disguise](http://dannygreg.org/post/4069621218/designers-in-disguise).
- MG Siegler feels he has [hit the “app wall”](http://techcrunch.com/2011/03/05/the-app-wall/):

  > The app wall means that for every app in, one must go out. … If you’re not designing an app that is meant to be on the homescreen of every iPhone or Android phone out there, you’re not aiming high enough.
- Lukas Mathis [on multitasking](http://ignorethecode.net/blog/2011/03/04/multitasking/):

  > The argument that multitasking on computers is bad because humans can’t multitask is flawed. It uses the word “multitasking” in two different ways, but implies that the two kinds of multitasking are somehow the same thing. They’re not: a task (or an app) on a computer, and a task performed by a human don’t map to each other one-to-one.
- If you speak German, you should read Martin Pittenauer’s interesting [account of the creation of Carcassonne for iPhone and iPad](http://zuspieler.de/carcassonne-auf-dem-iphone/). From prototype to the first App Store release, it took the [Coding Monkeys](http://codingmonkeys.de/) approximately 2.5 person-years to complete this awesome game.
- If your app gets a [review like this one](http://mike3k.posterous.com/best-app-store-review-ever) on the App Store, consider yourself lucky. You just got thousands of dollars worth of design advice for free. Now back to the drawing board.

**Late addition:** Two sites collecting and categorizing UI patterns on mobile platforms, especially iOS: [Mobile UI Patterns](http://mobile-patterns.com/) and [Pttrns](http://pttrns.com/). Useful to see what other apps do and which usage patterns beyond Apple’s Human Interface Guidelines have already emerged on the platform.

# The App Store

- Two more posts on last month’s controversy about Apple’s new in-app-purchase rules:

    - John Gruber [argues largely from Apple’s point of view](http://daringfireball.net/2011/03/dirty_percent).
    - Joshua Benton responds: [To the victor goes the pricing power](http://www.niemanlab.org/2011/03/john-gruber-on-apples-30-cut-to-the-victor-goes-the-pricing-power/).
- Great insight by John Siracusa, who comes at it from a different angle: [The Apple strategy tax](http://arstechnica.com/staff/fatbits/2011/03/the-apple-strategy-tax.ars):

  > Apple can try to be a good platform owner and ensure that popular apps like Kindle and Netflix thrive on iOS, and it can also try to advance its own competing services, but both efforts cannot succeed to their fullest potential.
- Manton Reece: [Where Apple went wrong with free apps](http://www.manton.org/2011/03/where_apple.html):

  > We take for granted now that much of the App Store’s success is because of free apps, but I’m not sure it had to be that way. The iTunes Music Store launched with a full paid catalog of music. Many of the hits in the App Store, like Angry Birds and Doodle Jump, have never been free. … Apple can’t accept a future in which too many apps are technically free — something that has already happened on Android — unless they are also taking a cut when money changes hands outside of app download.
- Justin Williams: [‘Useless’ Is a Loaded Word](http://carpeaqua.com/2011/03/28/useless-is-a-loaded-word/)

  > Here is a tip for all the non-developers out there. When you email your favorite developer with a feature request or bug report never, ever, ever use the word useless to describe their product. Useless is kryptonite to developers and puts us on the defensive instantly.

**Late addition:** Following up on John Siracusa’s strategy tax article, someone named alx names [trust](https://statictext.tumblr.com/post/3676219047/trust) as the reason Steve Jobs and Apple feel the need to build their own solution for every major new use case of their devices, be it listening to (and buying) music, reading e-books, or doing video chat:

> You have to tell the whole story, how your product uses all that technology to do things better and faster, things that are not even possible on other devices. And you can’t trust third party developers to do it for you. … Every aspect of the hardware has to have a counterpart in the software that can be used in a real world scenario. They would never include a hardware component without a killer way to take advantage of it in the software on day one.

Great read.

# The Indie Community

Finally, I love this post by Ben Zotto, creator of Penultimate for the iPad: [Designing A Software Atelier](http://blog.cocoabox.com/post/3727157793/designing-a-software-atelier). I think the way Ben wants to grow his business is what many indie developers can identify with.

> Here’s my goal: I’d like to create a high-quality, high-design mobile software “atelier”. Picture a small number of great developers, designers and others working together to create software on the platforms that are on the verge of taking over the world. Smart, interesting people who appreciate design and craftsmanship in software (and probably outside software as well), and who demand to work with others who value that.
