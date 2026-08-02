---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_MotionSynchronizer_h.html
archived_at: '2026-07-18T03:27:53.763181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-VideoSnakeOpenGLRenderer.m.md)[Previous](Classes-VideoSnakeSessionManager.h.md)

# Classes/MotionSynchronizer.h

```objc
/*
 <codex>
 <abstract>Synchronizes motion samples with media samples</abstract>
 </codex>
 */

#import <Foundation/Foundation.h>
#import <CoreMedia/CMSampleBuffer.h>
#import <CoreMedia/CMSync.h>

@class CMDeviceMotion;

@protocol MotionSynchronizationDelegate;

@interface MotionSynchronizer : NSObject

@property(nonatomic) int motionRate;
@property(nonatomic, retain) __attribute__((NSObject)) CMClockRef sampleBufferClock; // safe to update if you aren't concurrently calling appendSampleBufferForSynchronization:

- (void)start;
- (void)stop;

- (void)appendSampleBufferForSynchronization:(CMSampleBufferRef)sampleBuffer;
- (void)setSynchronizedSampleBufferDelegate:(id<MotionSynchronizationDelegate>)sampleBufferDelegate queue:(dispatch_queue_t)sampleBufferCallbackQueue;

@end

@protocol MotionSynchronizationDelegate <NSObject>

@required
- (void)motionSynchronizer:(MotionSynchronizer *)synchronizer didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer withMotion:(CMDeviceMotion*)motion;

@end
```

[Next](Classes-VideoSnakeOpenGLRenderer.m.md)[Previous](Classes-VideoSnakeSessionManager.h.md)

