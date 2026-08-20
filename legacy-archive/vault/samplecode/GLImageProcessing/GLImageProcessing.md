---
title: GLImageProcessing
apple_id: DTS40009053
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2014-03-25'
source_url: https://developer.apple.com/library/archive/samplecode/GLImageProcessing/Introduction/Intro.html
archived_at: '2026-07-18T03:10:08.118058Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# GLImageProcessing

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2014-03-25 Removed warnings. Updated for 64-bit. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 4.0 SDK |
| __Runtime Requirements:__ | iPhone OS 3.2 or later |

The GLImageProcessing sample application demonstrates how to implement simple image processing filters (Brightness, Contrast, Saturation, Hue rotation, Sharpness) using OpenGL ES1.1. The sample also shows how to create simple procedural button icons using CoreGraphics.

By looking at the code you'll see how to set up an OpenGL ES view and use it for applying a filter to a texture. The application creates a texture from an image loaded from disk. It pads the image to a power of two, if required by the GPU.

The Debug configuration in the Xcode project defines DEBUG and ASSERT preprocessor macros, to enable additional error checking.

To use this sample, open it in Xcode and click Build and Go. Use the slider to control the current filter. Only a single filter is applied at a time.

[Next](ReadMe.txt.md)

