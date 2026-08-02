---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_MovieRecorder_h.html
archived_at: '2026-07-18T03:27:53.882560Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-VideoSnakeAppDelegate.m.md)[Previous](Classes-ShaderUtilities.h.md)

# Classes/MovieRecorder.h

```objc
/*
 <codex>
 <abstract>Real-time movie recorder which is totally non-blocking</abstract>
 </codex>
 */

#import <Foundation/Foundation.h>

#import <CoreMedia/CMFormatDescription.h>
#import <CoreMedia/CMSampleBuffer.h>

@protocol MovieRecorderDelegate;

@interface MovieRecorder : NSObject

- (id)initWithURL:(NSURL *)URL;

// Only one audio and video track each are allowed.
- (void)addVideoTrackWithSourceFormatDescription:(CMFormatDescriptionRef)formatDescription transform:(CGAffineTransform)transform;
- (void)addAudioTrackWithSourceFormatDescription:(CMFormatDescriptionRef)formatDescription;

- (void)setDelegate:(id<MovieRecorderDelegate>)delegate callbackQueue:(dispatch_queue_t)delegateCallbackQueue; // delegate is weak referenced

- (void)prepareToRecord; // Asynchronous, might take several hunderd milliseconds. When finished the delegate's recorderDidFinishPreparing: or recorder:didFailWithError: method will be called.

- (void)appendVideoSampleBuffer:(CMSampleBufferRef)sampleBuffer;
- (void)appendVideoPixelBuffer:(CVPixelBufferRef)pixelBuffer withPresentationTime:(CMTime)presentationTime;
- (void)appendAudioSampleBuffer:(CMSampleBufferRef)sampleBuffer;

- (void)finishRecording; // Asynchronous, might take several hundred milliseconds. When finished the delegate's recorderDidFinishRecording: or recorder:didFailWithError: method will be called.

@end

@protocol MovieRecorderDelegate <NSObject>
@required
- (void)movieRecorderDidFinishPreparing:(MovieRecorder *)recorder;
- (void)movieRecorder:(MovieRecorder *)recorder didFailWithError:(NSError *)error;
- (void)movieRecorderDidFinishRecording:(MovieRecorder *)recorder;
@end
```

[Next](Classes-VideoSnakeAppDelegate.m.md)[Previous](Classes-ShaderUtilities.h.md)

