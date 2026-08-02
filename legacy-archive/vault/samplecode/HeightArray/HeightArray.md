---
title: HeightArray
apple_id: DTS40010103
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/HeightArray/Introduction/Intro.html
archived_at: '2026-07-18T03:11:47.322338Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# HeightArray

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2014-06-17 Updated with Core Profile and GLKit Math Utilities. Moved shader setup to -prepareOpenGL to ensure that the OpenGL framebuffer is valid at the time and thus avoid validation failure. Cleaned up code and removed Static Analyzer warnings. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamjqgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.9 or later, Xcode 5.0 or later |
| __Runtime Requirements:__ | OS X v10.7 or later |

The EXT_TEXTURE_ARRAY extension introduces the notion of one and two-dimensional texture array, which is a collection of one and two-dimensional images of identical size and format, arranged in layers. This sample provides an example of two-dimensional texture array. It visualizes a terrain by using terrain's Z-coordinate to index into a texture array and applies the correct image for that point's elevation.

Usage: Move your mouse around to view the terrain from different camera angles.

[Next](Readme.txt.md)

