---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Introduction/Intro.html
archived_at: '2026-07-18T03:06:06.800031Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Sources-main.mm.md)

# Deep Image Display with OpenGL

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2015-12-10 First release. |
| __Build Requirements:__ | OSX 10.11 SDK |
| __Runtime Requirements:__ | OSX 10.11 |

30-Bit Color is now supported on the Mac Pro (Late 2013), iMac (Retina 5K, 27-inch, Late 2014), and iMac (Retina 5K, 27-inch, Late 2015). The frame buffer of these Macs has a depth of 10 bits per color component, allowing apps to display graphics and imagery with more than 256 color gradations per component.

When a window’s color depth limit is set to 64-bit (RGBA 16-16-16-16), a specialized dither pattern is automatically applied to the window’s content as it is composited into the 8-bits per color channel frame buffer. This dithering minimizes the appearance of quantization artifacts on screen. Using the technique demonstrated by the sample you can also display 32-bit "deep" formats like 10-10-10-2 RGBX (or 2-10-10-10 XRGB).

[Next](Sources-main.mm.md)

