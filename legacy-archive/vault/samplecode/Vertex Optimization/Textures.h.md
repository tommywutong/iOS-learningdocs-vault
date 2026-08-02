---
title: Vertex Optimization
apple_id: DTS10000553
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/Vertex_Optimization/Listings/Textures_h.html
archived_at: '2026-07-18T03:27:49.935239Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Vertex Optimization](Vertex%20Optimization.md)


[Next](Textures.m.md)[Previous](PerfBarOpenGLView.m.md)

# Textures.h

```objc
/*
 *  Textures.h
 *  VertexPerformance
 *
 *  Created by Kent Miller on Tue Oct 29 2002.
 *  Copyright (c) 2002 Apple Computer. All rights reserved.
 *
 */

#import <Cocoa/Cocoa.h>
#import <OpenGL/gl.h>

#define kTextureUnitCount 8

void TextureFromNSImage(NSImage *image, GLuint *texID, GLuint * width,GLuint *height);
void StringToTexture( char * string, char * fontName, 
            int fontSize, GLuint *texID, GLuint texWidth, 
            GLuint texHeight, NSColor *color);
```

[Next](Textures.m.md)[Previous](PerfBarOpenGLView.m.md)

