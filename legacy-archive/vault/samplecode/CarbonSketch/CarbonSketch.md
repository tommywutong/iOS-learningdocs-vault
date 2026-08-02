---
title: CarbonSketch
apple_id: DTS10003226
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/CarbonSketch/Introduction/Intro.html
archived_at: '2026-07-18T03:03:13.286488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# CarbonSketch

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-03-23 Updated to be compatible with systems earlier than Mac OS v10.3 by using weak linking for Pasteboard API symbols. |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X 10.2 and Later |

CarbonSketch is a HIToolbox-based Carbon drawing application which instead of using QuickDraw APIs, does all of its rendering using Core Graphics.
This Sample Demonstrates:
1) The usage of an overlay window for mouse-tracking feedback.
2) The usage of a 1x1-CGBitmapContext for hit-testing.
3) Printing
4) Saving as a PDF File.
5) Copy and Paste of pdf data using the new Pasteboard API's.
6) Weak linking and verification that the Pasteboard API's exist before using them.

[Next](ReadMe.txt.md)

