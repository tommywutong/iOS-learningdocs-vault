---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_CubePlayback_h.html
archived_at: '2026-07-18T03:09:49.769377Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-MainViewController.h.md)[Previous](GLAirPlay-GLView.m.md)

# GLAirPlay/CubePlayback.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An Obj-C class which wraps an OpenAL playback environment
 */

#import <UIKit/UIKit.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>

@interface CubePlayback : NSObject

@property           BOOL isPlaying; // Whether the sound is playing or stopped
@property           BOOL wasInterrupted; // Whether playback was interrupted by the system
@property           float* sourcePos; // The coordinates of the sound source
@property           float* listenerPos; // The coordinates of the listener
@property           float listenerRotation; // The rotation angle of the listener in radians

- (void)initOpenAL;
- (void)teardownOpenAL;

- (void)startSound;
- (void)stopSound;

@end
```

[Next](GLAirPlay-MainViewController.h.md)[Previous](GLAirPlay-GLView.m.md)

