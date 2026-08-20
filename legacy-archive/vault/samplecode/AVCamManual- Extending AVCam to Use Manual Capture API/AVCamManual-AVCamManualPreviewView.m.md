---
title: 'AVCamManual: Extending AVCam to Use Manual Capture API'
apple_id: TP40014578
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-15'
source_url: https://developer.apple.com/library/archive/samplecode/AVCamManual/Listings/AVCamManual_AVCamManualPreviewView_m.html
archived_at: '2026-07-18T03:00:02.928858Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCamManual: Extending AVCam to Use Manual Capture API](AVCamManual-%20Extending%20AVCam%20to%20Use%20Manual%20Capture%20API.md)


[Next](AVCamManual-AVCamManualPhotoCaptureDelegate.m.md)[Previous](AVCamManual-AVCamManualCameraViewController.m.md)

# AVCamManual/AVCamManualPreviewView.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Camera preview.
*/

@import AVFoundation;

#import "AVCamManualPreviewView.h"

@implementation AVCamManualPreviewView

+ (Class)layerClass
{
    return [AVCaptureVideoPreviewLayer class];
}

- (AVCaptureSession *)session
{
    AVCaptureVideoPreviewLayer *previewLayer = (AVCaptureVideoPreviewLayer *)self.layer;
    return previewLayer.session;
}

- (void)setSession:(AVCaptureSession *)session
{
    AVCaptureVideoPreviewLayer *previewLayer = (AVCaptureVideoPreviewLayer *)self.layer;
    previewLayer.session = session;
}

@end
```

[Next](AVCamManual-AVCamManualPhotoCaptureDelegate.m.md)[Previous](AVCamManual-AVCamManualCameraViewController.m.md)

