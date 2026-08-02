---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_VideoSnakeOpenGLRenderer_h.html
archived_at: '2026-07-18T03:27:54.404897Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-VideoSnakeAppDelegate.h.md)[Previous](Classes-VideoSnakeViewController.m.md)

# Classes/VideoSnakeOpenGLRenderer.h

```objc
/*
 <codex>
 <abstract>The VideoSnake OpenGL effect renderer.</abstract>
 </codex>
 */
#import <Foundation/Foundation.h>
#import <CoreMedia/CoreMedia.h>
#import <CoreVideo/CoreVideo.h>
#import <CoreMotion/CoreMotion.h>

@interface VideoSnakeOpenGLRenderer : NSObject

- (void)prepareWithOutputDimensions:(CMVideoDimensions)outputDimensions retainedBufferCountHint:(size_t)retainedBufferCountHint;
- (void)reset;

- (CVPixelBufferRef)copyRenderedPixelBuffer:(CVPixelBufferRef)pixelBuffer motion:(CMDeviceMotion *)motion;

@property(nonatomic, assign) BOOL shouldMirrorMotion;
@property(nonatomic, readonly) CMFormatDescriptionRef __attribute__((NSObject)) outputFormatDescription; // non-NULL once the renderer has been prepared

@end
```

[Next](Classes-VideoSnakeAppDelegate.h.md)[Previous](Classes-VideoSnakeViewController.m.md)

