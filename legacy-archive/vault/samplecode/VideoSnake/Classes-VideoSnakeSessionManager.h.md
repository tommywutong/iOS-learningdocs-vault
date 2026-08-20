---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_VideoSnakeSessionManager_h.html
archived_at: '2026-07-18T03:27:54.641040Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-MotionSynchronizer.h.md)[Previous](Classes-MotionSynchronizer.m.md)

# Classes/VideoSnakeSessionManager.h

```objc
/*
 <codex>
 <abstract>The class that creates and manages the AVCaptureSession</abstract>
 </codex>
 */

#import <AVFoundation/AVFoundation.h>
#import <CoreMotion/CoreMotion.h>

@protocol VideoSnakeSessionManagerDelegate;

@interface VideoSnakeSessionManager : NSObject 

- (void)setDelegate:(id<VideoSnakeSessionManagerDelegate>)delegate callbackQueue:(dispatch_queue_t)delegateCallbackQueue; // delegate is weak referenced

// Consider renaming this class VideoSnakeCapturePipeline
// These methods are synchronous
- (void)startRunning;
- (void)stopRunning;

// Must be running before starting recording
// These methods are asynchronous, see the recording delegate callbacks
- (void)startRecording;
- (void)stopRecording;

@property (readwrite) BOOL renderingEnabled; // When set to false the GPU will not be used after the setRenderingEnabled: call returns.

@property (readwrite) AVCaptureVideoOrientation recordingOrientation; // client can set the orientation for the recorded movie

- (CGAffineTransform)transformFromVideoBufferOrientationToOrientation:(AVCaptureVideoOrientation)orientation withAutoMirroring:(BOOL)mirroring; // only valid after startRunning has been called

// Stats
@property (readonly) float videoFrameRate;
@property (readonly) CMVideoDimensions videoDimensions;

@end

@protocol VideoSnakeSessionManagerDelegate <NSObject>
@required

- (void)sessionManager:(VideoSnakeSessionManager *)sessionManager didStopRunningWithError:(NSError *)error;

// Preview
- (void)sessionManager:(VideoSnakeSessionManager *)sessionManager previewPixelBufferReadyForDisplay:(CVPixelBufferRef)previewPixelBuffer;
- (void)sessionManagerDidRunOutOfPreviewBuffers:(VideoSnakeSessionManager *)sessionManager;

// Recording
- (void)sessionManagerRecordingDidStart:(VideoSnakeSessionManager *)manager;
- (void)sessionManager:(VideoSnakeSessionManager *)manager recordingDidFailWithError:(NSError *)error; // Can happen at any point after a startRecording call, for example: startRecording->didFail (without a didStart), willStop->didFail (without a didStop)
- (void)sessionManagerRecordingWillStop:(VideoSnakeSessionManager *)manager;
- (void)sessionManagerRecordingDidStop:(VideoSnakeSessionManager *)manager;

@end
```

[Next](Classes-MotionSynchronizer.h.md)[Previous](Classes-MotionSynchronizer.m.md)

