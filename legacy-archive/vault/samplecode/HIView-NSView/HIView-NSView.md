---
title: HIView-NSView
apple_id: DTS10004005
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2007-05-29'
source_url: https://developer.apple.com/library/archive/samplecode/HIView-NSView/Introduction/Intro.html
archived_at: '2026-07-18T03:11:35.086313Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# HIView-NSView

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2007-05-29 Upgraded to use NSViewController. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbqguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.0 (or the latest) |
| __Runtime Requirements:__ | Mac OS X 10.5 |

Demonstrates how to embed an NSView within an HIView in a Carbon window. This Carbon sample includes both a Carbon and a Cocoa nib file. The Cocoa nib, WebView.nib, contains a view hierarchy embedded in a top level NSView. After a new Carbon window is created, an NSViewController is used to load the Cocoa nib and get a reference to the top level view. The NSView hierarchy is then embedded in an HICocoaView. All the connections made in Interface Builder are preserved. NSViews can be created manually or with Interface Builder.

[Next](main.c.md)

