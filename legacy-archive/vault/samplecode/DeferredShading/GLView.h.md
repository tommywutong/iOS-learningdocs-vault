---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/GLView_h.html
archived_at: '2026-07-18T03:06:11.242975Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](DeferredShadingAppDelegate.m.md)[Previous](LICENSE.txt.md)

# GLView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The OpenGL view. It delegates to the renderer class for drawing.
 */


#import <Cocoa/Cocoa.h>
#import <QuartzCore/QuartzCore.h>

class OpenGLRenderer;

typedef struct _CallbackContext
{
    NSOpenGLContext* ctx;
    OpenGLRenderer* renderer;
} CallbackContext;

@interface GLView : NSOpenGLView {
    CallbackContext* cbCtx;
    NSOpenGLPixelFormat* pf;
    CVDisplayLinkRef displayLink;
}

@end
```

[Next](DeferredShadingAppDelegate.m.md)[Previous](LICENSE.txt.md)

