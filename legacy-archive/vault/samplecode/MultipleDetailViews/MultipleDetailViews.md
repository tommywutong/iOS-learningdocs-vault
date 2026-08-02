---
title: MultipleDetailViews
apple_id: DTS40009775
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2012-09-18'
source_url: https://developer.apple.com/library/archive/samplecode/MultipleDetailViews/Introduction/Intro.html
archived_at: '2026-07-18T03:16:28.954732Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# MultipleDetailViews

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-09-18 Demonstrates managing the presentation of multiple detail view controllers with a navigation hierarchy that includes multiple levels. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzxguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 5.0 SDK or later |
| __Runtime Requirements:__ | iOS 5.0 or later |

This sample shows how you can use UISplitViewController to manage the presentation of multiple detail views in conjunction with a navigation hierarchy.

The application uses a split view controller with a custom object as its delegate. When you make a selection in the table view, a new view controller is set as the split view controller's second view controller.

The custom split view delegate defines a protocol (SubstitutableDetailViewController) that detail view controllers must adopt. The protocol specifies a property to hide and show the bar button item controlling the popover.

[Next](ReadMe.txt.md)

