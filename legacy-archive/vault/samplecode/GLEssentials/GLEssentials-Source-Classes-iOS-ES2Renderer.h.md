---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_iOS_ES2Renderer_h.html
archived_at: '2026-07-18T03:10:03.280791Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Classes-iOS-AppDelegate.m.md)[Previous](GLEssentials-Source-Classes-OSX-GLEssentialsFullscreenWindow.h.md)

# GLEssentials/Source/Classes/iOS/ES2Renderer.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The main rendering code.
 */

#import <QuartzCore/QuartzCore.h>

#import <OpenGLES/EAGL.h>
#import <OpenGLES/EAGLDrawable.h>
#import "OpenGLRenderer.h"

@interface ES2Renderer : OpenGLRenderer
{

}

- (instancetype)initWithContext:(EAGLContext*)context AndDrawable:(id<EAGLDrawable>)drawable;
- (void)render;
- (BOOL)resizeFromLayer:(CAEAGLLayer*)layer;

@end
```

[Next](GLEssentials-Source-Classes-iOS-AppDelegate.m.md)[Previous](GLEssentials-Source-Classes-OSX-GLEssentialsFullscreenWindow.h.md)

