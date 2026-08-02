---
title: ZoomRecter
apple_id: DTS10000178
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomRecter/Introduction/Intro.html
archived_at: '2026-07-18T03:28:43.779778Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CodeWarrior%20%28OS%209%29-CarbonPrefix.h.md)

# ZoomRecter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-10-10 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon (both 9 and X) QuickDraw, CarbonLib |

This sample has been updated for the Carbon API. This snippet shows how to do "Finder" style zooming between two rectangles. The boolean flag "kZoomLarger" controls the proportional direction of the zooming. To get the two rectangles, you drag them out rubberbanded, and the zoom occurs between them. To quit, click the close box. If you want to do zooms between windows, open up a port with the dimensions of the desktop (from GetGrayRgn()). DON'T use this as a sample of how to do rubberband drawing!!! It's sort of hacked together bypassing the event mechanism and just using Button(). Requirements: QuickDraw, CarbonLib Keywords: Zoom Rect, Carbon

[Next](CodeWarrior%20%28OS%209%29-CarbonPrefix.h.md)

