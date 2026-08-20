---
title: CrossEvents
apple_id: DTS10004324
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2007-05-31'
source_url: https://developer.apple.com/library/archive/samplecode/CrossEvents/Introduction/Intro.html
archived_at: '2026-07-18T03:05:17.406628Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# CrossEvents

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-05-31 Demonstrates how to send CarbonEvents and NSNotifications between Carbon and Cocoa. |
| __Build Requirements:__ | Mac OS X 10.5, Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

"CrossEvents" is a Carbon-Cocoa hybrid application that demonstrates how to send Carbon Events and NSNofitications between Carbon and Cocoa portions of code. In particular a custom Carbon Event is created and sent from a window handler to an Objective-C controller object. In the opposite way an NSNotification is sent from NSTextField delegate method to a notification listener object on the Carbon side. In using this technique this sample shows how you can change content between Carbon's HITextView and Cocoa's NSTextField, all within the same Carbon window.

[Next](main.c.md)

