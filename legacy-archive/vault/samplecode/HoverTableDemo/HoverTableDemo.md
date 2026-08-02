---
title: HoverTableDemo
apple_id: DTS40011082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/HoverTableDemo/Introduction/Intro.html
archived_at: '2026-07-18T03:11:56.187594Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# HoverTableDemo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2012-10-04 Upgraded to OS X 10.8 to eliminate build warnings, now uses NSDictionary to back each table row, App Sandboxing enabled. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmbygiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.4, OS X 10.8 |
| __Runtime Requirements:__ | OS X 10.7 or later |

Demonstrates how to use view-based NSTableViews in your application, complete with custom drawing and mouse tracking.

It subclasses NSTableView's drawGridInClipRect for custom grid drawing as well as "setFrameSize:size" to invalidate more elements when live-resizing occurs. The sample implements a custom NSTableRowView class that tracks the mouse to achieve an elegant selection appearance. The overrides for this include:

Override point to draw a custom background: drawBackgroundInRect:dirtyRect Override point for drawing the (horizontal) separator: drawSeparatorInRect:dirtyRect Override point for drawing the selection: drawSelectionInRect:dirtyRect

[Next](ReadMe.txt.md)

