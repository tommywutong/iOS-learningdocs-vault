---
title: VertexPerformanceDemo
apple_id: DTS10003726
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenGL
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/VertexPerformanceDemo/Listings/Textures_h.html
archived_at: '2026-07-18T03:27:48.382346Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VertexPerformanceDemo](VertexPerformanceDemo.md)


[Next](Textures.m.md)[Previous](newave.m.md)

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

[Next](Textures.m.md)[Previous](newave.m.md)

