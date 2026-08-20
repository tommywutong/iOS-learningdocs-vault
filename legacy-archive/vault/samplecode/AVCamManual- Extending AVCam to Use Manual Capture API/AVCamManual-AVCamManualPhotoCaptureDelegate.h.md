---
title: 'AVCamManual: Extending AVCam to Use Manual Capture API'
apple_id: TP40014578
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-15'
source_url: https://developer.apple.com/library/archive/samplecode/AVCamManual/Listings/AVCamManual_AVCamManualPhotoCaptureDelegate_h.html
archived_at: '2026-07-18T03:00:02.745251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCamManual: Extending AVCam to Use Manual Capture API](AVCamManual-%20Extending%20AVCam%20to%20Use%20Manual%20Capture%20API.md)


[Next](AVCamManual-AVCamManualCameraViewController.h.md)[Previous](AVCamManual-AVCamManualPreviewView.h.md)

# AVCamManual/AVCamManualPhotoCaptureDelegate.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Photo capture delegate.
*/

@import AVFoundation;

@interface AVCamManualPhotoCaptureDelegate : NSObject<AVCapturePhotoCaptureDelegate>

- (instancetype)initWithRequestedPhotoSettings:(AVCapturePhotoSettings *)requestedPhotoSettings willCapturePhotoAnimation:(void (^)())willCapturePhotoAnimation completed:(void (^)( AVCamManualPhotoCaptureDelegate *photoCaptureDelegate ))completed;

@property (nonatomic, readonly) AVCapturePhotoSettings *requestedPhotoSettings;

@end
```

[Next](AVCamManual-AVCamManualCameraViewController.h.md)[Previous](AVCamManual-AVCamManualPreviewView.h.md)

