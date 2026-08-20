---
title: StopNGo for iOS
apple_id: DTS40011123
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/samplecode/StopNGo/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:25:46.280195Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StopNGo for iOS](StopNGo%20for%20iOS.md)


[Next](StopNGo-main.m.md)[Previous](StopNGo%20for%20iOS.md)

# ReadMe.txt

```
### StopNGo ###

===========================================================================
DESCRIPTION:

StopNGo is a simple stop-motion animation QuickTime movie recorder that uses AVFoundation.

It creates a AVCaptureSession, AVCaptureDevice, AVCaptureVideoPreviewLayer, and AVCaptureStillImageOutput to preview and capture still images from a video capture device, then re-times each sample buffer to a frame rate of 5 fps and writes frames to disk using AVAssetWriter.

A frame rate of 5 fps means that 5 still images will result in a 1 second long movie. This value is hard coded in the sample but may be changed as required by the developer.

===========================================================================
BUILD REQUIREMENTS:

Xcode 4.2 or later; iPhone iOS SDK 5.0 or later.

===========================================================================
RUNTIME REQUIREMENTS:

iOS 5.0 or later. This app will not produce camera output on the iOS simulator.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0 First version.

===========================================================================
Copyright (C) 2011 Apple Inc. All rights reserved.
```

[Next](StopNGo-main.m.md)[Previous](StopNGo%20for%20iOS.md)

