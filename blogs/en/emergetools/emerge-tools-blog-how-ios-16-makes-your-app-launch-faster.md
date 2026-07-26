---
title: 'Emerge Tools Blog | How iOS 16 makes your app launch faster'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/iOS16LaunchTime'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:ce2fe3708c50fa5a'
translated: false
---

> 原文：[Emerge Tools Blog | How iOS 16 makes your app launch faster](https://www.emergetools.com/blog/posts/iOS16LaunchTime)　·　Emerge Tools Blog

# How iOS 16 makes your app launch faster

July 6, 2022 by

[Noah Martin](https://twitter.com/sond813)

iOSPerformanceStartup time

![Graphic with text "iOS 16 Startup Time Discoveries"](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog8.857fc0f9.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

WWDC22's [state of the union](https://developer.apple.com/videos/play/wwdc2022/102/) promised to bring some big launch time improvements:

_with apps like Lyft or Airbnb launching almost twice as fast thanks to improvement in the dynamic linker._

This improvement comes from speeding up protocol checks, which I demonstrated to be slow in a [previous blog post](https://www.emergetools.com/blog/posts/SwiftProtocolConformance). Additionally, iOS 16 improves the time it takes to load a binary by reducing the amount of data loaded from disk. This was also the subject of a [previous article](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles).

These improvements come down to changes in [dyld](https://www.emergetools.com/glossary/dyld) -- the program responsible for bootstrapping your app and starting execution of your own code. They also take two opposite (but common) approaches to improving performance - **eager loading**, and **lazy evaluation**.

In this post, we'll look at what changed in iOS 16, how much faster it really is, and how you can best take advantage of these new features in your app.

## [Protocol checks](https://www.emergetools.com/blog/posts/iOS16LaunchTime#protocol-checks)

Protocol conformance checks happen in the Swift runtime to determine the result of code like `myVar as? MyProtocol`. Every time a type conforms to a protocol the binary will include a "conformance record". When checking a conformance, the runtime loops over every conformance record to see if any match the current operation. This loop is O(n) where n is the number of conformance records in your app. For big apps there can be over one hundred thousand, making each conformance check very slow.

Protocol conformance checks are widespread in Swift apps even if you don't write them, because they are also invoked from common operations like `String(describing:)` or `AnyHashable`. For some large Swift apps, such as Lyft and Airbnb, close to half of the launch time is spent in protocol conformance checks.

The big change comes in the "dyld closure", which is a per-app cache used to accelerate various dyld operations during app launch. The **closure now contains pre-computed conformances**, allowing each lookup to be much faster. Note that the dyld closure is not always used, e.g. because it's out-of-date or because it's being launched from Xcode, which complicates things. This change was implemented in the Swift open source project as part of [Mike Ash's PR](https://github.com/apple/swift/pull/41185), which adds the dyld API call: `_dyld_find_protocol_conformance_on_disk`. If the conformance is found with this cache, the O(n) operation is completely skipped, so we should see big improvements to apps with a large number of conformances.

### [Testing it out](https://www.emergetools.com/blog/posts/iOS16LaunchTime#testing-protocol-checks)

At Emerge, we run a lot of performance tests to identify how PRs impact app launch.. So naturally, we wanted to measure exactly how these precomputed conformance checks will affect launch time.

Since we are dealing with two different OS versions, we can't test on the same device. Instead, I opted to micro-benchmark the time for a conformance check across an app with 10k, 20k, 30k, 40k, and 50k conformances in the binary. Each version is launched on an iOS 16 and iOS 15 device, with the 10k conformance considered a baseline and only times relative to the baseline are compared.

![Time to check conformances on iOS 16 and 15.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog8%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Clearly, iOS 15 gets slower as more conformances are added while iOS 16 does not, problem solved! In practice, the closure is not always going to be available, so we'll have to wait until iOS 16 hits user devices in a few months to know exactly how much this will change numbers in production. This improvement applies to all apps, even if their minimum deployment target is below iOS 16.

## [Page faults](https://www.emergetools.com/blog/posts/iOS16LaunchTime#page-faults)

The second big improvement comes from reducing the amount of data that has to be loaded from disk at startup. The first time a piece of code is executed, the kernel loads the surrounding chunk of memory, known as a page, in a process called a **page fault**. On app launch some parts of the binary need to be fixed up before the code can run (an in-depth explanation of this is in a [previous blog post](https://www.emergetools.com/blog/posts/SwiftReferenceTypes)). On iOS 15 all fixups were done at app launch, meaning any location in the binary requiring a fixup had to be paged in. Now, a new feature called [page-in linking](https://developer.apple.com/wwdc22/110362) resolves fixups lazily, only the first time a page is accessed.

Last year's WWDC introduced a major new format to the metadata used to perform these fixups, which I [covered in depth](https://www.emergetools.com/blog/posts/iOS15LaunchTime) at the time. This format is required for the lazy evaluation of fixups, so iOS 16 users will only get it if you target iOS 13.4 or later.

### [Testing it out](https://www.emergetools.com/blog/posts/iOS16LaunchTime#testing-page-faults)

On iOS 15, all of the __DATA and __DATA_CONST segments of a binary contain fixups, so the total number of page faults before your code even runs is just the size of these segments. With Emerge's tooling, we can also measure how many pages your code needs to run, the difference gives us how many fewer page faults you have in iOS 16.

### [Getting the full benefit](https://www.emergetools.com/blog/posts/iOS16LaunchTime#getting-the-full-benefit)

This is a great improvement that immediately reduces page faults, but there are ways to get an even larger reduction. Emerge offers an order file service - Launch Booster - which automatically orders a binary to minimize page faults. We **improved launch time by an average of 18%** when deploying an order file to the app store on iOS 15. Now that iOS 16 doesn't automatically load every page, ordering the binary can make your app startup time even faster! If you'd like to learn more about how you can automatically reduce startup time and take advantage of iOS 16 improvements, [get in touch](https://www.emergetools.com/cdn-cgi/l/email-protection#6d1e181d1d021f192d0800081f0a08190202011e430e0200) with the Emerge team.
