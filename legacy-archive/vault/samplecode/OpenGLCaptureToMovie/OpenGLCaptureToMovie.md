---
title: OpenGLCaptureToMovie
apple_id: DTS10004445
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2007-08-30'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGLScreenCapture/Introduction/Intro.html
archived_at: '2026-07-18T03:18:09.428931Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

Relevant replacement documents include:

- Technical Q&A _[How to capture screen activity to a movie file using AV Foundation on OS X 10.7 Lion and later](https://developer.apple.com/library/archive/qa/qa1740/_index.html#//apple_ref/doc/uid/DTS40011007)_

# OpenGLCaptureToMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-08-30 How to capture the screen on Mac OS X using OpenGL and save to a QuickTime movie. |
| __Build Requirements:__ | Mac OS X 10.4, Xcode 2.4 |
| __Runtime Requirements:__ | Mac OS X 10.4, QuickTime 7 |

Demonstrates how to capture the screen on Mac OS X using OpenGL. The sample shows how to grab frames using asynchronous texture fetching, a technique which is more complicated but offers better performance than synchronous capture using glReadPixels.

When performing asynchronous texture fetching, the resulting capture is saved to a movie file. Compression of the actual frames for the destination movie file is performed simultaneously with the capture but on a separate thread for better performance.

[Next](main.m.md)

