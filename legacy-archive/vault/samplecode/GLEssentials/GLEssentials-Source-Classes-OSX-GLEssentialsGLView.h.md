---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_OSX_GLEssentialsGLView_h.html
archived_at: '2026-07-18T03:10:01.790632Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Classes-OSX-GLEssentialsFullscreenWindow.m.md)[Previous](GLEssentials-Source-Classes-OSX-AppDelegate.m.md)

# GLEssentials/Source/Classes/OSX/GLEssentialsGLView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 OpenGL view subclass.
 */


#import <Cocoa/Cocoa.h>
#import <QuartzCore/CVDisplayLink.h>

#import "modelUtil.h"
#import "imageUtil.h"

@interface GLEssentialsGLView : NSOpenGLView {
    CVDisplayLinkRef displayLink;
}

@end
```

[Next](GLEssentials-Source-Classes-OSX-GLEssentialsFullscreenWindow.m.md)[Previous](GLEssentials-Source-Classes-OSX-AppDelegate.m.md)

