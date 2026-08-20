---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLProgram_h.html
archived_at: '2026-07-18T03:06:07.263968Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-Quad2D.vs.md)[Previous](Sources-GLQuad.h.md)

# Sources/GLProgram.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a program object.
 */

#import <OpenGL/OpenGL.h>

@interface GLProgram : NSObject

// Attach shaders, in an ascending order, starting at index 0
@property (nonatomic, setter=attach:) GLuint shader;

// Bind attributes, in an ascending order, starting at index 0
@property (nonatomic, nullable, setter=bind:) const GLchar* attribute;

// Bind/unbind the program
@property (nonatomic, setter=program:) BOOL use;

// Program id
@property (nonatomic, readonly) GLuint pid;

// Link shaders and create the program object
- (BOOL) link;

@end
```

[Next](Sources-Quad2D.vs.md)[Previous](Sources-GLQuad.h.md)

