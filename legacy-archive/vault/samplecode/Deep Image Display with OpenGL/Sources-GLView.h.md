---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLView_h.html
archived_at: '2026-07-18T03:06:08.022598Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLShader.mm.md)[Previous](Sources-GLDIDAppDelegate.mm.md)

# Sources/GLView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom OpenGL view for the application.
 */

#import "IOSurface2D.h"

@interface GLView : NSOpenGLView

@property (nonatomic, retain, nullable) NSString* resource;
@property (nonatomic, retain, nullable) NSString* path;

@property (nonatomic, retain, nullable) NSURL* URL;

@property (nonatomic, retain, nullable) IOSurface2D* surface;

@property (nonatomic, readonly)  GLsizei width;
@property (nonatomic, readonly)  GLsizei height;

@end
```

[Next](Sources-GLShader.mm.md)[Previous](Sources-GLDIDAppDelegate.mm.md)

