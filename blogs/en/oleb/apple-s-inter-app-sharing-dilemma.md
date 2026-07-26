---
title: 'Apple''s Inter-App Sharing Dilemma'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/12/apples-inter-app-sharing-dilemma/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a211e62710fbe8e8'
translated: false
---

> 原文：[Apple's Inter-App Sharing Dilemma](https://oleb.net/blog/2013/12/apples-inter-app-sharing-dilemma/)　·　Ole Begemann

# Apple's Inter-App Sharing Dilemma

Developers and users ([myself included](https://oleb.net/blog/2012/02/what-ios-should-learn-from-android-and-windows-8/)) have hoped for a long time that Apple would introduce better inter-app data sharing features to iOS. The lack of new inter-app sharing functionality in iOS 7 was the major letdown of the new version for me.

In fact, Apple didn’t just not add new sharing features to iOS 7, they even took one away: shared named pasteboards. Up until iOS 6, apps could create additional pasteboards and put arbitrary data in them. Any other app that knew the name of such a pasteboard could freely read from and write to it. In iOS 7, this functionality is restricted to apps from the same vendor.[1](#fn:1)

Named pasteboards got a bit of publicity in recent months because the [TextExpander touch](http://smilesoftware.com/TextExpander/touch/) app used them to share snippets with third-party apps. When this became impossible in iOS 7, TextExpander [switched over to the system’s Reminders database](http://smilesoftware.com/blog/entry/how-ios-7-affects-textexpander-touch) as a shared data storage, a hacky solution that [Apple recently decided not to accept any longer](http://www.smilesoftware.com/blog/entry/important-changes-in-textexpander-touch-for-ios).

# Why?

While I think Apple was right in rejecting the abuse of the Reminders store, the question why they don’t offer better sharing APIs remains. And I don’t think the answer is spite or that they just don’t care.

I truly believe Apple realizes that better inter-app sharing is a desirable feature for iOS users and developers. It’s conceivable that they simply haven’t gotten around to it (maybe the iOS 7 redesign was a higher priority this year) but then why did they disable shared pasteboards? That would not make sense.

I think Apple faces a real dilemma here. Any API that facilitates data sharing between apps without user interaction can easily be abused for tracking purposes, a practice Apple has opposed pretty strongly – at least in word if not in actual rejections of apps.

Just like ad networks, analytics services and social network companies (trough social sharing buttons) are able to track users across websites, analytics and ad libraries can track a user’s app usage across multiple apps as long as they have a common identifier for each device. Trackers used to use the unique device identifier for this purpose until [Apple forbid it](http://arstechnica.com/apple/2013/03/apple-forcing-developers-to-ditch-unique-device-ids/). Afterwards, many libraries switched to solutions that involved shared pasteboards. I am not sure if tracking companies have found another solution that works in iOS 7 (short of heuristics).[2](#fn:2)

# What Can Apple Do?

The nature of a dilemma is that there is no perfect solution. Let’s have a look at the options Apple has:

1. Leave everything as-is. Provide no official sharing APIs and try to close any loopholes that tracking companies might find in the future. App developers with legitimate needs for inter-app sharing need to find another solution. For instance, [Brent Simmons suggested a web service](http://inessential.com/2013/11/21/textexpander_and_data_sharing) for TextExpander. That comes with its own problems (user/device identification, additional cost for the developer, no offline mode) but it is certainly an alternative in many cases.
2. Provide an official sharing API that only works with user interaction. Just like apps cannot send emails or text messages from the user’s account without an explicit action by the user, this would require the user to confirm any data exchange. Depending on the implementation, this solution might not work well in TextExpander’s case but it would definitely solve lots of common sharing problems.
3. Provide an official sharing API that also works without user interaction (like shared pasteboards or a common folder on the file system that all apps could access) and at the same time improve the app review process to expose abusers. I’d love to see this but stricter app reviews (and removal from the App Store if found out later) do not seem like something Apple wants to do. For example, I cannot recall an example of an enforcement of this general rule in the [App Store Review Guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html) that is related to privacy abuse:

  > If you attempt to cheat the system (for example, by trying to trick the review process, steal data from users, copy another developer’s work, or manipulate the ratings) your Apps will be removed from the store and you will be expelled from the developer program.

My hope for iOS 8 is that we will at least see an implementation of option 2. Basically, what I envision is the ability for any app to add itself to the built-in system sharing sheet for all data types the app supports.

1. It’s worth noting that arbitrary named pasteboards have been a long-standing feature of OS X. When Apple ported the pasteboard code to iOS (with the introduction of copy & paste in iPhone OS 3.0), they may not have considered the implications of this feature for sharing data between app sandboxes or they might not have ported the functionality over in the first place. [↩︎](#fnref:1)
2. The official replacement API for the unique identifier, [`advertisingIdentifier`](https://developer.apple.com/library/ios/documentation/AdSupport/Reference/ASIdentifierManager_Ref/ASIdentifierManager.html#//apple_ref/doc/uid/TP40012654-CH1-SW4), does not technically limit device tracking so it could be used for this purpose. But Apple allows its use only “for the purpose of serving advertising” (whatever that means). Additionally, apps are required to respect the user’s preference to limit ad tracking. How strictly these rules are enforced during app review is anybody’s guess. [↩︎](#fnref:2)
