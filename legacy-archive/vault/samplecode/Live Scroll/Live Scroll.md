---
title: Live Scroll
apple_id: DTS10000591
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Live_Scroll/Introduction/Intro.html
archived_at: '2026-07-18T03:13:40.778767Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AppleEvents.c.md)

# Live Scroll

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Demonstrates how to implementing live scrolling during the tracking of scroll bar thumbs. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

"Live Scroll" is a bare bones application demonstrating one approach you can take to implementing live scrolling (aka active and dynamic scrolling) during the tracking of scroll bar thumbs. Scroll arrows allow accurate placement of a document within its window, but are often too slow when the user wishes to scroll the content relatively large distances. While the scroll thumb can be used in this situation, it is less than ideal because the user cannot see the result of the scroll until the thumb is released. As a result, the user often finds that two or more scroll operations are required before the desired positioning is achieved. These problems can be overcome by implementing live scrolling within an application which allows a user to more accurately scroll a document to the correct position with direct control over the speed of the scrolling, and by providing complete visual feedback of the scrolling operation as it occurs. It also demonstrates the two different types of action procedure, both for 68K and PowerPC architectures. Requirements: Keywords: live scrolling, control, appearance, scroll

[Next](AppleEvents.c.md)

