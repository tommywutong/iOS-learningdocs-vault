---
title: SquareCam
apple_id: DTS40011190
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-04-04'
source_url: https://developer.apple.com/library/archive/samplecode/SquareCam/Introduction/Intro.html
archived_at: '2026-07-18T03:25:29.630600Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SquareCam

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2013-04-04 Editorial [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjzgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.2 or later, iOS 5 SDK or later |
| __Runtime Requirements:__ | iOS 5 or later |

SquareCam demonstrates improvements to the AVCaptureStillImageOutput class in iOS 5, highlighting the following features:

- KVO observation of the @"capturingStillImage" property to know when to perform an animation - Use of setVideoScaleAndCropFactor: to achieve a "digital zoom" effect on captured images - Switching between front and back cameras while showing a real-time preview - Integrating with CoreImage's new CIFaceDetector to find faces in a real-time VideoDataOutput, as well as in a captured still image. Found faces are indicated with a red square. - Overlaid square is rotated appropriately for the 4 supported device rotations.

Note: This sample will not deliver any camera output on the iOS simulator.

[Next](ReadMe.txt.md)

