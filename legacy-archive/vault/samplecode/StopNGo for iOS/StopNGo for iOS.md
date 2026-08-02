---
title: StopNGo for iOS
apple_id: DTS40011123
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/samplecode/StopNGo/Introduction/Intro.html
archived_at: '2026-07-18T03:25:46.243230Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# StopNGo for iOS

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2011-10-12 First Version. |
| __Build Requirements:__ | Xcode 4.2 or later; iPhone iOS SDK 5.0 or later |
| __Runtime Requirements:__ | iOS 5.0 or later. This app will not produce camera output on the iOS simulator. |

StopNGo is a simple stop-motion animation QuickTime movie recorder that uses AVFoundation.

It creates a AVCaptureSession, AVCaptureDevice, AVCaptureVideoPreviewLayer, and AVCaptureStillImageOutput to preview and capture still images from a video capture device, then re-times each sample buffer to a frame rate of 5 fps and writes frames to disk using AVAssetWriter.

A frame rate of 5 fps means that 5 still images will result in a 1 second long movie. This value is hard coded in the sample but may be changed as required.

[Next](ReadMe.txt.md)

