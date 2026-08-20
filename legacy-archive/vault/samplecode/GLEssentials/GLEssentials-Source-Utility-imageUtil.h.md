---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Utility_imageUtil_h.html
archived_at: '2026-07-18T03:10:03.554484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Utility-vectorUtil.c.md)[Previous](GLEssentials-Source-Readme.md.md)

# GLEssentials/Source/Utility/imageUtil.h

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Functions for loading an image files for textures.
 */


#ifndef __IMAGE_UTIL_H__
#define __IMAGE_UTIL_H__

#include "glUtil.h"

typedef struct demoImageRec
{
    GLubyte* data;

    GLsizei size;

    GLuint width;
    GLuint height;
    GLenum format;
    GLenum type;

    GLuint rowByteSize;

} demoImage;

demoImage* imgLoadImage(const char* filepathname, int flipVertical);

void imgDestroyImage(demoImage* image);

#endif //__IMAGE_UTIL_H__
```

[Next](GLEssentials-Source-Utility-vectorUtil.c.md)[Previous](GLEssentials-Source-Readme.md.md)

