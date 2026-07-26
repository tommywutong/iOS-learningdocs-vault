---
title: 'iOS and Mac Development Link Roundup: December 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/01/ios-and-mac-development-link-roundup-december-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a13c4909de8b67f8'
translated: false
---

> 原文：[iOS and Mac Development Link Roundup: December 2011](https://oleb.net/blog/2012/01/ios-and-mac-development-link-roundup-december-2011/)　·　Ole Begemann

# iOS and Mac Development Link Roundup: December 2011

Here is my summary of the past month in links.

# Carrier IQ

_The_ story at the beginning of the month was the Carrier IQ software that [Trevor Eckhart found on his Android phone](http://www.wired.com/threatlevel/2011/11/secret-software-logging-video/), logging a lot of seemingly privacy-related activity. Grant Paul quickly found out that [Carrier IQ also is on iOS](http://blog.chpwn.com/post/13572216737), although Apple was quick to affirm that it has never used the software for anything that’s not covered by their privacy policy and only collected usage data if users explicitly opted in.

As the days went by, what seemed like a huge scandal at first turned out to have been blown out of proportion. Still, some phone carriers are to be blamed for using Carrier IQ’s software to track things like [the applications used or what URLs are visited by a user](http://vulnfactory.org/blog/2011/12/05/carrieriq-the-real-story/) (information which, admittely, they know anyway).

# Programming

## Android Graphics Architecture vs. iOS

There has been an interesting discussion about the shortcomings (or not) of Android’s graphics architecture vs. iOS. It’s hard to follow the original discussion now because many of the posts have been edited but let’s recap:

Dianne Hackborn, Android engineer at Google, set out to correct some assumptions about Android’s internals in a post titles [How about some Android graphics true facts?](https://plus.google.com/105051985738280261832/posts/2FXDCz8x93s). Andrew Munn, former intern on the Android team, followed up with his (misinformed) post [The Reason Android is Laggy](https://plus.google.com/100838276097451809262/posts/VDkV9XaJRGS), claiming the main advantage of iOS’s over Android’s architecture was that iOS used  a dedicated UI thread with real-time priority.

In [another follow-up post](https://plus.google.com/105051985738280261832/posts/XAZ4CeVP6DC), Dianne Hackborn rejected this claim, instead naming the security model and the design of certain APIs as reasons for Android’s past performance problems. Several people also pointed out flaws in Andrew’s description of how iOS actually works (see [Andrew Munn’s updated post](https://plus.google.com/100838276097451809262/posts/VDkV9XaJRGS)). Bob Lee’s post [The truth about Android & iOS UI performance](http://blog.crazybob.org/2011/12/truth-about-android-ios-ui-performance.html) on the topic is worth reading, too.

In conclusion, it’s probably fair to say that with Android 4.0, the technical differences between iOS and Android in terms of graphics rendering are pretty small. I really like Becca Royal-Gordon’s take on the topic, quoted by Andrew Munn:

> All that stuff you noticed—the way images aren’t drawn into lists while you’re scrolling, the way WebKit rendering stops when the system is tracking a touch—isn’t inherently built-in by a mechanism that pauses the world when a finger is on the screen.* It’s deliberate behavior painstakingly implemented by the developer of each individual app.
> 
> This is not a technical difference; it’s a cultural difference. Good iOS developers don’t ship software until it runs at something near 60 fps while scrolling and tracks touches almost perfectly; good Android developers do.

## [Disassembling the Assembly, Part 3: ARM edition](http://www.mikeash.com/pyblog/friday-qa-2011-12-30-disassembling-the-assembly-part-3-arm-edition.html)

Gwynne Raskind gives a good introduction to reading ARM assembly language. This can be useful for intense iOS debugging sessions or if you just want to better understand your compiler. Don’t miss [part 1](http://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html) and [part 2](http://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html) of the series covering x86_64 assembly.

## [QuadCurveMenu](https://github.com/levey/QuadCurveMenu)

Zhu Levey created an open-source implementation of the animated fly-out menu made popular this month by the redesigned Path app. While I hope we won’t see this kind of menu in every second app in the future, the code can help illustrate some advanced Core Animation techniques.

## [Attaching an info panel to a UIScrollViewIndicator like in the Path 2 app](http://blog.madefm.com/post/13817640556/ios-devcorner-attaching-an-info-panel-to-a)

Another UI gem in the new Path app is the floating clock that scrolls and animates with the main scroll view to indicate the position of the timeline. Florian Mielke shows how to mimic this behavior in your own view controller.

**Update Janurary 1, 2012:** [TimeScroller](https://github.com/andrewroycarter/TimeScroller) by Andrew Roy Carter is another take on this. Andrew’s solution goes a little further and actually reproduces the look of the control in the Path app including the clock.

## [A Dynamic Siri](http://kickingbear.com/blog/archives/264)

Guy English on the possibility of Apple providing developer access to Siri in the future.

> I predict that a Siri API is further off than you might think. The integration of services into Siri appears to be on a very case by case basis and even an internal app required special consideration. … Apple doesn’t appear to have an internal API for Siri yet, and it’s my bet that they’re a year or so away from it.

## [Economies of Scalar](http://subjectiveobserver.wordpress.com/2011/12/04/economies-of-scalar/)

Someone naming herself Subjective Observer points out a very useful new Core Data option in iOS 5 and OS X Lion. The Core Data editor now lets you “use scalar properties for primitive data types” instead of `NSNumber`, generating accessors based on scalar data types for numeric attributes. That is a great and largely undocumented addition! She also shows how to make use of this new feature while maintaining compatibility with older OS versions.

## [Nib Segregation](http://joshua.nozzi.name/2011/11/nib-segregation/)

It’s common Cocoa wisdom and the rule to put each window into its own NIB file. Joshua Nozzi argues that it’s not always beneficial, though. Blind adherence to generalizations will get you in trouble.

## [VendorKit](http://vendorkit.com/)

VendorForge and Vendor, two of the Cocoa package managers I mentioned in [last month’s link roundup](https://oleb.net/blog/2011/11/ios-and-mac-development-link-roundup-november-2011/), have merged to form VendorKit. I hope to see more of this. One package manager to rule them all! (Provided it’s a good one.)

## [Constant Confusion](https://aussiebloke.blogspot.com/2011/12/constant-confusion.html)

Stuart Carnie clears up a syntax rule in C that always eluded me before: where to put the `const` keyword in a complex declaration? The answer is, of course, it depends on whether you want a constant pointer to a mutable value or a mutable pointer to a constant value or a constant pointer to a constant value. For all these cases, Stuart comes up with an easy-to-remember rule:

> Always write `const` to the right and read the declaration from right to left.

Simple as that.

## [JSON Libraries for iOS Comparison](http://www.bonto.ch/blog/2011/12/08/json-libraries-for-ios-comparison-updated/)

“Junior B.” compared the performance of various open-source JSON libraries to Apple’s new built-in JSON parser in Cocoa. Result: on iOS, JSONKit is up to ~30% faster than Apple’s `NSJSONSerialization`. SBJSON and TouchJSON are much slower than both.

## [CMPopTipView](https://github.com/chrismiles/CMPopTipView)

CMPopTipView by Chris Miles is a view component that can display a UIPopover-like “bubble”, containing a text message, pointing at a specified button or view. Looks good for help texts.

## [PNG compression and iOS apps](http://bjango.com/articles/pngcompression/)

Mark Edwards analyzes the benefits of trying to optimize PNG images for your apps.

> I’m going to come straight out and say it—if you’re spending any effort compressing or optimising your PNG images for iOS app development, you’re wasting your time.

## [UIStoryboard Issues](http://toxicsoftware.com/uistoryboard-issues/)

Great post by Jonathan Wight on the current shortcomings of Storyboarding in iOS 5 apps. Jonathan’s verdict is that, while Storyboarding is a promising concept, it isn’t yet mature enough to be used in a complex app. I was particularly struck by the section titled “Misuse sender field”. It really seems Apple has forgotten to provide an essential API here.

## [retainCount is useless](http://www.friday.com/bbum/2011/12/18/retaincount-is-useless/)

If you ever find yourself logging retain counts while trying to debug a memory management problem, remember Bill Bumgarner’s post and stop what you’re doing immediately.

## [Trying Out Multisampling On iOS](http://gamesfromwithin.com/trying-out-multisampling-on-ios)

Noel Llopis investigates the benefits and performance drawbacks of using OpenGL multisampling in iOS. In his testing with the Flower Garden app, the performance impact varied greatly by device: almost none on the iPhone 3GS and iPad 2, huge impact on the iPad 1 and iPhone 4 (whose GPU is less capable relative to the amount of pixels they have to handle).

## [AQSocket](https://github.com/AlanQuatermain/AQSocket)

Jim Dovey wrote a simple socket class that illustrates how to work with Grand Central Dispatch’s dispatch sources and dispatch I/O channels. Both are GCD features that are usually not addressed in your typical GCD tutorial so Jim’s code should be very useful if you want to learn more about the topic.

## [F3BarGauge](https://github.com/ChiefPilot/F3BarGauge)

F3BarGauge by Brad Benson is a customizable iOS control to display bar gauges. Useful for your next audio mixer/visualizer app.

## [Zucchini](http://www.zucchiniframework.org/)

Zucchini is a new visual iOS testing framework, inspired by the [Cucumber framework](http://cukes.info/), which is very popular in the Ruby community. You write your tests in CoffeeScript, which Zucchini then compiles down to Apple’s UIAutomation Javascript syntax. Jake Marsh already [blogged about Zucchini](http://deallocatedobjects.com/posts/zucchini-visual-ios-testing-written-in-coffeescript). Looks promising.

## [Building a Universal Framework for iOS](http://spin.atomicobject.com/2011/12/13/building-a-universal-framework-for-ios/)

Justin DeWind wrote an up-to-date tutorial on building frameworks in Xcode that include multiple architectures such as armv6, armv7, and i386. This is especially useful for developers of open-source components. Or you can build your own frameworks if you want to easily mix ARC and non-ARC code without the hassle of specifying per-file compiler flags.

## [Static Code Analysis](http://altdevblogaday.com/2011/12/24/static-code-analysis/)

John Carmack talks about the huge benefits he got from using static code analysis in his projects. The discussion of particular tools is C/C++-centric and thus not directly applicable to Objective-C code but his general findings are interesting:

> The most important thing I have done as a programmer in recent years is to aggressively pursue static code analysis. Even more valuable than the hundreds of serious bugs I have prevented with it is the change in mindset about the way I view software reliability and code quality. … I feel the success that we have had with code analysis has been clear enough that I will say plainly it is irresponsible to not use it.

Lesson for Cocoa developers: at least use the Clang Static Analyzer that’s built into Xcode regularly.

## [Siri Authentication](http://blog.chpwn.com/post/14612320117)

Grant Paul reverse-engineered how Siri authentication works, thereby ensuring that it only runs on an iPhone 4S (or for hacks you need an iPhone 4S device token). This is his overview.

## [iCloud Demystified](http://gamesfromwithin.com/icloud-demystified)

Noel Llopis gives a good tutorial (including a demo project) how to sync files with iCloud in the simplest way possible (without using `UIDocument`).

## [Suppressing Xcode Warnings On A Per File Basis](http://blog.bluelightninglabs.com/2011/12/suppressing-xcode-warnings-on-a-per-file-basis/)

Nice little tip by Shane Crawford. Especially useful if you use some open source library whose author did not care to fix all compiler warnings.

# Design

## [Inspiration vs. Imitation](http://www.jessicahische.is/obsessedwiththeinternet/andbeingresponsivelyinspired/inspiration-vs-imitation-2)

Great post by Jessica Hische on the fine line between being inspired by others and using this inspiration to create something original and blatantly copying others’ creations.

## [What Goes into the Sausage – The Creation of an Icon](http://blackpixel.com/blog/1458/what-goes-into-the-sausage-the-creation-of-an-icon/)

Michael Shephard from Black Pixel about the iterative and non-linear nature of the design process. Nice insight.

## [On Magazines and the iPad](http://carpeaqua.com/2011/12/04/on-magazines-and-the-ipad/)

Justin Williams shows what happens when media companies create apps for the sake of having an app rather than to create a better user experience.

> I’m convinced that the people who actually write for magazines, edit them and publish them have never actually tried using their iPad versions for more than a few moments. If they actually did try to use their publication’s app as the actual means to read each issue, things would have to improve. Right? RIGHT?!

## [UI Parade](http://www.uiparade.com/)

UI Parade is another one of the sites that collect examples of outstanding UI design. I mentioned a number of these over the past months in my blog posts but this one seems particularly well edited.

## [UX design experiments for a Number 1 mobile app](http://discovr.info/2011/12/ux-design-experiments-for-a-number-1-mobile-app/)

David McKinney illustrates different approaches how to integrate help into your app’s UI. I like the integrated approach they settled on very much.

## The Flipboard for iPhone design process

After Flipboard for the iPhone came out earlier this month, members of the design team tweeted some pictures showing the many, many iterations they did for this one app’s design. I love how the photos illustrate the incredible amount of work that went into it.

![Flipboard for iPhone Design Prototype 1](http://distilleryimage1.s3.amazonaws.com/e7432e64212511e19896123138142014_7.jpg)

![Flipboard for iPhone Design Prototype 2](http://distilleryimage8.s3.amazonaws.com/7724c43c21d711e180c9123138016265_7.jpg)

![Flipboard for iPhone Design Prototype 3](http://distilleryimage11.s3.amazonaws.com/eac8d40421d311e180c9123138016265_7.jpg)

## [UX Critique of Path 2](http://startingup.me/post/13738882378/path-2)

Brenden Mulligan took a very detailed look at the new Path app from a design and user experience point of view. Very insightful and spot-on.

## [Texture](http://carpeaqua.com/2011/12/22/texture/)

Justin Williams on the importance of texture in the iOS UI. Justin gives examples of some new apps that to him feel out of place on iOS because their design is based on solid colors without texture, which seems more fitting in Android and Windows Phone environments. He points out the importance of designing especially for the target platform:

> Mobile is young enough that we’ve got three vibrant platforms that offer uniquely identifiable experiences jockeying for position. If your goal is to reach all of those customers, do it with respect and taste. Build something tailored specifically for them, not something that is just “good enough” for all three.

## [Beth on Brushes](https://vimeo.com/33991213)

Fraser Speirs posted a video that shows how competently his 4-year-old daughter uses the Brushes app on the iPad to paint a picture. Again and again, it’s amazing to see how much more intuitive these post-PC devices are compared to a classical mouse-driven GUI.

# App Store

## [How to to climb in the App Store, Part II](https://plus.google.com/115711522874757126523/posts/BBn6UjDiDLU)

Oliver Reichenstein continued to analyze and publish iA’s pricing experiments with their app, iA Writer. The takeaway from this for developers seems to be: trying out different price points is fine and all but in the end, the quality and uniqueness of your app will be a much bigger sales driver:

> To increase sales: Don’t imitate. You might get some crumbs from some table but ultimately, you’ll help the original by doing so. Innovate. Think different, be different. Take maximum care for details, even if it’s a hassle. Read all feedback and don’t get irritated by feature requests and focus on the next big step.

## [And now a reminder of how tough the App Store slog really is](http://www.splatf.com/2011/12/path-rank/)

Taking the new Path app as an example, Dan Frommer points out how hard it is to be successful on the App Store these days, even if you made a great product and got as much press as those guys did. A few days later, Dan followed up with [a post showing that in Path’s case](http://www.splatf.com/2011/12/path-top-25/) at least, the app finally made it into the top 25. So it may be hard, but it’s definitely not impossible.

## [Apple’s Mac App Store Downloads Top 100 Million](http://www.apple.com/pr/library/2011/12/12Apples-Mac-App-Store-Downloads-Top-100-Million.html)

In a press release, Apple announced some numbers for the Mac App Store now that it is almost one year old. 100 million app downloads in less than a year sure sound impressive until you compare it to the size of the iOS App Store, which registers about 1 _billion_ downloads _a month_.

In other words, the iOS App Store is about 50-100 times bigger than the Mac App Store in terms of downloads. Interestingly, the relation is about the same when you count the total number of available apps (500,000 for iOS vs. less than 10,000 on the Mac App Store). So arguably, because it’s so much easier to get your share of visibility on the Mac App Store, your chances of making money could be roughly equal on both stores, especially since Mac apps tend to be priced higher.

## [A look at the Mac App Store, 100 million downloads later](http://www.splatf.com/2011/12/macappstore-100million/)

Dan Frommer also takes a look at the numbers in the Mac App Store. According to his statistics, only about 18 apps are added to the Mac App Store each day. Surprising.

## [App Developers Bet on iOS over Android this Holiday Season](http://blog.flurry.com/bid/79061/App-Developers-Bet-on-iOS-over-Android-this-Holiday-Season)

According to Flurry (who have unique data on many mobile app stats thanks to their analytics software), app developers still favor iOS over Android by a wide margin despite Android’s tremendous growth in market share. The main reason seems to be that the App Store is where the money is.

## [Distimo Releases Full Year 2011 Publication](http://www.distimo.com/blog/2011_12_distimo-releases-full-year-2011-publication/)

Research firm Distimo published an updated report on the mobile app store field in 2011. Key findings:

1. The iOS App Store generates about four times the revenue that the Android Market makes.
2. In-app purchases and freemium business models have an increasing share of the total revenue.
3. The app market in China is growing fast.

## [Free-to-Play Pioneer NimbleBit Says to Put Fun and User Experience First, Not Monetization](http://www.insidemobileapps.com/2011/12/14/free-to-play-pioneer-nimblebit-say-to-put-fun-and-user-experience-first-not-monetization/)

Good interview by Kathleen De Vere with David and Ian Marsh, the twin brothers behind Tiny Tower. They talk about monetization strategies on the App Store and the increasing role of “freemium” business models. Surprisingly to me, 30% of the revenue they make with Tiny Tower comes from selling $30 in-app purchases, even though these items only make up 4% of all their in-app purchases. Goes to show that it pays off to give your most loyal users the chance to give you more than $0.99.

# Community

## [Latest Version](http://mattgemmell.com/2011/12/05/latest-version/)

Matt Gemmell makes the tongue-in-cheek argument that it is okay to only support the latest OS version. And I actually agree (up to a point).

## [The Golden Age of the Developer](http://www.kernelmag.com/scene/2011/12/developers-developers-developers/)

David Haywood Smith from The Kernel says there has never been a better time to be a developer. There are countless resources and opportunities available to us. The only thiing we have to do is consume them. But at the same time, David reminds us that we all have the responsibility to give something back to this awesome community. Everybody should think about how they can contribute. And to all those who already do contribute, do not sit back:

> The big challenge is leading. It’s not as scary as it sounds. It’s really just an extension of contributing. If you make a significant contribution then you automatically become a leader. … I encourage you to start thinking about how to move up the ladder. Whatever kind of developer you are, you’ll find it pays dividends.

## [Open Source Code](http://mattgemmell.com/2011/12/19/open-source-code/)

On the same topic, Matt Gemmell has some very useful tips on how to publish some of your code in open-source form. By following Matt’s advice, you increase the chances that your open-source project will actually be noticed significantly. Even if your code is absolutely amazing, almost no one will look at it if you don’t package it nicely and make it easy for others to use.

## [From Idea to Market: How We Built Gradient](http://net.tutsplus.com/articles/general/from-idea-to-market-how-we-built-gradient/)

Nicola Armellini from Jumpzero talks about the development process of their Mac app, Gradient. I love how he stresses to start out with a simple idea that solves a real problem and the importance of prototyping and showing what you do to possible influencers far before it’s done.

# Competition

## [10 Billion Android Market downloads and counting](https://googleblog.blogspot.com/2011/12/10-billion-android-market-downloads-and.html)

Google reported on their blog that the Android Market has reached 10 billion app downloads. The current growth rate of the Market is 1 billion downloads per month, similar to the current growth of the iOS App Store.

## [Standing Up For Android](http://shiftyjelly.wordpress.com/2011/12/08/standing-up-for-android/)

The guys from Shifty Jelly make quite a convincing point for iOS developers to also look at the opportunities of the Android community.

> In many ways it’s [the Android Market] a better place to be than iOS, since so many developers are ignoring it, and yet there is a massive install base waiting to give you their money.

I’m sure there are many Android developers who would agree. So why all the controversy? Let everyone decide on their own which platform they want to target (first). I am sure some will follow [Eric Schmidt’s prediction](http://julianyap.com/2011/12/08/What-Eric-Schmidt-actually-said.html) and others (probably most, at least in the next 6 months) will not.

## [Microsoft to drop Desktop App from Windows 8 ARM tablets?](https://www.zdnet.com/blog/microsoft/microsoft-to-drop-desktop-app-from-windows-8-arm-tablets/11325)

Mary Jo Foley writes that Microsoft may make a 180 degree turn and actually make Windows 8 tablets Metro only, not bringing over the traditional Windows desktop. I think that would be a great move for Microsoft.

## [Previewing the Windows Store](http://blogs.msdn.com/b/windowsstore/archive/2011/12/06/announcing-the-new-windows-store.aspx)

Antoine Leblond from Microsoft gives developers a preview of the upcoming app store for Windows 8. Their feature set sounds great:

> We have full platform support for free apps, trials (both time-based and feature-based trials) and paid apps, including in-app purchase. And we have sales analytics that will help you target customers more effectively.

In addition, developers will get an 80% revenue share (instead of the usual 70%) if their app is successful enough to make it over $25,000 in total revenue. Let’s hope that more competition in the app store space will give Apple the incentive to further improve their offerings.

## [HP to Contribute webOS to Open Source](http://www.hp.com/hpinfo/newsroom/press/2011/111209xa.html)

Press release by HP. Will it make a difference? Will other major players like Facebook or Amazon now adopt webOS for their own devices? In an interview with Joshua Topolsky for The Verge, HP CEO Meg Whitman and board member Marc Andreessen at least confirmed that HP has plans to make new tablets running webOS, but what I can’t tell you is whether that will be in 2012 or not.

## [Twenty four hours of Lumia](http://www.alasdairmonk.com/journal/twenty-four-hours-of-lumia/)

Alasdair Monk’s is one of a number of very positive reviews of the Lumia 800, Nokia first device running Windows Phone 7.5. The phone is stunning and the software looks great too. Looking at the market reaction, it still seems to have come too late.

## [Goodbye, Nokia Lumia 800: £400 and one month on, it didn’t work out](http://www.guardian.co.uk/technology/blog/2011/dec/30/nokia-lumia-800-goodbye)

Matthew Baxter-Reynolds just published a rather negative review of his Lumia 800 experience over the last month, citing many minor flaws both in the built-in software and in third-party apps.

> What’s wrong is the niggles. Windows Phone is a good operating system. But it’s not a great operating system. … It’s the niggles that’s stopped me from developing a deeper relationship with the device that turns it into a ubiquitous tool, as opposed to “just a phone”.

# Apple and Steve Jobs

## [Apple’s Terrific And Tumultuous 2011](http://techcrunch.com/2011/12/30/apple-2011/)

MG Siegler summarizes Apple’s 2011 for Techcrunch in a long list of links. Very useful post for reference if you want to find a particular article again.

## [10 things we learned about Apple this year](http://www.splatf.com/2011/12/apple-2011-lessons/)

Dan Frommer highlights some key points how Apple works and acts. Realizing these traits will probably make it much easier to tell if the next random Apple rumor has any value or not. Most important lesson for developers: The iPad really is special. If you did not know that already.

## [Apple Made A Deal With The Devil (No, Worse: A Patent Troll)](http://techcrunch.com/2011/12/09/apple-made-a-deal-with-the-devil-no-worse-a-patent-troll/)

Apple has been extremely busy recently suing its competitors (and being sued by them) for patent infringement, copycat design, etc. I think it’s fair to say that it has become impossible to say who’s right and who’s wrong overall. Not so in this particular case: Jason Kincaid seems to have uncovered that Apple may have cooperated with a patent troll. To quote Jason, it’s hard to see Apple in a positive light here.

## [Steve Jobs by Walter Isaacson: A Review](http://blog.thomasqbrady.com/post/13639200852/steve-jobs-by-walter-isaacson-a-review)

Thomas Q. Brady with a well-written and well-founded critique of the Jobs biography. Brady makes many of the same points I already [heard from John Siracusa](http://5by5.tv/hypercritical/42), so this is a good article to read if you don’t listen to podcasts.

## [Apple Submits Updated Campus 2 Plans to Cupertino, Reveals Stunning Renderings](http://www.iphoneincanada.ca/iphone-news/apple-submits-updated-campus-2-plans-to-cupertino-reveals-stunning-renderings/)

Gary Ng’s article includes links to many new renderings and plans of Apple’s stunning plans for the new corporate campus.

## [The Real Story Behind Apple’s “Think Different” Campaign](http://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/)

In the Steve Jobs biography, Walter Isaacson suggests that Steve Jobs himself wrote much of the “Here’s to the Crazy Ones” text for Apple’s famous _Think Different_ campaign. In this interesting article for Forbes, Rob Siltanen, member of the original advertising team, tells a different story. Obviously, this is not development-related at all, but it is a good read.
