---
title: TextSizingExample
apple_id: DTS40008841
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-06-05'
source_url: https://developer.apple.com/library/archive/samplecode/TextSizingExample/Introduction/Intro.html
archived_at: '2026-07-18T03:26:41.579686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# TextSizingExample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-06-05 Updated for Mac OS X 10.7 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobugewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

This example demonstrates different ways of configuring the objects in the Cocoa text system. The app displays a window where different examples of NSTextViews with different sizing properties can be shown. A pop-up button at the top of the window controls which example is visible.

In most of the examples, the same NSTextStorage is used and the example contains an NSLayoutManager that adds itself to the shared NSTextStorage and one or more pairs of NSTextContainer and NSTextView objects. By default this NSTextStorage loads this ReadMe file, but you can load a new file or edit the text.

[Next](main.m.md)

