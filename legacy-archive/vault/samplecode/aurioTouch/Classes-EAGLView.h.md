---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_EAGLView_h.html
archived_at: '2026-07-18T03:28:52.559729Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-aurioTouchAppDelegate.mm.md)[Previous](Classes-FFTHelper.h.md)

# Classes/EAGLView.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class wraps the CAEAGLLayer from CoreAnimation into a convenient UIView subclass

 */

// Framework includes
#import <UIKit/UIKit.h>
#import <QuartzCore/QuartzCore.h>
#import <OpenGLES/EAGL.h>
#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>

// Local includes
#import "AudioController.h"

@interface EAGLView : UIView

@property (assign)  BOOL applicationResignedActive;

- (void)startAnimation;
- (void)stopAnimation;

@end
```

[Next](Classes-aurioTouchAppDelegate.mm.md)[Previous](Classes-FFTHelper.h.md)

