---
title: Target-Action using Cocoa Bindings
apple_id: DTS10004366
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-04-18'
source_url: https://developer.apple.com/library/archive/samplecode/BoundButton/Introduction/Intro.html
archived_at: '2026-07-18T03:02:13.089696Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Target-Action using Cocoa Bindings

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2013-04-18 Update to use ARC, Auto Layout, Base Localization, and modern Objective-C syntax (including use of properties, autosynthesis, and literals). [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzwgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.8, Xcode 4.5 |
| __Runtime Requirements:__ | Mac OS X v10.8 |

This is a simple example that illustrates how you can use Cocoa bindings to bind a button's target and action parameters.

In most situations, target/action is the appropriate pattern to use for buttons - you simply want a method to be invoked when the button is pressed. Sometimes, however, it may be convenient to use bindings to collect information from your application and pass it to the target using the method arguments, or the target itself might be selected dynamically. In these situations, using bindings may prove beneficial. In this example, the selections in the two table views are collected from their corresponding array controllers using bindings.

[Next](ReadMe.txt.md)

