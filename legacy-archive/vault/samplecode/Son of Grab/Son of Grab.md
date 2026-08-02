---
title: Son of Grab
apple_id: DTS10004490
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: Quartz
published: '2015-05-18'
source_url: https://developer.apple.com/library/archive/samplecode/SonOfGrab/Introduction/Intro.html
archived_at: '2026-07-18T03:24:58.159362Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# Son of Grab

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2015-05-18 Updated to 10.10 SDK. Converted to ARC. Updated to follow Objective-C best practices. Other miscellaneous changes. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbzgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X 10.10 SDK or later |
| __Runtime Requirements:__ | OS X 10.8 or later |

Demonstrates the CGWindow API to grab the contents of arbitrary sets of windows.

The core of this sample are 5 methods on the Controller class, described below.

-updateWindowList
This method gets the current list of windows from the window server. Options in the GUI allow you to exclude offscreen windows and desktop elements. The list returned from the window server is further processed (via the WindowListApplierFunction callback) to produce the list that is presented in the GUI.

-createSingleWindowShot
Creates a screen shot relative to the single CGWindowID that is passed in. Depending on the "Single Window Options" specified in the GUI, the screen shot may include any number of other windows and may or may not include the window actually passed to this method.

-createMultiWindowShot
Creates a screen shot with exactly those windows passed in. Uses the -createWindowListFromSelection method to create a compatible CFArrayRef that specifies the windows to create an image from.

-createScreenShot
Creates a screen shot from all of the windows that are currently onscreen and readable.

-createWindowListFromSelection
Transforms the GUI selection of windows into a CFArrayRef that specifies the exact list of windows to render and the order to render them in.

[Next](main.m.md)

