---
title: On Teaching iOS Programming
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/on-teaching-ios-programming/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f6ef072b42b50f4d'
translated: false
---

> 原文：[On Teaching iOS Programming](https://oleb.net/blog/2011/06/on-teaching-ios-programming/)　·　Ole Begemann

# On Teaching iOS Programming

I held my first course in iOS development for beginners last weekend and it was great. I had the privilege to introduce eight students with all kinds of different backgrounds to the iOS platform and SDK. All of them had programming experience in other languages and some had even worked through a few iOS programming tutorials before, though that was not required.

Over two days, we covered the basics of Objective-C, talked about pointers and memory management, and learned our way around Xcode 4. I introduced the Cocoa Touch frameworks and common design patterns like delegating and target-action and we spent a lot of time building view controllers and designing app flows around view controller hierarchies. After playing around with some cool iOS features like view animations and gesture recognizers, we used the beginning of day 2 to practice debugging with Xcode and Instruments.

We spent the rest of the day designing a more or less complete little app: I chose a basic RSS reader (called _Feeder_) for this because it lends itself nicely to a classic navigation controller design. It is also a great way to introduce talking with web services (through `NSURLConnection`) and local caching of the results (with Core Data). Everything together yields a fairly complex app that serves as a nice example to illustrate the code design of larger projects.

![iPhones with screenshots of RSS reader app Feeder](https://oleb.net/media/feeder-iphone-screenshots.png)

<sub>Screenshots of _Feeder_, my little RSS reader sample app.</sub>

As I had expected beforehand, two days was not enough time to examine every aspect of Feeder in detail. At the end, I had to quickly go over some important concepts that I felt needed more explanation and practice. Still, I felt it important to not just work with countless small examples, thereby leaving the students in the dark on how to approach the design of a “real” app. Perhaps timing-wise it would have been better to move the harder stuff into the morning hours and leave the afternoon, when everyones’ heads are about to explode, for playing around and exploring the SDK, as one participant has suggested. Another alternative would be to extend the workshop to three days.

Anyway, I had a lot of fun teaching and I got some very good feedback from my students (thank you for that!), so if time permits, I will probably make this a more or less regular thing in the future. Not only because I enjoyed it so much but also because it is a great way for myself to learn. As the saying goes, if you really want to learn something, teach it to someone else. Highly recommended.

I will post some of the things I have prepared (and learned) for the course, including the source code of _Feeder_, here on my blog in the coming weeks.
