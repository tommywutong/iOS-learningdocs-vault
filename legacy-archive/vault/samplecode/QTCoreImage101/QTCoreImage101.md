---
title: QTCoreImage101
apple_id: DTS10003719
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/QTCoreImage101/Introduction/Intro.html
archived_at: '2026-07-18T03:20:03.835184Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTCoreImage101

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2009-10-27 Updated project for 10.5 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzrhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.1.4+ |
| __Runtime Requirements:__ | Mac OS 10.5+, QuickTime 7.0+ |

QTCoreImage101 is a cocoa application demonstrating (using very little code) how to render a QuickTime Movie using Core Image filters and the new video pipeline. It is a good place to start for developers looking at Core Image, Core Video and Visual Contexts for the very first time.
In this sample we're using the following framework APIs:
QTKit is used to play back a QuickTime Movie.
QuickTime Visual Context is used as the drawing destination for the QuickTime Movie.
Core Image to add a filter to the video frame.
NSOpenGLView is used as our view, this is where we draw a video frame.
Core Video pipeline:
Movie -> Visual context -> Core Image Filter -> OpenGL rendering ----> Hardware
What is Core Image:
Core Image is an extensible architecture built into Mac OS X v10.4 for near real-time, pixel-accurate image processing of graphics as well as video.
What is Core Video:
Core Video delivers a modern foundation for video services providing a bridge between QuickTime and the GPU for hardware-accelerated video processing. This highly optimized pipeline for video presentation increases performance and reduces CPU load, freeing up resources for other operations.

[Next](main.m.md)

