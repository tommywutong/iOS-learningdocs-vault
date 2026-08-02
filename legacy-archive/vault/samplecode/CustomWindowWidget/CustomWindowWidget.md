---
title: CustomWindowWidget
apple_id: DTS10000632
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/CustomWindowWidget/Introduction/Intro.html
archived_at: '2026-07-18T03:05:43.744888Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# CustomWindowWidget

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Demonstrates two ways of adding a custom window widget to the window frame of a standard document window. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Mac OS X |

This sample code demonstrates two ways of adding a custom window widget to the window frame of a standard document window: - on 10.1 and earlier, it overrides the kEventWindowDrawFrame, kEventWindowDrawPart, and kEventWindowHitTest events. - on 10.2 and later, it uses a custom HIView, which it inserts into the root view of the window. Requirements: Mac OS X Keywords: window, HIView, window frame, widget

[Next](main.c.md)

