---
title: BetterAuthorizationSample
apple_id: DTS10004207
resource_type: Sample Code
platform: macOS
topic: Security
technology: Security
published: '2007-11-27'
source_url: https://developer.apple.com/library/archive/samplecode/BetterAuthorizationSample/Introduction/Intro.html
archived_at: '2026-07-18T03:01:51.240556Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](BetterAuthorizationSampleLib.c.md)

Relevant replacement documents include:

- [https://developer.apple.com/library/mac/samplecode/EvenBetterAuthorizationSample/](https://developer.apple.com/library/mac/samplecode/EvenBetterAuthorizationSample/)

# BetterAuthorizationSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-11-27 Shows the recommended way to access privileged functionality from a non-privileged application on Mac OS X. |
| __Build Requirements:__ | Xcode 2.4.1 |
| __Runtime Requirements:__ | Mac OS X 10.4.6 |

BetterAuthorizationSample shows the recommended way to access privileged functionality from a non-privileged application on Mac OS X. This involves putting the privileged code into a small, privileged helper tool that is run by launchd. Apple recommends this approach because it is more secure than previously documented approaches (such as using a setuid root helper tool).

[Next](BetterAuthorizationSampleLib.c.md)

