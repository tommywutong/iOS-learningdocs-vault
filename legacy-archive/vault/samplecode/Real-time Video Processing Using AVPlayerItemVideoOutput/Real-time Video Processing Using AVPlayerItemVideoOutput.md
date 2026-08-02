---
title: Real-time Video Processing Using AVPlayerItemVideoOutput
apple_id: DTS40013109
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-10-01'
source_url: https://developer.apple.com/library/archive/samplecode/AVBasicVideoOutput/Introduction/Intro.html
archived_at: '2026-07-18T03:00:01.171488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AVBasicVideoOutput-main.m.md)

# Real-time Video Processing Using AVPlayerItemVideoOutput

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2015-10-01 Change in build configuration. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmjqhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.6 or later, iOS 6 or later |
| __Runtime Requirements:__ | iOS 6 or later |

AVBasicVideoOutput demonstrates how to perform real-time video processing using AVPlayerItemVideoOutput and how to display processed video frames on screen using CAEAGLLayer and CADisplayLink. AVPlayerItemVideoOutput provides sample buffers (CVPixelBufferRef) which are then adjusted for their luma (Y) and chroma (UV) values based on the input from a user via UISliders. These processed pixel buffers are then rendered to a CAEAGLLayer.

[Next](AVBasicVideoOutput-main.m.md)

