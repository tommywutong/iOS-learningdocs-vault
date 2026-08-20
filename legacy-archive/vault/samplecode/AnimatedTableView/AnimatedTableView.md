---
title: AnimatedTableView
apple_id: DTS40008863
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-05-31'
source_url: https://developer.apple.com/library/archive/samplecode/AnimatedTableView/Introduction/Intro.html
archived_at: '2026-07-18T03:01:02.253573Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AnimatedTableView

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2012-05-31 Upgraded to Xcode 4.3 and Mac OS X 10.7, fixed some leaks. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobwgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.3, Mac OS X v10.7.x or later |
| __Runtime Requirements:__ | Mac OS X v10.6.x or later |

This example demonstrates some advanced concepts and features in NSTableView and NSBrowser. The application loads images from a specific directory and displays them in a custom NSTableView subclass on the left side. The Table View displays a list of cells that display an desktop background image along with a fill color that can be edited with a custom pop-up color editor. While images are loading, an animated progress indicator is added to the Table View. A basic NSImageView displays the selected image on the right side of the window, which can then be set as the desktop wallpaper via a button click. Double clicking on the large Image View will bring up a customized NSBrowser that allows modifying the image through a series of CoreImage filters.

[Next](ReadMe.txt.md)

