---
title: Color Finder Safari Extension
apple_id: DTS40011115
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/ColorFinderSafariExtension/Introduction/Intro.html
archived_at: '2026-07-18T03:03:55.189116Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Color Finder Safari Extension

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2011-06-07 This extension uses a popover to show the colors used by the current page. |
| __Build Requirements:__ | Safari v5.1 or later |
| __Runtime Requirements:__ | Safari v5.1 or later |

When the user clicks on the toolbar item for this extension, a popover that is specified in the Extension Builder is shown. When the popover event is received, the popover sends a message to the content script to gather the color information for the current web page. The content script iterates through all the stylesheets of the current web page, and then sends a message back up to the Application Layer with this information. The color information is then turned into HTML content and shown in the popover.

This extension also includes a bar that can be used instead of the popover. To use the bar, add a bar in the Extension Builder that uses bar.html.

[Next](ReadMe.txt.md)

