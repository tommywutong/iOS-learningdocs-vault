---
title: TextureUpload
apple_id: DTS40009988
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2010-05-19'
source_url: https://developer.apple.com/library/archive/samplecode/TextureUpload/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:26:45.025711Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextureUpload](TextureUpload.md)


[Next](main.m.md)[Previous](TextureUpload.md)

# ReadMe.txt

```
TextureUpload

===========================================================================
DESCRIPTION:

This sample code demonstrates the fundamental techniques to obtain optimal 
texture upload performance. There are two levels of optimizations here:

- The Apple Client Storage extension allows you to eliminate a texture copy 
at the client. 

- When working with non-power-of-two texture target (GL_TEXTURE_RECTANGLE_EXT), 
you may use the Rectangle Texture extension and the Apple Texture Range 
extension to further optimize texture upload performance.

Note, the first level of optimization applies to both GL_TEXTURE_2D and 
GL_TEXTURE_RECTANGLE_EXT targets; the second level of optimization applies to 
the GL_TEXTURE_RECTANGLE_EXT target only.

See the OpenGL Programming Guide for Mac OS X for more information, in 
particular, the chapter of "Best Practices for Working with Texture Data".

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.6 or later, Xcode 3.1 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.6 or later

===========================================================================
PACKAGING LIST:

MyOpenGLView.h
MyOpenGLView.m

The MyOpenGLView class is an NSOpenGLView subclass, which defines the view 
object that handles 3D OpenGL drawing.

===========================================================================
Copyright (C) 2010 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](TextureUpload.md)

