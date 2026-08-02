---
title: WDEFPatch
apple_id: DTS10000199
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WDEFPatch/Introduction/Intro.html
archived_at: '2026-07-18T03:28:05.801860Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](wdefpatch.c.md)

# WDEFPatch

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This snippet shows how you can add a simple extra part to an existing WDEF and be able to do hit testing on the part via FindWindow(). The extra part in this case is on the right side of the title bar, just to the left of where the zoombox would be. When hit, it inverts the window. Previous version stomped the variation code bits containing the zoom box data. Fixed this by adding some code to mask these bits in if we're in 24-bit mode. Also, previous version assumed a5 would be set-up inside WDEF code, since it called StripAddress which is glue in Think C. Fixed by adding a5 stuff to patch code.

[Next](wdefpatch.c.md)

