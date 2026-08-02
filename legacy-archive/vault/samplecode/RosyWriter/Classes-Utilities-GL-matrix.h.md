---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Classes_Utilities_GL_matrix_h.html
archived_at: '2026-07-18T03:22:20.615732Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Classes-Utilities-GL-ShaderUtilities.c.md)[Previous](Classes-Utilities-OpenGLPixelBufferView.m.md)

# Classes/Utilities/GL/matrix.h

```

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple 4x4 matrix computations
 */

#ifndef MATRIX_H
#define MATRIX_H

void mat4f_LoadIdentity(float* m);
void mat4f_LoadScale(float* s, float* m);

void mat4f_LoadXRotation(float radians, float* mout);
void mat4f_LoadYRotation(float radians, float* mout);
void mat4f_LoadZRotation(float radians, float* mout);

void mat4f_LoadTranslation(float* t, float* mout);

void mat4f_LoadPerspective(float fov_radians, float aspect, float zNear, float zFar, float* mout);
void mat4f_LoadOrtho(float left, float right, float bottom, float top, float near, float far, float* mout);

void mat4f_MultiplyMat4f(const float* a, const float* b, float* mout);

#endif /* MATRIX_H */
```

[Next](Classes-Utilities-GL-ShaderUtilities.c.md)[Previous](Classes-Utilities-OpenGLPixelBufferView.m.md)

