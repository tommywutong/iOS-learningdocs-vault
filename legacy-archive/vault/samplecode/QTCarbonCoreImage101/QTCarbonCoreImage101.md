---
title: QTCarbonCoreImage101
apple_id: DTS10003878
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-02-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTCarbonCoreImage101/Introduction/Intro.html
archived_at: '2026-07-18T03:20:01.450210Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# QTCarbonCoreImage101

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-02-14 Demonstrates how to render QuickTime Movies using Core Image filters and the new video pipeline. |
| __Build Requirements:__ | Xcode 2.2.1, MacOSX10.4u.sdk |
| __Runtime Requirements:__ | Mac OS X 10.4.4, QuickTime 7.0.4 |

QTCarbonCoreImage101 is a Carbon application demonstrating (using very little code) how to render a QuickTime Movie using Core Image filters and the new video pipeline. It is a good place to start for Carbon developers looking at Core Image, Core Video and Visual Contexts for the very first time.
Developers interested in seeing a Cocoa version of this sample should examine QTCoreImage101.
In this sample we're using the following framework APIs:
Standard QuickTime APIs are used to play back a Movie.
AGL APIs are use to create an AGL context for rendering.
A QuickTime Visual Context is used as the drawing destination for the QuickTime Movie.
Core Image is used to add a filter and render the video frame.
Core Video pipeline:
Movie -> Visual context -> Core Image Filter -> OpenGL rendering ----> Hardware
What is Core Image:
Core Image is an extensible architecture built into Mac OS X v10.4 for near real-time, pixel-accurate image processing of graphics as well as video.
What is Core Video:
Core Video delivers a modern foundation for video services providing a bridge between QuickTime and the GPU for hardware-accelerated video processing. This highly optimized pipeline for video presentation increases performance and reduces CPU load, freeing up resources for other operations.

[Next](main.c.md)

