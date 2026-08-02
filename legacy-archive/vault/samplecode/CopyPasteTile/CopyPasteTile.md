---
title: CopyPasteTile
apple_id: DTS40009040
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2010-06-28'
source_url: https://developer.apple.com/library/archive/samplecode/CopyPasteTile/Introduction/Intro.html
archived_at: '2026-07-18T03:04:20.726524Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# CopyPasteTile

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2010-06-28 Added CFBundleIconFiles in Info.plist. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbugawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 4.0 SDK |
| __Runtime Requirements:__ | iPhone OS 3.2 or later |

CopyPasteTile demonstrates how to implement the copy-cut-paste feature introduced in iPhone OS 3.0. The sample:

\* Shows how to use the UIMenuController class to position and display the editing menu (the menu with the Copy, Cut, Paste, and other commands).

\* Illustrates how you might implement the canPerformAction:withSender: method of UIResponder to validate the menu commands for the current context.

\* Shows how to respond when the user taps a menu command by reading and writing data to a pasteboard, (an instance of the UIPasteboard class).

[Next](ReadMe.txt.md)

