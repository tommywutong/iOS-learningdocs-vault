---
title: 'iOS and Mac Development Link Roundup: June 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/07/ios-and-mac-development-link-roundup-june-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:590ce62c6836c50a'
translated: false
---

> 原文：[iOS and Mac Development Link Roundup: June 2011](https://oleb.net/blog/2011/07/ios-and-mac-development-link-roundup-june-2011/)　·　Ole Begemann

# iOS and Mac Development Link Roundup: June 2011

Here is my summary of the past month in links:

# WWDC 2011

[WWDC is over](http://techcrunch.com/2011/06/07/wwdc-highlights/) and [the session videos are out](http://developer.apple.com/videos/wwdc/2011/). OS X Lion has lots of cool new features, though Mac developers have known about most of them for a while. The big WWDC news for developers: tons of new stuff in iOS 5 and, of course, iCloud, designed to become the next game changer. Gone is the digital hub, [the Mac demoted to just another device](http://daringfireball.net/2011/06/demoted).

Apple is betting on a vision that is different from Google’s, a world where the data lives in the cloud but access to it is hidden behind native apps. You don’t need a web browser to get the impression that your data is always there for you, no matter where you are and which device you use. For iCloud, Mac OS and iOS are equals. The cloud [just works](http://techcrunch.com/2011/06/08/apple-icloud-google-cloud/), to the extent that you shouldn’t even notice that it is there. Good news for Cocoa developers.

Another learning: Objective-C is [very much alive and kicking](http://clang.llvm.org/docs/AutomaticReferenceCounting.html). Apple seems totally committed to the language, and the switch to LLVM is a huge thing for the future improvement of the language. More good news for Cocoa developers.

# Programming

## Articles

- Matt Gallagher explains [a weak point in Objective-C’s weak typing typing](http://cocoawithlove.com/2011/06/big-weakness-of-objective-c-weak-typing.html): methods with the same selector but different argument or return types can lead to the wrong method being selected at runtime.
- Mike Ash illustrates the [similarities and differences between Objective-C blocks to C++0x lambdas](http://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html).
- In [My Fear of Middleware](http://gamesfromwithin.com/my-fear-of-middleware), Noel Llopis makes a great case against using frameworks like Cocos2D in game development. If you have an excellent grasp of the language and the technology you’re working with, all-encompassing libraries can sometimes hinder you more than they help. On the other hand, a framework like Cocos2D can save you tons of work if you’re a beginner. It all depends on the situtation.
- David Singleton: [Why mobile apps suck when you’re mobile](http://blog.davidsingleton.org/mobiletcp). Good explanation why TCP connections can suck so badly when used over a bad mobile link. Includes suggestions to improve your own networking code.
- Kelly Sommers turned her Continuous Client concept I mentioned last month [into an impressive cross-platform demo](http://kellabyte.com/2011/06/26/continuous-client-my-first-attempt-at-multi-device-user-experience-transitions/). No matter whether your immediate goal is something similar or not, a messaging-based approach to component design in your app seems like a good idea.
- Guy English takes [a close look at Apple’s Push Notification technology](http://kickingbear.com/blog/archives/202), the system that enables much of iCloud, and the competitive advantage such a high-capacity, OS-level service potentially gives them:

  > The thing is this, and it’s an important thing — always bet on the technologies that scale. … Apple is now betting that multiple applications maintaining their own connections to disparate servers will end up performing poorly on mobile devices. I believe they’re right.

## Components and Libraries

- Dave DeLong wrote [DDMathParser](https://funwithobjc.tumblr.com/post/6196535272/parsing-mathematical-expressions), an extensible parser for mathematical expressions.
- Another interesting parsing library is Tom Davie’s [CoreParse](https://github.com/beelsebob/CoreParse). It allows you to write your own tokenizer and parser with very little effort.
- The guys at enormego wrote [EGOTextView](https://github.com/enormego/EGOTextView), a rich text editor alternative for `UITextView`. Unfortunately, the included demo app doesn’t really show off any rich text formatting features. The code looks good, though.
- Jason Morrissey’s [JMTabView](https://github.com/jasonmorrissey/JMTabView) is a very stylish and good-looking tab view alternative. Rendered entirely using Core Graphics.
- Jim Dovey published [AQAppStateMachine](https://github.com/AlanQuatermain/AQAppStateMachine), a simple-to-use application state machine, designed to assist the development of applications with some fairly intricate state requirements.
- [SBTableAlert](https://github.com/simonb/SBTableAlert) by Simon Blommegård: a `UIAlertView` containing a `UITableView`, similar to what iOS uses in the Maps app when you search for a location and there are multiple matches.
- The guys at Gowalla published [AFNetworking](https://github.com/gowalla/AFNetworking), a nice-looking lightweight networking library based on `NSOperation` and blocks.
- [NPReachability](https://github.com/nickpaulson/NPReachability) by Nick Paulson: a blocks-based reachability implementation.
- The Cocos2D community set up [a repository of high-quality third party extensions for Cocos2D](https://github.com/cocos2d/cocos2d-iphone-extensions). Extensions include useful components such as scrollable menus, a slider control, a video player and much more.
- [Appledoc](http://www.gentlebytes.com/home/appledocapp/) is an older project that made the rounds on Twitter this month. It looks like a great tool to create nice-looking Objective-C API documentation that matches Apple’s own style.

## Tutorials

- Rather than writing a simple tutorial that illustrates one particular problem, Matt Gallagher leads us through [the design and implementation of a fairly complex RSS reader app for iOS](http://cocoawithlove.com/2011/06/process-of-writing-ios-application.html) from beginning to end. This is great learning material for anyone.
- Tutorial king Ray Wenderlich published an excellent [two-part tutorial on how to create a game like Tiny Wings](http://www.raywenderlich.com/3888/how-to-create-a-game-like-tiny-wings-part-1) (dynamic textures and all) using Cocos2D. Based on a [demo project by Sergey Tikhonov](https://github.com/haqu/tiny-wings). Earlier, Jean-Philippe Sarda also wrote an [article explaining the procedural graphics behind Tiny Wings](https://jpsarda.tumblr.com/post/6171831450/tiny-wings-hills-with-cocos2d). I can’t really tell which one is better.
- Someone calling himself CodePadawan published a nice post about [drawing buttons in the iOS Calculator app style entirely with Core Graphics](http://www.codepadawan.com/2011/06/iphone-glossy-buttons.html).
- Nice screencast by Patrick Hogan on [how to set up separate windows for Build Log and Console Output in Xcode 4](https://www.youtube.com/watch?v=0aYCsX4ifIA). The only downside: if you accidentally close one of the windows, it’s quite a lot of work to recreate it.

# Design

- Noel Llopis and Miguel Ángel Friginal, developers of the great iPad game _Casey’s Contraptions_, wrote [a detailed post-launch analysis](http://www.gamasutra.com/view/feature/6412/postmortem_llopis_and_friginals_.php). Great read. Make sure to read the comments, too. PocketGamer has [another good interview with the two about their game](http://www.pocketgamer.biz/r/PG.Biz/Casey%27s+Contraptions/feature.asp?c=30643).
- Kyle Neath shares [the design process of the new GitHub app for Mac](http://warpspire.com/posts/designing-github-mac/). It is an interesting account from a newcomer to both designing and developing Cocoa apps that helps to illustrate some of the weak points of AppKit and a lot of the cruft that has accumulated in AppKit over the years. Not all of his criticism is justified in my opinion. Interface Builder pretty useless? Come on. And:

  > Along those same lines, I think that Cocoa is dying for a framework. Something that weighs on the simple defaults side rather than complex code generation side.

  What does this even mean? Cocoa _is_ the framework. And the simple defaults are (among other things) the standard UI controls. You can build your own ff you don’t want to use the defaults, but you will have to work harder.
- Not specifically app-related: the awesome Kathy Sierra points out what all our design should boil down to: [Just make people better at something they want to be better at](http://gapingvoid.com/2011/06/07/pixie-dust-the-mountain-of-mediocrity/).

# App Store

Apple [backpedaled on the strict in-app subscription rules](http://www.macrumors.com/2011/06/09/apple-reverses-course-on-in-app-subscriptions/) they introduced in February. There is no longer a requirement that external content be offered through in-app purchase at all and at the same price or less than outside an app. This is a very welcome change before the June 30 deadline expired that Apple had set developers to comply with the rules.

With iA Writer for Mac as the example, Dan Wineman reminds us of [a useful lesson when pricing our own apps](http://venomousporridge.com/post/6531100630/commoditizing-complements): don’t try to commoditize your own product just because Apple does something similar. Apple is playing a different game. Oliver Reichenstein from Information Architects expands on this and compares the performance of iA Writer on the Mac App Store to the iOS App Store. Key finding: the two ecosystems are two very different beasts.

Martin Schultz [shares sales numbers of his game _Hard Rock Racing_ on the Mac App Store](http://forum.unity3d.com/threads/95001-Mac-App-Store-Sales-Results-from-Hard-Rock-Racing). Even after being featured by Apple and reaching the number 3 spot of paid games in the US, it sold only 743 copies on its best day.

David Heinemeier Hansson [argues that ten apps is all he needs](http://37signals.com/svn/posts/2959-ten-apps-is-all-i-need); competitors shouldn’t need a massive App Store to compete with Apple if they do the basic apps that everybody uses really well. David Barnard has a very good reply with [The Eleventh App](http://davidbarnard.com/post/6831261746/the-eleventh-app): every single user might only use a small number of apps but at least some of these apps will be different from person to person.

# Competition

- Battleheart developers Mika Mobile offer an interesting comparison of their app’s performance on the iOS App Store and the Android Market: [Part 1](https://mikamobile.blogspot.com/2011/06/android.html), [Part 2](https://mikamobile.blogspot.com/2011/06/some-more-android-stats.html). Monetization on iOS is still a lot stronger but Android seems to be catching up, especially considering that they found it to be easier to get high into the top charts on the Android Market.
- David Barnard: [Winning the Mobile Platform Race](http://davidbarnard.com/post/6760485722/winning-the-mobile-platform-race).

# Community

- Marcus Zarra sees a growing trend in the Cocoa developer community to unfairly criticize the work of others without knowledge of or respect for both the people involved and the constraints projects are under: [Why So Serious?](http://www.cimgf.com/2011/06/03/why-so-serious/) Marcus’s specific example is the bashing that the _The Daily_ app (where he was involved in the development) received by many.

  > Gone is the sharing and the live/let live attitude that once made this community so great. Quite a few members are just full of piss and vinegar. … What saddens me is this new desire to attack things that are either new or just in the media. Does the application suck? Maybe. But to curse the developers who wrote it? Not cool.

  I can’t say I agree with him but this is definitely something everybody should look out for.
- Brent Simmons sold NetNewsWire, one of the best-known indie Mac and iOS apps. In a [long interview on Daring Fireball](http://daringfireball.net/2011/06/netnewswire_black_pixel), Brent and Black Pixel’s Daniel Pasco discuss the reasons and NetNewsWire’s future. Very insightful.
- The [Appsterdam](http://mur.mu.rs/?p=196) community officially [kicked off their project](https://www.youtube.com/watch?v=HE8jb1HlK38) with a big launch event. I hope they can keep up the enthusiasm and find many imatators in other cities around the world. Anything that improves the community spirit is good for all of us.

# Legal

Patents are on their best way to become a recurring topic here.

After Lodsys’s decision [to sue some app developers over infringement](https://fosspatents.blogspot.com/2011/05/lodsys-sues-7-app-developers-in-eastern.html), Apple filed [a motion to intervene in the proceedings](https://fosspatents.blogspot.com/2011/06/apple-enters-fray-against-lodsys-files.html) on behalf of their developers. Meanwhile, several companies decided to file lawsuits against Lodsys ([one](https://fosspatents.blogspot.com/2011/06/all-four-lodsys-patents-under.html), [two](https://fosspatents.blogspot.com/2011/06/all-four-lodsys-patents-now-also.html), [three](https://fosspatents.blogspot.com/2011/06/two-more-lawsuits-against-lodsys-by-new.html), [four](https://fosspatents.blogspot.com/2011/06/novell-challenges-lodsyss-two-core.html)) with the aim of invalidating all four Lodsys patents, in response to which [Lodsys sued another ten companies](https://fosspatents.blogspot.com/2011/06/lodsys-sues-another-ten-companies.html) (bigger names this time), possibly to avoid more pre-emptive countersuits. Florian Mueller of [FOSS Patents](https://fosspatents.blogspot.com/) covered all this in admirable detail. We haven’t heard any news from the targeted app developers lately. It is probably safe to say that they have been in discussion with Apple and agreed to not talk publicly about it. Lodsys has apparently [asked for time until July 27, 2011, to answer Apple’s motion to intervene](https://fosspatents.blogspot.com/2011/06/lodsys-corrects-its-motion-for.html).

Macrosolve, the other company that is currently targeting app developers, sued [another 20 companies over a patent reagrding electronic forms](https://fosspatents.blogspot.com/2011/06/macrosolve-sues-another-20-companies.html).

What does this mean for developers? Craig Grannell offers [a grim outlook](http://reverttosaved.com/2011/06/01/lodsys-sues-ios-developers-over-in-app-payments-rebuffs-apple-and-thinks-you-should-love-it/):

> Dear developers: in future, make sure you check every aspect of everything you do against every patent that has ever existed, ever.

Meanwhile, it seems that all big phone companies are [happily suing each other](https://fosspatents.blogspot.com/2011/07/visualization-of-worldwide-patent-war.html). Who benefits? [Apple and Nokia settled their patent dispute last month](https://fosspatents.blogspot.com/2011/06/apple-and-nokia-settle-patent-dispute.html) with the probable result that Apple pays Nokia a per-iPhone royalty fee. Sounds bad for Apple but given that competitors are likely to infringe on the same patents it might actually be a good settlement.

To top it all off, an unlikely consortium of Apple, Microsoft and Sony (among others) [just paid $4.5 billion(!) for Nortel’s patent portfolio](http://www.macrumors.com/2011/07/01/nortel-patents-sold-to-consortium-which-includes-apple/). Crazy!

The more I read about this, the more I am convinced that the world would be a much better place if all patents were abolished. The only people profiting from this bullshit are the lawyers.
