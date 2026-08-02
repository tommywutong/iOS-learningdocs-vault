---
title: Deep Image Display with Quartz
apple_id: DTS40012163
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2012-04-04'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplay/Introduction/Intro.html
archived_at: '2026-07-18T03:06:06.393965Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Deep Image Display with Quartz

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2012-04-04 Shows how specialized dithering improves the rendering of “deep” images (greater than 8-bpc) on OS X Lion. |
| __Build Requirements:__ | Mac OS X 10.7 SDK or later |
| __Runtime Requirements:__ | Mac OS X 10.7 or later |

The “Deep Image Display with Quartz” sample shows how to take advantage of specialized dithering to improve the appearance of “deep” images (i.e. greater than 8-bits per color channel) drawn using Quartz.

When a window’s color depth limit is set to 64-bit (RGBA 16-16-16-16), a specialized dither pattern is automatically applied to the window’s content as it is composited into the 8-bits per color channel frame buffer. This dithering minimizes the appearance of quantization artifacts on screen.

For comparison purposes, the sample application shows a color gradient image in two windows. The left image shows a deep version of the image drawn using the above technique while the right shows a “standard” (8-bits per color channel) version.

[Next](ReadMe.txt.md)

