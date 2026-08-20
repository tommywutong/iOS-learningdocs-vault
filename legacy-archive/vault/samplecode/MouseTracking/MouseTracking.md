---
title: MouseTracking
apple_id: DTS10003602
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/MouseTracking/Introduction/Intro.html
archived_at: '2026-07-18T03:16:02.572396Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# MouseTracking

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2005-06-01 Sample code used in the WWDC 2005 Hands-On session 215 "Moving from QD to Quartz" |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X 10.4 |

Demonstrates solutions for various issues the come up during a QD -> Quartz conversion:
a) Tracking loop to collect CGPath data: globalToLocal, HIView coordinates
b) Using a CGPath and CGPathApply for drawing and clipping (vs. the QD clipRgn)
c) Using a 1x1 bitmap context for hit testing
d) Drag a clipped image portion around (vs. GWorlds, CopyBits, maskRgn, CopyDeepMask etc.)
e) Use a masked image to remove the white background in the image (vs. CopyBits, SearchProc, BitmapToRegion etc.)
f) Demonstrate two different ways to produce the masked image: CGImageCreateWithMaskingColors, and CGImageCreateWithMask, where the mask was an image created from a gray-level bitmap context.

[Next](main.c.md)

