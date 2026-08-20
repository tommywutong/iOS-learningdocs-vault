---
title: 'AVCamManual: Extending AVCam to Use Manual Capture API'
apple_id: TP40014578
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-15'
source_url: https://developer.apple.com/library/archive/samplecode/AVCamManual/Listings/AVCamManual_AVCamManualPreviewView_h.html
archived_at: '2026-07-18T03:00:02.871632Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCamManual: Extending AVCam to Use Manual Capture API](AVCamManual-%20Extending%20AVCam%20to%20Use%20Manual%20Capture%20API.md)


[Next](AVCamManual-AVCamManualPhotoCaptureDelegate.h.md)[Previous](AVCamManual-AVCamManualPhotoCaptureDelegate.m.md)

# AVCamManual/AVCamManualPreviewView.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Camera preview.
*/

@import UIKit;

@class AVCaptureSession;

@interface AVCamManualPreviewView : UIView

@property (nonatomic) AVCaptureSession *session;

@end
```

[Next](AVCamManual-AVCamManualPhotoCaptureDelegate.h.md)[Previous](AVCamManual-AVCamManualPhotoCaptureDelegate.m.md)

