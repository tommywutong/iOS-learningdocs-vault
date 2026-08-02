---
title: OverlayView
apple_id: DTS40008906
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-02-28'
source_url: https://developer.apple.com/library/archive/samplecode/OverlayView/Introduction/Intro.html
archived_at: '2026-07-18T03:18:18.702078Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# OverlayView

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2013-02-28 Upgraded for OS X 10.8 SDK, updated to adopt current best practices for Objective-C. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojqgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.8 SDK or later |
| __Runtime Requirements:__ | OS X v10.7 or later |

An overlay view is a straightforward subclass of NSView that can draw on top of sibling views by simply being the last subview of the parent. In this example, we imitate a behavior of Interface Builder and Keynote to show "guidelines" between the edge of a view and the edges of the view which contains it. We also use tracking areas to receive mouse moved events and implement some mouse event handling methods to allow the user to move the views.

[Next](ReadMe.txt.md)

