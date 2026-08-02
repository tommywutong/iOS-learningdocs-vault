---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Utility_sourceUtil_h.html
archived_at: '2026-07-18T03:10:04.412254Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Utility-glUtil.h.md)[Previous](GLEssentials-Source-Utility-vectorUtil.h.md)

# GLEssentials/Source/Utility/sourceUtil.h

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Functions for loading source files for shaders.
 */


#ifndef __SOURCE_UTIL_H__
#define __SOURCE_UTIL_H__

#include "glUtil.h"

typedef struct demoSourceRec
{
    GLchar* string;

    GLsizei byteSize;

    GLenum shaderType; // Vertex or Fragment

} demoSource;

demoSource* srcLoadSource(const char* filepathname);

void srcDestroySource(demoSource* source);

#endif // __SOURCE_UTIL_H__
```

[Next](GLEssentials-Source-Utility-glUtil.h.md)[Previous](GLEssentials-Source-Utility-vectorUtil.h.md)

