---
title: Using AVFoundation APIs to record a movie with location metadata
apple_id: TP40014494
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCaptureLocation/Listings/AVCaptureLocation_AAPLCaptureManager_h.html
archived_at: '2026-07-18T03:00:03.356270Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVFoundation APIs to record a movie with location metadata](Using%20AVFoundation%20APIs%20to%20record%20a%20movie%20with%20location%20metadata.md)


[Next](AVCaptureLocation-AAPLAppDelegate.m.md)[Previous](AVCaptureLocation-main.m.md)

# AVCaptureLocation/AAPLCaptureManager.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  This class creates and manages the AV capture session and CLLocationManager, to gather location data, and writes out this data using asset writer. 

 */

@import Foundation;
@import AVFoundation;

@protocol AAPLCaptureManagerDelegate;

@interface AAPLCaptureManager : NSObject

@property (assign) id <AAPLCaptureManagerDelegate>  delegate;
@property (readonly) AVCaptureSession               *session;
@property (readonly, getter=isRecording) BOOL       recording;
@property AVCaptureVideoOrientation                 referenceOrientation;
@property CGFloat                                   distanceUpdateInMeters;

- (void)setupAndStartCaptureSession;
- (void)stopAndTearDownCaptureSession;

- (void)startRecording;
- (void)stopRecording;

- (void)pauseCaptureSession; // Pausing while a recording is in progress will cause the recording to be stopped and saved.
- (void)resumeCaptureSession;

@end

@protocol AAPLCaptureManagerDelegate <NSObject>

@required
- (void)recordingWillStart;
- (void)recordingDidStart;
- (void)recordingWillStop;
- (void)recordingDidStop;
- (void)newLocationUpdate:(NSString *)locationDescription;

@end
```

[Next](AVCaptureLocation-AAPLAppDelegate.m.md)[Previous](AVCaptureLocation-main.m.md)

