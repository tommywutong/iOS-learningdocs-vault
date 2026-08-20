---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_OpenGLPixelBufferView_h.html
archived_at: '2026-07-18T03:27:54.098957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-MovieRecorder.m.md)[Previous](Classes-VideoSnakeAppDelegate.m.md)

# Classes/OpenGLPixelBufferView.h

```objc
/*
 <codex>
 <abstract>The OpenGL ES view.</abstract>
 </codex>
 */
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <CoreVideo/CoreVideo.h>

@interface OpenGLPixelBufferView : UIView

- (void)displayPixelBuffer:(CVPixelBufferRef)pixelBuffer;
- (void)flushPixelBufferCache;
- (void)reset;

@end
```

[Next](Classes-MovieRecorder.m.md)[Previous](Classes-VideoSnakeAppDelegate.m.md)

