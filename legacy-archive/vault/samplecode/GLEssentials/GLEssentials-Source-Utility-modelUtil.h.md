---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Utility_modelUtil_h.html
archived_at: '2026-07-18T03:10:04.286615Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Utility-imageUtil.m.md)[Previous](GLEssentials-Source-Utility-matrixUtil.h.md)

# GLEssentials/Source/Utility/modelUtil.h

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Functions for loading a model file for vertex arrays.  The model file
  format used is a simple "binary blob" invented for the purpose of this sample code.
 */

#ifndef __MODEL_UTIL_H__
#define __MODEL_UTIL_H__

#include "glUtil.h"

typedef struct demoModelRec
{
    GLuint numVertcies;

    GLubyte *positions;
    GLenum positionType;
    GLuint positionSize;
    GLsizei positionArraySize;

    GLubyte *texcoords;
    GLenum texcoordType;
    GLuint texcoordSize;
    GLsizei texcoordArraySize;

    GLubyte *normals;
    GLenum normalType;
    GLuint normalSize;
    GLsizei normalArraySize;

    GLubyte *elements;
    GLenum elementType;
    GLuint numElements;
    GLsizei elementArraySize;

    GLenum primType;

} demoModel;

demoModel* mdlLoadModel(const char* filepathname);

demoModel* mdlLoadQuadModel();

void mdlDestroyModel(demoModel* model);

#endif //__MODEL_UTIL_H__
```

[Next](GLEssentials-Source-Utility-imageUtil.m.md)[Previous](GLEssentials-Source-Utility-matrixUtil.h.md)

