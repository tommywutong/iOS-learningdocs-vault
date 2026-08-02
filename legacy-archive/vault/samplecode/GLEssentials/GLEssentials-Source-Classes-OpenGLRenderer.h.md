---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_OpenGLRenderer_h.html
archived_at: '2026-07-18T03:10:02.586187Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Readme.md.md)[Previous](GLEssentials-Source-Classes-iOS-EAGLView.m.md)

# GLEssentials/Source/Classes/OpenGLRenderer.h

```objc
 /*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The OpenGLRenderer class creates and draws objects.
  Most of the code is OS independent.
 */
#include "glUtil.h"
#import <Foundation/Foundation.h>

@interface OpenGLRenderer : NSObject 

@property (nonatomic) GLuint defaultFBOName;

- (instancetype) initWithDefaultFBO: (GLuint) defaultFBOName;
- (void) resizeWithWidth:(GLuint)width AndHeight:(GLuint)height;
- (void) render;
- (void) dealloc;

@end
```

[Next](GLEssentials-Source-Readme.md.md)[Previous](GLEssentials-Source-Classes-iOS-EAGLView.m.md)

