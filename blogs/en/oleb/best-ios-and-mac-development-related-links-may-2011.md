---
title: 'Best iOS and Mac Development-Related Links: May 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/best-ios-and-mac-development-related-links-may-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:384ab25570c2ccfe'
translated: false
---

> 原文：[Best iOS and Mac Development-Related Links: May 2011](https://oleb.net/blog/2011/06/best-ios-and-mac-development-related-links-may-2011/)　·　Ole Begemann

# Best iOS and Mac Development-Related Links: May 2011

Here is my summary of the past month in links:

# Lodsys

The story of the month was certainly that of [patent troll](https://en.wikipedia.org/wiki/Patent_troll) Lodsys. In chronological order:

On May 13th, James Thomson tweeted that he was [threatened with a patent infringement lawsuit over in-app purchase](https://twitter.com/jamesthomson/status/68992803472015360) by (what we later learned) Lodsys, [together with handful of other small developers](http://www.cultofmac.com/ios-devs-under-fire-by-patent-troll-for-offering-in-app-purchases/94916).

While the developer community waited for Apple to respond, Lodsys tried to explain themselves to the public in [a series of blog posts](http://www.lodsys.com/1/post/2011/05/q-why-is-lodsys-contacting-application-publishers-and-website-publishers-rather-than-operating-system-vendors-or-device-manufacturers.html). Craig Grannell [took them apart](http://reverttosaved.com/2011/05/16/lodsys-responds-to-trolling-accusations-regarding-ios-in-app-payments/). Meanwhile, the EFF asked Apple to [stand up and defend their developers](https://www.eff.org/deeplinks/2011/05/apple-should-stand-up) and Mike Lee proposed that developers [boycott the in-app purchasing API](http://mur.mu.rs/?p=126) to show both the patent trolls what we think and Apple what we expect of them:

> What I propose is this: for every API that is infected by parasites, we cut off the branch and boycott the API. I don’t think it’s unreasonable to expect to be able to use an API without being sued, the same way it’s not unreasonable to expect to use an API without getting spam.

Craig Hockenberry of the Iconfactory wrote [an open letter to Steve Jobs](http://furbo.org/2011/05/23/predators/). With the deadline set by Lodsys approaching, some people reasonably started [suggesting for targeted developers to cooperate with Lodsys](https://fosspatents.blogspot.com/2011/05/in-absence-of-blanket-coverage-from.html) in order to avoid a very costly lawsuit.

On May 23rd, [Apple finally responded publicly by publishing a letter sent to Lodsys](http://www.macworld.com/article/160031/2011/05/apple_legal_lodsys_letter_text.html), claiming that app developers are protected by the license Apple has acquired to the Lodsys patents.

Many expected Lodsys would now retract their claims and this would be over, others warned that [Lodsys could still decide to sue](https://fosspatents.blogspot.com/2011/05/analysis-of-apples-letter-to-lodsys.html). And that’s what they did: in response to Apple’s letter, on May 31st [Lodsys publicly disputed Apple’s assertion that their license covers app developers](http://www.lodsys.com/1/post/2011/05/apples-license-claim-disputed1.html) and announced that they have sued seven relatively small iOS app developers, among them the Iconfactory and Quickoffice.

Florian Mueller at [FOSS Patents](https://fosspatents.blogspot.com/) has covered not only [that last part](https://fosspatents.blogspot.com/2011/05/lodsys-sues-7-app-developers-in-eastern.html) but the whole case extensively.

Unfortunately, this story is not over yet. I can’t imagine how bad it must feel to be faced with such a meaningless and potentially destructive lawsuit. I really hope we as a community can do our best to help those unlucky seven. Also, let’s not forget that while the Lodsys case gets all the attention, a company named [MacroSolve has also sued small developers over patent infringement](https://fosspatents.blogspot.com/2011/05/worse-than-lodsys-macrosolves-sues.html).

It will be interesting to see if Steve Jobs decides to talk about it during the WWDC keynote next week. I think it would mean a lot to developers if he did.

# Programming

Let’s move on to happier news:

- [DCIntrospect](http://domesticcat.com.au/projects/introspect/) by Domestic Cat Software is a very clever library that helps you debug your user interfaces in the iOS Simulator. Similar to CSS box-model visualizers, it can outline the dimensions and other properties of your views, and by integrating with the Mac’s keyboard, it doesn’t interfere with the rest of your app.
- Matt Gallagher posted a set of [reusable classes for fetching and parsing XML or JSON via HTTP](http://cocoawithlove.com/2011/05/classes-for-fetching-and-parsing-xml-or.html). This is not so much about the code itself (which is quite straightforward to write) but about the design: it is much better to put your network and parsing code into reusable classes than to stuff it directly into your view controller class.
- Nice tutorial by Saul Mora on [how to make Core Data work in a multithreaded environment](http://www.cimgf.com/2011/05/04/core-data-and-threads-without-the-headache/) with the help of blocks and GCD.
- Sam Vermette wrote [SVSegmentedControl](http://samvermette.com/255), a customizable version of `UISegmentedControl`. It animates when switching from one segment to the next, similar to both `UISwitch` and the redesigned tab views Apple had used in the first developer previews of Mac OS X Lion but now seems to have abandoned. Looks great.
- [Benjamin Godard](http://www.cocoabyss.com/) has published [NYXImageUtilities](https://github.com/Nyx0uf/NYXImagesUtilities), a collection of useful `UIImage` categories for filtering, resizing, masking, rotating, and saving to different file formats.
- Gustavo from CodeCrop has written [a useful `NSMutableDictionary` category that knows about image metadata such as geo coordinates and EXIF data](http://blog.codecropper.com/2011/05/adding-metadata-to-ios-images-the-easy-way/). It makes saving an image with metadata very easy.
- Noel Llopis blogged about [the difficulties in achieving determinism](http://gamesfromwithin.com/casey-and-the-clearly-deterministic-contraptions) (something we usually taked for granted when working with computers) in his new game Caseys’ Contraptions:

  > Same input should create the same output. Not really. We’re missing the most crucial input: The timer. Casey’s Contraptions runs at 60 fps on an iPad one, but the timestep isn’t set to a fixed 16.667ms. Instead, I use a high-resolution timer to measure how much time has really elapsed since last frame, and I advance the simulation by that much. The problem is that the timer doesn’t always return the exact same amount. It’s not super-precise, and it can be slightly affected by other things going on in the device. It won’t be off by more than 1/10th of a ms, but that’s enough to cause different results and start diverging the simulation.
- Mike Ash explains [how NSZombies work](http://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html), our favorite debugging instrument for finding memory management bugs. If you suspect some serious behind-the-scenes magic, it is surprisingly simple and straightforward (a feeling I often get when looking under the hood of Objective-C and the runtime).
- Martin Pilkington dives deep into the Objective-C Runtime: [Dynamic Tips & Tricks with Objective-C](http://pilky.me/view/21).
- Another great tutorial by Ray Wenderlich: [How to make a space shooter game](http://www.raywenderlich.com/3611/how-to-make-a-space-shooter-iphone-game) with Cocos2D.
- Microsoft introduced a [Bing Maps Control for iOS](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=6e01a102-49ed-409e-b384-0b67521fb612). The API is very similar to `MKMapView`.
- Kelly Sommers picks up a topic that I am sure many of us have thought about: [Continuous Client: Our multi-device dream but how do we build it?](http://kellabyte.com/2011/05/26/continuous-client-our-multi-device-dream-but-how-do-we-build-it/) When we all have multiple computer-like devices, how can we transfer one device’s state to another when we switch devices? Kelly proposes that we design our apps with the Continuous Client concept in mind to make it easy to actually implement it when the time has come (did anybody say iCloud?). Specifically, think about using `NSNotification` to signal UI interactions in your app:

  > If you are an iOS deveoper are you using NSNotificationCenter? If you are using these mechanisms to publish and subscribe UI interactions you are well on your way already. The more your software is designed around messages the easier your system can be automated without special code required because your system is natively written to handle these messages.
- In [Regarding Objective-C & Copland 2010](http://kickingbear.com/blog/archives/168) Guy English talks about John Siracusa’s articles and podcast about the [future and longevity of Objective-C and Cocoa](https://oleb.net/blog/2011/04/john-siracusa-a-dark-age-of-objective-c/). Guy does not share John’s prediction that to stay competitive, Apple will need to replace Objective-C with a newer, higher-abstraction language in the coming five to ten years; he makes some very good points that Objective-C is actually very well positioned in the competitive landscape of programming languages. I still tend to side with John Siracusa here, though not necessarily with his argument that automatic memory management is the key issue. In my opinion, the downsides of Objective-C’s C heritage show in more aspects than just memory management, from syntax to complexity (why again do app developers have to deal with countless different types for integer numbers?).

**Update July 3, 2011:** Tim Wood of the Omni Group compared the [performance of different techniques to create a drop shadow on iOS](http://www.omnigroup.com/blog/entry/ipad_drop_shadow_performance_test/). Great post.

# Design

- Marco Arment is [very annoyed by the increasingly common “Rate this App” dialogs](http://www.marco.org/2011/05/05/apps-prompting-for-reviews) and he doubts they actually help:

  > More reviews and higher ratings can drive sales, but a highly satisfied customerbase drives a lot more. When someone has spent $4.99 for my app, they’re entitled to a hassle-free experience. I wouldn’t feel right shoving a dialog box in their face a few days later asking for a time-consuming favor

  Contrast this with [Kobo’s experience when they added such a dialog to their app](https://quatermain.tumblr.com/post/5545497083/lessthanuthink-a-snapshot-of-current-reviews):

  > I was fairly sceptical about the reception the new ‘rate this app’ dialog in the Kobo app would have, but it appears to be working nicely. For about the first time ever, people who like the app are actually giving us reviews, with the result that it’s now among the highest-rated apps in the Books section of the iTunes store.
- Great talk by Mike Lee on [Making Apps That Don’t Suck](http://www.infoq.com/presentations/Making-Apps-That-Dont-Suck). I believe this is more or less the same talk Mike gave at NSConference 2011.
- Greg Cox on a new trend in Mac app design and why he does not like it: [Column-based list views are so passé](http://expletiveinserted.com/2011/05/28/column-based-list-views-are-so-passe/).
- Jean-Francois Martin highlights [the design approach of the Twitter app, Reeder and Remeber the Milk on the iPad](http://www.buildingiphoneapps.com/2011/05/beyond-uisplitviewcontroller.html). These apps were not satisfied with Apple’s flawed `UISplitViewController` design and created better alternatives for displaying hierarchical information.

# App Store

- Users who got your app through a promo code are [no longer able to leave a rating or review](http://www.macrumors.com/2011/05/03/apple-no-longer-accepting-app-store-reviews-for-redeemed-promo-codes/) for it on the App Store.

  > According to Apple representatives, the change has been made in order to help prevent developers from gaming the ratings and reviews system by using an entire batch of promo codes to boost their profile.
- In a post titled [Top Grossest Apps](https://mrgan.tumblr.com/post/5398236151/top-grossest-apps), Neven Mrgan talks about the meaninglessness of the Top Grossing list in the App Store since Apple includes in-app purchases in that list:

  > Then Apple added in-app purchases and decided to include those when calculating apps’ earnings for the Top Grossing list. The result? The list is completely dominated by fake-money compulsion engines.
- There are now more than 500,000 apps in the iOS App Store. 148apps, Chomp and Chilingo created a [huge infographic about the history and current state of the App Store](http://c3316209.r9.cf0.rackcdn.com/500kAppsInfographic.png): the 500,000 apps have been created by 85,000 developers. Close to 40% of all apps are free. While the average price of a paid app is $3.64 (note that averages probably have little meaning in the distribution of App Store apps), almost half of all paid apps sell for $0.99, and another 20% are $1.99. The median price of a paid app is $1.99. Interestingly, the average price level has been more or less constant since late 2008. With 15% of all apps, games are the single biggest category (closely followed by ebooks), but the percentage of games was even higher (24%) when the App Store launched.

# Competition

- Jean-Louis Gassée points out [the flaws in comparing the iPhone vs. Android situation today with the Mac vs. PC “battle”](http://www.mondaynote.com/2011/05/01/carnival-barker-edition-show-me-your-ios-licensing-certificate/) and predicting on that basis that the iPhone will “lose” (whatever that means) to Android.
- One reason why developers stick to iOS: [The App Store is projected to account for more than 75% of the market in 2011](http://www.isuppli.com/media-research/news/pages/revenue-for-major-mobile-app-stores-to-rise-77-7-percent-in-2011.aspx).
- Lukas Mathis gives a [very good and detailed overview of Windows Phone 7](http://ignorethecode.net/blog/2011/05/31/windows_phone_7/) that really makes me want to try it out myself. WP7’s clean and modern UI makes parts of iOS look kind of old. As Lukas puts it:

  > After looking at the clean, ascetic visual language of WP7 for such a long time, iOS suddenly seems garish, overdone, and kind of ugly.

  Related, [Microsoft shows off Mango, the next version of Windows Phone](https://www.youtube.com/watch?v=OP30F3ZxTmw). Looks good.

# Other

- Aldo Cortesi points out [the privacy issues that arise from the fact that every iOS device has a unique ID and that Apple gives apps free access to it](http://corte.si/posts/security/openfeint-udid-deanonymization/), encouraging developers to use the UDID for tracking purposes. Cross-app libraries such as ad or game networks can use the UDID to track users across apps. OpenFeint even links the UDID to sometimes private user information in a public API call.
- Chopper creator David Frampton answers a question: [Is Being an Indie all Fun and Games?](http://majicjungle.com/blog/496/)

  > There are a few negatives, but they are vastly out-weighed by the positives.
- Nice article by Matthijs Hollemans to give to the next potential client who thinks you are too expensive: [Developing Software is Expensive Because It is Hard](http://www.hollance.com/2011/05/developing-software-is-expensive-because-it-is-hard/).
