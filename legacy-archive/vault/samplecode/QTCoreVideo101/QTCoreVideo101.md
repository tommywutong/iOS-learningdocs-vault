---
title: QTCoreVideo101
apple_id: DTS10003690
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2011-01-22'
source_url: https://developer.apple.com/library/archive/samplecode/QTCoreVideo101/Introduction/Intro.html
archived_at: '2026-07-18T03:20:04.342694Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTCoreVideo101

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.3, 2011-01-22 Updated for Xcode 3.2.5 and 10.6SDK [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrzgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.5+ |
| __Runtime Requirements:__ | Mac OS X 10.6, Mac OS X 10.6, QuickTime 7+ |

QTCoreVideo101 is a cocoa application demonstrating (in the least amount of code possible) how to render a QuickTime Movie using OpenGL and the new video pipeline. It is a good place to start for developers looking at OpenGL, Core Video and Visual Contexts for the very first time.

In this sample we're using the following framework APIs:

QTKit is used to play back a QuickTime Movie.

QuickTime Visual Context is used as the drawing destination for the QuickTime Movie.

NSOpenGLView is used as our view, this is where we draw a video frame on a teapot or quad.

Core Video pipeline:

Movie -> Visual context -> OpenGL transforms -> OpenGL rendering ----> Hardware

What is Core Video:

Core Video delivers a modern foundation for video services providing a bridge between QuickTime and the GPU for hardware-accelerated video processing. This highly optimized pipeline for video presentation increases performance and reduces CPU load, freeing up resources for other operations.

[Next](main.m.md)

