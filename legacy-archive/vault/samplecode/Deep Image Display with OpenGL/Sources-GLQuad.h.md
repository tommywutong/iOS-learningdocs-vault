---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLQuad_h.html
archived_at: '2026-07-18T03:06:07.388181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLProgram.h.md)[Previous](Sources-NSTextFile.mm.md)

# Sources/GLQuad.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for rendering a textured quad.
 */

#import <OpenGL/OpenGL.h>

@interface GLQuad: NSObject

// Create a quad with view bounds.
- (nullable instancetype) initWithBounds:(const NSRect)bounds;

// Program object id
@property (nonatomic, readonly) GLuint pid;

// Vertex array object
@property (nonatomic, readonly) GLuint vao;

// Draw mode
@property (nonatomic, readonly) GLenum mode;

// Texture target
@property (nonatomic, readonly) GLenum target;

// Texture bounds
@property (nonatomic, readonly) NSRect bounds;

// Set the image size. For texture 2D the default coordinates are used.
// For texture rectangle you need to set the original image size.
@property (nonatomic) NSSize size;

// Render the textured quad
- (void) render:(const GLuint)texture;

@end
```

[Next](Sources-GLProgram.h.md)[Previous](Sources-NSTextFile.mm.md)

