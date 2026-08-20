---
title: SquareCam
apple_id: DTS40011190
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-04-04'
source_url: https://developer.apple.com/library/archive/samplecode/SquareCam/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:25:29.677495Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SquareCam](SquareCam.md)


[Next](SquareCam-main.m.md)[Previous](SquareCam.md)

# ReadMe.txt

```
### SquareCam ###

===========================================================================
DESCRIPTION:

SquareCam demonstrates improvements to the AVCaptureStillImageOutput class in iOS 5, highlighting the following features:
- KVO observation of the @"capturingStillImage" property to know when to perform an animation
- Use of setVideoScaleAndCropFactor: to achieve a "digital zoom" effect on captured images
- Switching between front and back cameras while showing a real-time preview
- Integrating with CoreImage's new CIFaceDetector to find faces in a real-time VideoDataOutput, as well as in a captured still image.
     Found faces are indicated with a red square.
- Overlaid square is rotated appropriately for the 4 supported device rotations.
===========================================================================
BUILD REQUIREMENTS:

Xcode 4.2 or later; iPhone iOS SDK 5.0 or later.

===========================================================================
RUNTIME REQUIREMENTS:

iOS 5.0 or later. This app will not deliver any camera output on the iOS simulator.

===========================================================================
APIs USED:

ALAssetsLibrary - to write to the photos library
AVFoundation
AVCaptureConnection
AVCaptureDevice
AVCaptureDeviceInput
AVCaptureSession
AVCaptureStillImageOutput
AVCaptureVideoDataOutput
AVCaptureVideoPreviewLayer
CoreImage
CIFaceDetector
===========================================================================
Copyright (C) 2011 Apple Inc. All rights reserved.
```

[Next](SquareCam-main.m.md)[Previous](SquareCam.md)

