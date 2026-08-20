---
title: ShadingWinds
apple_id: DTS10000613
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/ShadingWinds/Introduction/Intro.html
archived_at: '2026-07-18T03:23:42.706486Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ShadingWinds.c.md)

# ShadingWinds

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This little application includes code to allow you to detect whether or not the Shell Window is "rolled up" by WindowShade. How do you do this? You check the window's contRgn. If the contRgn is empty, then the window is shaded. You'll note that the grafPort is unchanged by WindowShade, so if you need to save window dimensions, you can grab that information from the portRect.

[Next](ShadingWinds.c.md)

