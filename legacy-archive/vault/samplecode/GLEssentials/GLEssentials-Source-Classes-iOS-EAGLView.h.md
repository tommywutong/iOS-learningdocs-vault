---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_iOS_EAGLView_h.html
archived_at: '2026-07-18T03:10:03.149871Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Classes-iOS-AppDelegate.h.md)[Previous](GLEssentials-Source-Classes-iOS-AppDelegate.m.md)

# GLEssentials/Source/Classes/iOS/EAGLView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The EAGLView class is a UIView subclass that renders OpenGL scene.
*/

#import <UIKit/UIKit.h>

#import "ES2Renderer.h"

// This class wraps the CAEAGLLayer from CoreAnimation into a convenient UIView subclass.
// The view content is basically an EAGL surface you render your OpenGL scene into.
// Note that setting the view non-opaque will only work if the EAGL surface has an alpha channel.
@interface EAGLView : UIView

@property (readonly, nonatomic, getter=isAnimating) BOOL animating;
@property (nonatomic) NSInteger animationFrameInterval;

- (void) startAnimation;
- (void) stopAnimation;
- (void) drawView:(id)sender;

@end
```

[Next](GLEssentials-Source-Classes-iOS-AppDelegate.h.md)[Previous](GLEssentials-Source-Classes-iOS-AppDelegate.m.md)

