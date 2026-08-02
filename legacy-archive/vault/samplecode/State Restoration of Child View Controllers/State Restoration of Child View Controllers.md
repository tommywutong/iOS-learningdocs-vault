---
title: State Restoration of Child View Controllers
apple_id: DTS40013492
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2013-09-05'
source_url: https://developer.apple.com/library/archive/samplecode/StateRestoreChildViews/Introduction/Intro.html
archived_at: '2026-07-18T03:25:43.990443Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# State Restoration of Child View Controllers

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2013-09-05 UIWindow's makeKeyAndVisible now called in willFinishLaunchingWithOptions. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 6.0 SDK or later |
| __Runtime Requirements:__ | iOS 6.0 or later, Automatic Reference Counting (ARC) |

Demonstrates how to implement "State Preservation and Restoration" in an app with child view controllers. The sample contains one parent view controller, which can host two different child view controllers. The user taps the segmented control to toggle between the two different children.

It shows how to preserve and restore the "current" child view controller. It encodes/decodes the segmented control state to decide which child to make visible. When the app is re-launched, it decodes the segmented control state as well as each child view, and properly adds the correct child to its parent. To make this all work properly, the parent view controller needs to encode/decode both children. In addition, to round out the sample, each child view controller restores it's text field state. The parent and both children are required to have restoration identifiers.

[Next](ReadMe.txt.md)

