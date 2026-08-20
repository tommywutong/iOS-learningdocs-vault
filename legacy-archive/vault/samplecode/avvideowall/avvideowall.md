---
title: avvideowall
apple_id: DTS40011122
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/avvideowall/Introduction/Intro.html
archived_at: '2026-07-18T03:28:59.703395Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# avvideowall

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2011-08-25 First public release. |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

avvideowall demonstrates the flexibility of AV Foundation capture on Lion. It is a command line application that creates a wall of AVCaptureVideoPreviewLayers, 4 per capture device in a mirrored square, and sends them flying around the screen. The sample demonstrates how to create a complex AVCaptureSession consisting of multiple AVCaptureVideoDeviceInputs and multiple AVCaptureVideoPreviewLayers, and how to connect the correct inputs to the desired layers.

This sample does not use Automatic Reference Counting. To build, disable ARC in the Xcode project's Build Settings.

Usage: press space to spin/reset the video preview layers; press q/Q to quit

[Next](ReadMe.txt.md)

