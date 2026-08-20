---
title: SimpleDrillDown
apple_id: DTS40007416
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2012-02-28'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleDrillDown/Introduction/Intro.html
archived_at: '2026-07-18T03:24:00.067924Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SimpleDrillDown

|  |  |
| --- | --- |
| __Last Revision:__ | Version 3.1, 2012-02-28 Corrected table view cell style to be Basic instead of Custom. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonbrgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.2 or later, OS X v10.7 or later, iOS 5 or later. |
| __Runtime Requirements:__ | OS X v10.7 or later, iOS 5 or later. |

This application shows how to create a basic drill down interface.

The first scene shows a list of plays. When the user selects a play, the application displays a second scene that shows a list of the main characters and other data about the play. Both screens use a table view. The first list is in the "plain" style to show a standard list; the second is in the grouped style that you can use to lay out detail information.

The transition from the first scene to the second is defined by a segue associated with the prototype table view cell in the table view controller's table view. In the storyboard, the segue is named, "ShowSelectedPlay". The name is used as the idetifier in RootViewController's prepareForSegue:sender: method.

[Next](ReadMe.txt.md)

