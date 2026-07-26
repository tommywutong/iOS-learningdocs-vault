---
title: 'iOS and Mac Development Link Roundup: August 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/08/ios-and-mac-development-link-roundup-august-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:3539ccbdb297e475'
translated: false
---

> 原文：[iOS and Mac Development Link Roundup: August 2011](https://oleb.net/blog/2011/08/ios-and-mac-development-link-roundup-august-2011/)　·　Ole Begemann

# iOS and Mac Development Link Roundup: August 2011

August is traditionally the month of slow news. Not so in this year’s tech scene. The patent war between the giant tech companies is becoming hotter and hotter. I have long lost track of who is suing whom, but Apple seems to be better positioned than most other players. [Google buys Motorola](https://googleblog.blogspot.com/2011/08/supercharging-android-google-to-acquire.html), presumably at least partly [for its patent portfolio](http://thisismynext.com/2011/08/15/google-motorola-patents-for/). HP wants to get rid of its PC business, [killing off WebOS on the way out](http://www.hp.com/hpinfo/newsroom/press/2011/110818b.html). [Apple became the world’s most valuable public company](http://techcrunch.com/2011/08/09/apple-exxon-valuable-company/). And [Steve Jobs resigned as CEO](http://www.apple.com/pr/library/2011/08/24Letter-from-Steve-Jobs.html).

What are the implications of all of this for us developers? Probably none in the short term but it will keep being interesting what happens next. Here is my summary of the past month in programming-related links:

# Programming

- Brent Simmons shared [some useful little tips](http://inessential.com/2011/08/04/less_code_less_effort) that make you write better and, at the same time, less code. I already followed most of these but I haven’t spent much time with [`NSCache`](http://developer.apple.com/library/mac/#documentation/Cocoa/Reference/NSCache_Class/Reference/Reference.html) (though other people report that [`NSCache` is very slow](http://inquisitivecocoa.com/2009/12/27/nscache-is-slow/) so don’t use it blindly).
- In [Writing high-quality view controller containers](https://subjective-objective-c.blogspot.com/2011/08/writing-high-quality-view-controller.html), Samuel Défago shows how to implement a reliable view controller container that takes care of forwarding rotation and lifecycle events to its child controllers. Writing custom view controllers that contain other view controllers is unfortunately not a trivial matter in iOS 4.
- Samuel also [published CoconutKit](https://subjective-objective-c.blogspot.com/2011/08/announcing-coconutkit.html), an open-source library that contains several very useful additions to UIKit and Foundation (including the view controller containers mentioned above).
- Mike Ash explains the possible problems that can arise [when multiple methods in Objective-C share the same selector](http://www.mikeash.com/pyblog/friday-qa-2011-08-05-method-signature-mismatches.html) but have different argument and/or return types. Another reason to pay close attention to every single compiler warning.
- Noel Llopis [compares different analytics engines](http://gamesfromwithin.com/analytics-for-ios-games) for iOS. He ends up recommending [Localytics](http://www.localytics.com/app-analytics/) for both its functionality and its very small footprint in your executable.
- [StackScrollView](https://github.com/raweng/StackScrollView) is an iPad project by raw engineering that aims to reproduce the stacking panel behavior of Twitter’s iPad app.
- [QuickDialog](https://github.com/escoz/QuickDialog) by Eduardo Scoz is a library to simplify building forms or setting screens with table views in iOS. It’s one of many components that do such a thing but it looks quite advanced to me. What I don’t like about the approach: it uses a view controller as its base class instead of a plain view. That should make it more difficult to embed in a view that should also contain other elements.
- Steve Gifford publishes [WhirlyGlobe](https://code.google.com/p/whirlyglobe/), an open source iOS toolkit for displaying an interactive 3D globe in OpenGL.
- Techcrunch revealed that Apple is going to deprecate access to the UDID in iOS 5. While deprecation is only the first step towards removal of that feature, I think it is a good step. Free access to the UDID made it far too easy [for ad networks and analytics companies](http://blog.securemacprogramming.com/2011/08/on-device-identifiers/) to [track users across apps](http://blog.appblade.com/news/2011/08/essentials-of-apples-udid/). This will still be possible in the future via the MAC address, but at least Apple doesn’t hand them the functionality on a silver platter.
- David Linsin wrote an article on [writing Cocoa code with Jetbrains’ AppCode IDE](https://dlinsin.github.com/2011/08/27/AppCode.html) rather than Xcode. His report is quite favorable; I should take a look some day.
- [Parse](https://www.parse.com/) is an interesting new service, currently in beta, that aims to offer an easy-to-use web service backend to mobile app developers. Definitely fills a gap, together with [StackMob](http://www.stackmob.com/). Neither company has published their intended pricing, so it’s hard to evaluate. Also, competing with iCloud (which has no server component at the moment, though).

# Design

- In [Windowless Skyscraper](http://www.red-sweater.com/blog/2065/windowless-skyscraper), Daniel Jalkut makes a case for the importance of polishing an app:

  > But customers don’t care about the hard work that went into the 90%. They only notice the flaws or omissions in the 10%. … An important takeaway for software developers is that the missing 10%, or the missing one-tenth of 10%, may be something that will take a great deal of work to get right, but it may be something you simply overlooked the importance of.
- Miguel Ángel Friginal writes about the challenges he faced while [designing the iPhone version of Casey’s Contraptions](http://mysterycoconut.com/blog/2011/08/designing-casey-3/), the successful iPad game.
- [Photoshop file with Lion UI elements](http://dribbble.com/shots/233227-Lion-Ui-Kit-Preview) for your next app design by Jonatan Castro.
- Matt Gemmell: [Developers should learn from Apple’s user-centric approach](http://www.tapmag.co.uk/blog/matt-gemmell-explains-what-devs-should-learn-apples-user-centric-approach-24-08-2011):

  > Forget trying to have the most features – as your users will tell you, it’s all about the experience of using your finished app. … The success of iOS (and Apple) is largely due to focusing ruthlessly on the user, and understanding that the best way to do that is to make the hard choices before ever releasing a product. Remove features. Get rid of options. Don’t ask the user to make decisions.
- Aen Tan examines [the proportions of iOS UI elements from a grid perspective](http://aentan.com/design/new-visual-proportions-for-the-ios-user-interface/) and has a rather unfavorable verdict for Apple. Realigning the elements on a 4-point grid supposedly yields a better-proportioned design, though I hardly see the difference. To be honest, I don’t really see the point of a 4 × 4 grid. While 4 might be a nice round number to divide everything by, it is so small to become almost meaningless. After all, everything fits in a 1 × 1 grid. Also, it drives me nuts that he talks about pixels and not points all the time.

**Update September 1, 2011:** Dion Almaer reveals [the amount of care and work that went into the design of a single credit card entry field](http://functionsource.com/post/beautiful-forms) of the _Square_ iPhone app. Attention to detail is everything!

# Sales and Monetization

- The Omni Group put up a post on Lion adoption among their customers: within the first 20 days of Lion’s release, [Lion usage was already over 30%](http://www.omnigroup.com/blog/lion_adoption/). That’s encouraging for developers who are thinking about dropping support for Snow Leopard soon.
- Similarly, see [Adium’s usage stats of this week](http://sparkle.adium.im/?year=2011&week=35&graph=bar) (late August, 2011): 24% of the users are on Lion (and interestingly, 17% are still on 10.5. I wonder why; it can’t be PowerPC users as those make up only 3.5% of all machines).
- Marco Arment shared his [device and version stats for Instapaper](http://www.marco.org/2011/08/13/instapaper-ios-device-and-version-stats-update): currently, 98% of his customers are on iOS 4.0+ and 92% have an iPhone 3Gs or better (i.e., a device that is capable of running iOS 5). If you ask me, iOS developers that still support iOS 3.x in their next version are doing something wrong.
- Interesting thoughts by Federico Viticci for MacStories: users need to [build up trust for indie developers](http://www.macstories.net/stories/a-trusted-system/), otherwise they won’t invest time into switching to a new app. Developers can build trust with their audience by providing great support and regular updates.[1](#fn:1)
- [Business Insider interview with Dominique Leca](http://www.businessinsider.com/dom-leca-interview-sparrow-2011-8?op=1), co-creator of the Sparrow mail client for OS X. Sparrow made more than $500,000 in the half year since its introduction.
- Jeremy Olson, creator of the _Grades 2_ app, reports [impressive download numbers and lots of press after winning the Apple Design Award](http://tapity.com/grades/so-hows-it-going/). Unfortunately, more than 150,000 downloads of the free app resulted in no more than a few hundred dollars of revenue from in-app purchases and ads, though.
- In late 2008, when the iOS App Store was 6 months old, tap tap tap sold its successful _Where To?_ app to FutureTap in the first acquisition of the App Store era. Now, two and a half years later, Ortwin Gentz from FutureTap [reports how well the app did in an amazing infographic](http://taptaptap.com/blog/where-to-three-exciting-years/): after buying the _Where To?_ for $70,000, it generated just over $500,000 of revenue for FutureTap, who continually invested in improving the app and adding new features.

# Competition

- Fantastic account by Nick Farina about [his experience converting an iOS app to Android and developing for Android in general](http://nfarina.com/post/8239634061/ios-to-android).
- The iOS App Store might not be all perfect but it seems the grass is hardly greener on the other side. the guys at Shift Jelly reported on [a bad deal they agreed to make with Amazon](http://shiftyjelly.wordpress.com/2011/08/02/amazon-app-store-rotten-to-the-core/) who would promote their app on Amazon’s Android app store heavily for one day while making it free at the same time. What really makes this a bad story for Amazon in my opinion is not that deal itself (after all, both parties agreed to it). But the fact that [Amazon publicly guaranteed that developers would always make at least 20% of their list price](http://techcrunch.com/2011/08/02/amazons-appstore-youll-make-0-when-we-give-your-app-away-and-youll-like-it/) (even if Amazon gave the app away for free) and then privately changed the rules, potentially leaving customers and other developers in the dark about who profited from these promotions, makes them very unreliable business partners. Quote from the Techcrunch article:

  > And I was very clearly told that even if Amazon decided to make an app free, developers would still be making 20% of their list price. In other words, they’d still make money. So much for that idea.

  Also read Shift Jelly’s [follow-up post](http://shiftyjelly.wordpress.com/2011/08/17/the-dust-has-settled/), exposing another killer term in Amazon’s developer agreement: if you want to remove an app from Amazon’s app store, you are required to also remove it from Similar Services a.k.a. Google’s Android Market. I really hope developers won’t sign such a thing.
- As HP kills off WebOS, at least until they find a buyer (Amazon?), Ian Beck, who is selling a WebOS app, shares his [thoughts and hopes on the future of the platform](http://beckism.com/2011/08/webos-future/):

  > I have been re-investing my profits from TapNote development back into TapNote … and my goals and plans for the app all revolved around incremental improvements leading to long-term growth. Now my investments both of time and money are looking like very poor choices indeed.
- If you are interested in learning Windows Phone 7 development, [Microsoft is giving away Charles Petzold’s 1,000-page monster _Programming Windows Phone 7_ as a free ebook](http://blogs.msdn.com/b/microsoft_press/archive/2010/10/28/free-ebook-programming-windows-phone-7-by-charles-petzold.aspx) (in DRM-free PDF, ePub and Kindle formats). Nice gesture!

# Patents

- Mike Lee and the Appsterdam movement are planning to defend against Lodsys and others. Together with attorney Michael McCoy, [the Appsterdam Legal Defense Team and Fund is being set up](http://mur.mu.rs/?p=303). There haven’t been any news since the beginning of August, but I am very eager to see what they come up with. I’d strongly consider making a contribution to Operation Anthill.
- It’s good to see that [Apple insists to intervene in the Lodsys lawsuit](https://fosspatents.blogspot.com/2011/08/apple-insists-to-intervene-in-lodsys.html) despite Lodsys’s heavy opposition. While it might not help directly in the short term, Apple’s engagement is very good news for app developers.
- Google has adopted a different strategy than Apple and has [filed reexamination requests against two Lodsys patents](https://fosspatents.blogspot.com/2011/08/googles-reexamination-requests-against.html) with the US Patent and Trademark Office. These may indeed prove to be [devastating](http://www.groklaw.net/article.php?story=20110817200754569) to Lodsys in the long run but don’t help the Android developers much that have already been sued.
- Meanwhile, Lodsys continues to sue more and more developers on all platforms, [including BlackBerry](http://www.theglobeandmail.com/report-on-business/industry-news/the-law-page/small-blackberry-developer-in-patent-companys-sights/article2147597/). ~~Florian Mueller tweeted about [the first attack on a BlackBerry app developer](https://twitter.com/FOSSpatents/status/107287630173057024) he heard of.~~
-   - Nilay Patel

      for The Next Web.
    - Lukas Mathis

      .
    - Timothy B. Lee for Ars Technica

      .
    - David Barnard

      .
    - Mark Cuban

      .
- patent pledge

  to not sue companies with less than 25 people for software patent infringement. That wouldn’t help against patent trolls but at least it could raise awareness of the issue.

1. I love it that Federico cites my friend and fellow Berlin-based developer Oliver Fürniß, creator of [Mr. Reader](http://www.curioustimes.de/mrreader/) as a prime example of such a trusted indie developer. [↩︎](#fnref:1)
