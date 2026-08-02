---
title: 'AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback'
apple_id: TP40016165
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/AVMetadataRecordPlay/Listings/Objective_C_AVMetadataRecordPlay_AVMetadataRecordPlayCameraPreviewView_m.html
archived_at: '2026-07-18T03:00:19.877722Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVMetadataRecordPlay: Timed Metadata Capture Recording and Playback](AVMetadataRecordPlay-%20Timed%20Metadata%20Capture%20Recording%20and%20Playback.md)


[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlay%2BUICollectionView%2BConvenien.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayCameraViewController.h.md)

# Objective-C/AVMetadataRecordPlay/AVMetadataRecordPlayCameraPreviewView.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Camera preview view.
*/

@import AVFoundation;

#import "AVMetadataRecordPlayCameraPreviewView.h"

@implementation AVMetadataRecordPlayCameraPreviewView

+ (Class)layerClass
{
    return [AVCaptureVideoPreviewLayer class];
}

- (AVCaptureVideoPreviewLayer *)videoPreviewLayer
{
    return (AVCaptureVideoPreviewLayer *)self.layer;
}

- (AVCaptureSession *)session
{
    return self.videoPreviewLayer.session;
}

- (void)setSession:(AVCaptureSession *)session
{
    self.videoPreviewLayer.session = session;
}

@end
```

[Next](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlay%2BUICollectionView%2BConvenien.md)[Previous](Objective-C-AVMetadataRecordPlay-AVMetadataRecordPlayCameraViewController.h.md)

