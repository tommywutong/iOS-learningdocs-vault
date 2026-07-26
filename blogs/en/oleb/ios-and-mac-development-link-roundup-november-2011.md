---
title: 'iOS and Mac Development Link Roundup: November 2011'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/11/ios-and-mac-development-link-roundup-november-2011/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2d7e932d0ea690ad'
translated: false
---

> 原文：[iOS and Mac Development Link Roundup: November 2011](https://oleb.net/blog/2011/11/ios-and-mac-development-link-roundup-november-2011/)　·　Ole Begemann

# iOS and Mac Development Link Roundup: November 2011

I skipped my customary monthly link roundups in September and October simply because I did not have the time to compile them. Not only did the composition of the interesting links at the end of the month take up an increasing amount of time (which I would be fine with), but the fact that I felt I had to stay up to date with my Twitter timeline every single day in order not to miss anything made this impossible.

Perhaps not surprisingly, the amount of positive feedback I got the roundups increased tremendously once I had stopped doing them. Thanks to everybody who told me they liked these posts. The feedback encouraged me to make another attempt at continuing the series, though note that I am not making any promises. It is quite possible that I abandon the whole thing again as soon as next month.

# iOS 5.0.1

Apple [released iOS 5.0.1](http://support.apple.com/kb/HT5052). The update contains, among other small improvements, a way for developers to specify files that should remain on device, even in low storage situations. iOS 5.0.1 thereby fixes [the “Cleaning” issue faced by many offline content apps, illustrated by Marco Arment](http://www.marco.org/2011/10/13/ios5-caches-cleaning).

To prevent your offline files from both being backed up and deleted by the system, put them anywhere in your Documents or Library folder except `/Library/Caches` and [set an extended attribute to mark them as “should not back up”](http://developer.apple.com/library/ios/#qa/qa1719/_index.html).

Thanks to Apple for providing such a quick fix. It shows that Apple is indeed willing to make changes to their policies when they realize the consequences for consumers are bad.

# Programming

## Siri

The guys from Applidium [reverse-engineered Siri’s protocol](http://applidium.com/en/news/cracking_siri/). Basically, Siri uses binary plists over a non-standard-conforming HTTPS to talk with the server. It seems to require an iPhone 4S device ID to authenticate against the server. The binary plists contain raw audio data using the Speex audio codec. Applidium also published a [collection of tool](https://github.com/applidium/Cracking-Siri).

Using these as a basis, someone named Pete created [SiriProxy](https://github.com/plamoni/SiriProxy), a proxy server that allows you to inject custom handlers for certain keywords into Siri’s vocabular. [Pete’s demo video](https://www.youtube.com/watch?v=AN6wy0keQqo) is worth watching.

In the meantime, several SiriProxy plugins have been published or demoed, such as [one for Spotify](https://github.com/simonmaddox/SiriProxy/blob/fab7bb1798a40f2262f1c8a4970418b36f7825de/plugins/spotify/spotify.rb) from Simon Maddox.

## Components and Libraries

- [MKNetworkKit](http://blog.mugunthkumar.com/products/ios-framework-introducing-mknetworkkit/) by Mugunth Kumar is an interesting new iOS networking library, inspired by both ASIHTTPRequest and AFNetworking.
- [SVGKit](https://github.com/mattrajca/SVGKit) by Matt Rajca is a library for rendering SVG files as Core Animation layers. All shapes are represented by instances of the `CAShapeLayer` class and are animatable.
- [GMGridView](https://github.com/gmoledina/GMGridView) is a promising new grid view component for iOS, written by Gulam Moledina. Supports horizontal and vertical layouts, reordering via drag and drop, and the pinch-to-fullscreen gesture. Requires iOS 5.
- Sam Vermette published [SVStatusHUD](http://samvermette.com/309), a replica of Apple’s HUD overlays in iOS. I especially like how Sam prescribes the situations in which you should use the component to stay in accordance with Apple’s usage:

  > It should only be used in response to hardware or other important notifications (for instance when an accessory is detected by your app).
- Matthijs Hollemans wrote [MHTabBarController](http://www.hollance.com/2011/11/mhtabbarcontroller-a-custom-tab-bar-for-ios-5-using-the-new-container-apis/), a custom tab bar controller that illustrates the new view controller container APIs in iOS 5.

## Tutorials and How Tos

- Matthijs Hollemans has another nice trick up his sleeve: combine two JPEG images (the actual picture and a separate alpha mask) into [a single JPEG to make it transparent](http://www.hollance.com/2011/11/transparent-jpeg-images/). Great for the rare case when a PNG file would be too large. Matthijs provides a simple `UIImage` category that lets you do this.
- The folks around Ray Wenderlich published [multiple tutorials about some of the new iOS 5 features](http://www.raywenderlich.com/tutorials), such as Storyboards, ARC, and iCloud.
- Keith Harrison shows [how to replicate the sliding master view of Mail.app](https://useyourloaf.com/blog/2011/11/16/mail-app-style-split-view-controller-with-a-sliding-master-v.html) in iOS 5. In a [follow-up post](https://useyourloaf.com/blog/2011/11/24/creating-gesture-recognizers-with-interface-builder.html), Keith illustrates how to create the necessary gesture recognizers directly in Interface Builder.

## Miscellaneous

- The GNUstep project has release [version 1.6 of the GNUstep Objective-C Runtime](http://lists.gnu.org/archive/html/discuss-gnustep/2011-11/msg00113.html), bringing it to a level with iOS 5.0 and OS X 10.7. The GNUstep runtime also includes an interesting feature: Support for prototype-style object orientation, Javascript-style.
- The LLVM team has started a series of posts outlining major changes in LLVM 3.0. So far, they have published two articles on [the type system rewrite](http://blog.llvm.org/2011/11/llvm-30-type-system-rewrite.html) and [exception handling redesign](http://blog.llvm.org/2011/11/llvm-30-exception-handling-redesign.html). This is pretty in-depth stuff that you probably don’t need to know about but it never hurts to understand how the compiler works.
- Martin Pilkington continued his series of Xcode reviews, [this time with Xcode 4.2](http://pilky.me/view/28).
- Nathan de Vries discovered [how to enable WebGL](http://atnan.com/blog/2011/11/03/enabling-and-using-webgl-on-ios/?t=1320304062) (which is publicly only available for iAds since iOS 4.2) in `UIWebView` (using private APIs).
- An article titled [Parallel Implementations](http://altdevblogaday.com/2011/11/22/parallel-implementations/) by John Carmack:

  > If the task you are working on can be expressed as a pure function that simply processes input parameters into a return structure, it is easy to switch it out for different implementations. If it is a system that maintains internal state or has multiple entry points, you have to be a bit more careful about switching it in and out. If it is a gnarly mess with lots of internal callouts to other systems to maintain parallel state changes, then you have some cleanup to do before trying a parallel implementation.
- Daniel Jalkut in response to an [old Linus Torvalds e-mail](http://article.gmane.org/gmane.comp.version-control.git/57918) about his hatred of C++: [Objective-C is the Language](http://www.red-sweater.com/blog/2256/objective-c-is-the-language)
- [Chrashalytics is a new contender in the iOS Crash Reporting field](http://www.readwriteweb.com/mobile/2011/11/crashalytics-knows-why-your-io.php).
- [VendorForge](http://www.vendorforge.org/) by Keith Pitt is one of several third-party package managers for Cocoa developers that popped up over the last few months. Other similar projects include [CocoaPods](https://github.com/CocoaPods/CocoaPods), [kit](https://github.com/nkpart/kit) and [vendor](https://github.com/bazaarlabs/vendor). Since managing third-party libraries in Xcode is currently an absolute pain, this is an area where the Cocoa community could really benefit. My hope is that we end up with one great package manager that everybody can agree upon instead of an ugly mess of multiple different approaches.

# Design

- Wonderful article by Rob Beschizza at Boing Boing about the [fundamental differences in the design approach of Apple and its competitors](https://boingboing.net/2011/11/14/what-the-vaio-z-says-about-son.html), namely Sony:

  > Apple competitors are obsessed with copying Apple’s tastes without copying its central design habit, which is solving a problem and then refining the solution until the problem changes.
- Former Apple employee Bret Victor published [A Brief Rant on the Future of Interaction Design](http://worrydream.com/ABriefRantOnTheFutureOfInteractionDesign/), in which he encourages designers to not be satisfied with a future of Pictures Under Glass (the touchscreen). The future of interaction should be a dynamic medium that we can see, feel, and manipulate.

  David Barnard replies: [“Pictures Under Glass” is Revolutionary, Not Transitional](http://appcubby.com/blog/pictures-under-glass/):

  > My 2 year old son, Luke, is incredibly adept at using the iPad precisely because it doesn’t require tactile feedback to master, not in-spite of it.

  To Edward Tufte, Victor’s essay is [a celebration of the hand rather than about interface possibilities](http://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0003qM&topic_id=1).
- Andy Mangold [sees skeuomorphism as the opiate of the people](http://www.andymangold.com/skeuomorphism-the-opiate-of-the-people/) and argues that’s the underlying reason for the recent trend towards skeuomorphism in UI design:

  > But what hadn’t occurred to me is that it doesn’t matter if it actually does make it easier to use, all that matters is that it makes the average person _think_ it’s easier to use.
- Devin Coldewey: [In Defense of the Stylus](http://techcrunch.com/2011/11/11/in-defense-of-the-stylus/)
- [Mobile Design Pattern Gallery](http://mobiledesignpatterngallery.com/mobile-patterns.php) is another one of those sites that collect design patterns for mobile apps and examples of successful implementations. Looks good. Oliver Drobnik has compiled [a list of similar sites showcasing design patterns or outstanding app designs](http://www.cocoanetics.com/2011/11/steal-good-stuff-ios-design-pattern-collections/).

# Community

- Charlie Miller found a serious security hole in iOS [that allows apps to download code and execute it outside of their sandbox](http://www.forbes.com/sites/andygreenberg/2011/11/07/iphone-security-bug-lets-innocent-looking-apps-go-bad/). The result: Apple removed the offending demo app from the App Store and threw Charlie Miller out of the developer program [for 1 year](https://twitter.com/0xcharlie/status/133898695384109056). Federico Viticci [wrote about it for MacStories](http://www.macstories.net/news/security-researcher-demoes-bug-to-execute-unsigned-code-on-ios-devices/).
- Chris Schilling did a [fantastic interview with Matt Mills of ustwo](http://recombu.com/news/interview-ustwos-mills-on-whale-trail-the-rise-of-freemium-and-the-death-of-69p-gaming_M15758.html), creators of Whale Trail. So much insight about the state of the App Store and the game industry in this one. (Their [Making of Whale Trail](https://www.youtube.com/watch?v=r8bJs8opqRw) video is also worth watching.)
- [Copycats](http://mattgemmell.com/2011/11/27/copycats/) is a great article by Matt Gemmell:

  > There’s nothing new under the sun, as they say - we’re all inspired and affected by other things. All of our design takes place under constraints. So, be influenced. Incorporate elements. Agree with implementations. Understand an approach. Realise the purpose and function of a design decision. Address a need. _Renew something._ Be an innovator, not a copycat.
- David Barnard talks openly about [the rather disappointing launch of this beautiful new app](http://appcubby.com/blog/the-dreaded-app-store-fizzle/), TweetSpeaker.
- The guys from Shifty Jelly wrote a post that describes pretty well [how life is as an indie developer](http://shiftyjelly.wordpress.com/2011/11/22/you-guys-are-millionaires-right/).
- In [A Letter to the Developer Community](https://wildchocolate.tumblr.com/post/12555879965/a-letter-to-the-developer-community), Brittany Tarvin raises an important problem: what can we all do to make women feel more welcome in this community? For example, at Apple’s iOS 5 Tech Talk in Berlin this month, less than 1% of the participants were women. It felt just wrong, regardless if you were a man or a woman.
- [Great, encouraging quote from John Gruber’s keynote speech at the Çingleton Symposium](https://cycle-gap.blogspot.com/2011/11/john-gruber-has-some-career-advice-for.html) in October:

  > If you think this app store platform is big now, you really haven’t seen anything yet. … But I say to you, “This is an extraordinary time to be an Apple developer”. This is the right time and the right place. This is a once in a career opportunity. … If things go right, if things go the way I think they are going to go, these next five years, we are never going to work harder, we are never going to be under more pressure, we’re never going to be more stressed, we are never going to feel like we have to work faster and we are never going to have to solve tougher problems. We’re never going to have to move this fast. But the only thing any of us are going to regret is if we don’t aim big enough.

  The whole talk is worth watching.

# App Store

## Sandboxing Deadline Extended

Apple extended its deadline for Mac App Store apps to be sandboxed [from the planned November 2011 to March 1, 2012](http://developer.apple.com/news/index.php?id=11022011a). The nearer the original deadline came, realization probably grew in Cupertino that developers need more time to assess the impact of the sandboxing requirements on their apps and adapt them accordingly. And hopefully, Apple provides enough leeway to allow Mac apps to exist under sandboxing without impairing functionality that users take for granted.

On the occasion of Apple’s announcement, an interesting discussion about the merits (or not) of sandboxing sprung up in the blogosphere:

- Wil Shipley wrote a long article about the [benefits and drawbacks of sandboxing and other security measures such as code signing and code review](http://blog.wilshipley.com/2011/11/real-security-in-mac-os-x-requires.html). Wil concludes that sandboxing is not the right way and suggests that Lion only run code signed by an Apple certificate. At first, Apple would allow any developer to sign code with their certificate, but could then revoke it on a per-developer basis in case of a security problem.

  It’s an interesting idea and I certainly concur that Apple’s sandboxing model is not a good measure against malware. I’d add, however, that sandboxing has other merits, e.g. in the field of privacy.
- Pauli Olavi Ojala makes [a very convincing case against sandboxing](http://lacquer.fi/pauli/blog/2011/11/why-the-mac-app-sandbox-makes-me-sad/) from a functionality perspective: it seems to mean the end of app plugins.
- John Martellaro from The Mac Observer interviews MarsEdit developer Daniel Jalkut about [his opinion on the Mac App Store and especially sandboxing](http://www.macobserver.com/tmo/article/developer_losing_control_of_our_destiny_to_apple/).

## Pricing and Marketing

- Oliver Reichenstein [experimented with the pricing for iA Writer on iPad and Mac](https://plus.google.com/115711522874757126523/posts/LwZyWLKLN94): No matter what price we choose, we always make the same revenue.
- [Great story by Nathan Barry](https://nathanbarry.com/how-i-made-19000-on-the-app-store-while-learning-to-code/) how you can make money on the App Store not only without prior programming knowledge but also with a high-priced niche product.
- Ben Rooney reports on a talk by Greg Joswiak, part of the product marketing team at Apple, about [four keys to Apple’s success](http://blogs.wsj.com/tech-europe/2011/11/18/four-keys-to-apples-success/): Focus, Simplicity, Courage, Best. There is a lot of great quotes in this short piece.
- Nicholas Lovell about the tendency of the gaming market towards free: [Who Will Survive the Digital Tsunami?](http://www.gamasutra.com/view/news/38502/Opinion_Who_Will_Survive_The_Digital_Tsunami.php)
- King Sidharth wrote a good post called [Apps vs. Business](http://www.64notes.com/app-vs-business/). It takes more than just a good app to take down another business. You need to create a business: Solve a problem, then sell the solution.
- Confusion of the month: some company [announced that Apple approved a subscription-based gaming app](http://www.bloomberg.com/news/2011-11-22/apple-lets-big-fish-games-offer-ipad-subscription-a-first-for-video-games.html) but [Apple quickly removed it from the App Store](http://www.bloomberg.com/news/2011-11-23/apple-removes-big-fish-s-game-subscription-plan-from-app-store.html). Probably just a mistake by an app reviewer.
- Laugh of the month: Rich Jones reports that [the US government apparently paid $200,000 to have an absolute piece of crap app developed](http://gun.io/blog/the-governments-200000-useless-android-application/) (for three mobile platforms). Take a look at [the source code](http://www.osha.gov/SLTC/heatillness/heat_index/heat_app.html) yourself.

**Update December 1, 2011:** Marco Arment updated his regular [device and OS version stats](http://www.marco.org/2011/11/30/more-ios-device-and-os-version-stats-from-instapaper). As of the end of November, 45% of Instapaper users have updated to iOS 5. I would have expected a higher adoption rate.

# Competition

- Adobe finally [kills the Mobile Flash Player](http://blogs.adobe.com/conversations/2011/11/flash-focus.html). Opinions on the decision:

    - John Gruber: [Everybody wins](http://daringfireball.net/linked/2011/11/09/everybody-wins).
    - Matt Drance: [It is a victory for Adobe](http://www.appleoutsider.com/2011/11/09/falsh/).
- Apple Insider reports [an estimate by Piper Jaffray analyst Gene Munster](http://www.appleinsider.com/articles/11/11/21/googles_android_market_estimated_to_earn_just_7_of_what_apples_app_store_makes.html) saying that the Android Market has generated only 7% of the revenue that Apple’s App Store has made since its inception. This analysis is flawed on so many levels (different launch dates of the two stores; is the Mac App Store included?) that it is hard for me to believe in the numbers, though.
- Related to this, Ben Brooks attempts an explanation [why Android developers don’t make great looking apps](http://brooksreview.net/2011/11/apps-android/) – generally speaking.
- Jay Greene from CNET with the story [how and why Microsoft killed its promising Courier tablet](http://news.cnet.com/8301-10805_3-20128013-75/the-inside-story-of-how-microsoft-killed-its-courier-tablet/). I still think this thing could have been a hit.
- [Google released the source code for Android 4.0](https://groups.google.com/forum/#!msg/android-building/T4XZJCZnqF8/WkWhGUYb4MAJ).
- Nathan de Vries explains the [improvements that Android 4.0 made in its rendering pipeline](http://atnan.com/blog/2011/11/10/ios-vs-android-ics-hardware-accelerated-graphics-pipelines/), which should bring graphics performance into the same league as iOS and Windows Phone.

# Steve Jobs Biography

Walter Isaacson’s Steve Jobs biography came out in late October and many of you have probably already read the book. If you haven’t, I think you should do so because it really is quite good (although probably not as good as it could and should have been).

- In episodes [42](http://5by5.tv/hypercritical/42) and [43](http://5by5.tv/hypercritical/43) of the Hypercritical podcast, John Siracusa makes some very strong and well-founded arguments against the book and its author: Jobs picked the wrong guy. The podcasts are not short but if you make the effort to read the book, I think you should also listen to these episodes, it’s worth it.
- Jean-Louis Gassée [reviews the Jobs biography from his insider perspective](http://www.mondaynote.com/2011/10/30/steve%E2%80%99s-bio-a-personal-perspective/) as one of the top Apple employees in the post-Jobs era.
- A recent Churchill Club [panel about Steve Jobs’s Legacy](https://www.youtube.com/watch?v=N2C2oCsrqcM) is a very good companion to the book. The panel’s participants Bill Atkinson, Jean-Louis Gassée, Andy Hertzfeld, Regis McKenna, Deborah Stapleton, Larry Tesler are some of the people you also get to know in the early chapters of the biography.
- John Gruber, criticizing [Malcom Gladwell’s take on Jobs’s personality](http://www.newyorker.com/reporting/2011/11/14/111114fa_fact_gladwell?currentPage=all): [Getting Steve Jobs Wrong](http://daringfireball.net/2011/11/getting_steve_jobs_wrong).
- Nick Bilton did a [short interview with Walter Isaacson](http://bits.blogs.nytimes.com/2011/11/18/one-on-one-walter-isaacson-biographer-of-steve-jobs/) about the book.

  > He had three things that he wanted to reinvent: the television, textbooks and photography. He really wanted to take these on.
- Luke Wroblewski: [Memorable quotes from Robert X. Cringely’s rediscovered 1995 interview with Steve Jobs](http://www.lukew.com/ff/entry.asp?1449)
