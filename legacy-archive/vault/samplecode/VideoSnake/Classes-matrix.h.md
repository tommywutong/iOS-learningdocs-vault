---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_matrix_h.html
archived_at: '2026-07-18T03:27:55.138962Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-ShaderUtilities.c.md)[Previous](Classes-VideoSnakeAppDelegate.h.md)

# Classes/matrix.h

```

/*
 <codex>
 <abstract>Simple 4x4 matrix computations</abstract>
 </codex>
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

[Next](Classes-ShaderUtilities.c.md)[Previous](Classes-VideoSnakeAppDelegate.h.md)

