---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_matrix_c.html
archived_at: '2026-07-18T03:27:55.049167Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Resources-Shaders-videoSnake.vsh.md)[Previous](Classes-MovieRecorder.m.md)

# Classes/matrix.c

```c

/*
 <codex>
 <abstract>Simple 4x4 matrix computations</abstract>
 </codex>
 */

#include <string.h>
#include <math.h>
#include "matrix.h"

/*
 NOTE: These functions are created for your convenience but the matrix algorithms 
 are not optimized. You are encouraged to do additional research on your own to 
 implement a more robust numerical algorithm.
*/

void mat4f_LoadIdentity(float* m)
{
    m[0] = 1.0f;
    m[1] = 0.0f;
    m[2] = 0.0f;
    m[3] = 0.0f;

    m[4] = 0.0f;
    m[5] = 1.0f;
    m[6] = 0.0f;
    m[7] = 0.0f;

    m[8] = 0.0f;
    m[9] = 0.0f;
    m[10] = 1.0f;
    m[11] = 0.0f;   

    m[12] = 0.0f;
    m[13] = 0.0f;
    m[14] = 0.0f;
    m[15] = 1.0f;
}

// s is a 3D vector
void mat4f_LoadScale(float* s, float* m)
{
    m[0] = s[0];
    m[1] = 0.0f;
    m[2] = 0.0f;
    m[3] = 0.0f;

    m[4] = 0.0f;
    m[5] = s[1];
    m[6] = 0.0f;
    m[7] = 0.0f;

    m[8] = 0.0f;
    m[9] = 0.0f;
    m[10] = s[2];
    m[11] = 0.0f;   

    m[12] = 0.0f;
    m[13] = 0.0f;
    m[14] = 0.0f;
    m[15] = 1.0f;
}

void mat4f_LoadXRotation(float radians, float* m)
{
    float cosrad = cosf(radians);
    float sinrad = sinf(radians);

    m[0] = 1.0f;
    m[1] = 0.0f;
    m[2] = 0.0f;
    m[3] = 0.0f;

    m[4] = 0.0f;
    m[5] = cosrad;
    m[6] = sinrad;
    m[7] = 0.0f;

    m[8] = 0.0f;
    m[9] = -sinrad;
    m[10] = cosrad;
    m[11] = 0.0f;   

    m[12] = 0.0f;
    m[13] = 0.0f;
    m[14] = 0.0f;
    m[15] = 1.0f;
}

void mat4f_LoadYRotation(float radians, float* mout)
{
    float cosrad = cosf(radians);
    float sinrad = sinf(radians);

    mout[0] = cosrad;
    mout[1] = 0.0f;
    mout[2] = -sinrad;
    mout[3] = 0.0f;

    mout[4] = 0.0f;
    mout[5] = 1.0f;
    mout[6] = 0.0f;
    mout[7] = 0.0f;

    mout[8] = sinrad;
    mout[9] = 0.0f;
    mout[10] = cosrad;
    mout[11] = 0.0f;    

    mout[12] = 0.0f;
    mout[13] = 0.0f;
    mout[14] = 0.0f;
    mout[15] = 1.0f;
}

void mat4f_LoadZRotation(float radians, float* mout)
{
    float cosrad = cosf(radians);
    float sinrad = sinf(radians);

    mout[0] = cosrad;
    mout[1] = sinrad;
    mout[2] = 0.0f;
    mout[3] = 0.0f;

    mout[4] = -sinrad;
    mout[5] = cosrad;
    mout[6] = 0.0f;
    mout[7] = 0.0f;

    mout[8] = 0.0f;
    mout[9] = 0.0f;
    mout[10] = 1.0f;
    mout[11] = 0.0f;    

    mout[12] = 0.0f;
    mout[13] = 0.0f;
    mout[14] = 0.0f;
    mout[15] = 1.0f;
}

// v is a 3D vector
void mat4f_LoadTranslation(float* v, float* mout)
{
    mout[0] = 1.0f;
    mout[1] = 0.0f;
    mout[2] = 0.0f;
    mout[3] = 0.0f;

    mout[4] = 0.0f;
    mout[5] = 1.0f;
    mout[6] = 0.0f;
    mout[7] = 0.0f;

    mout[8] = 0.0f;
    mout[9] = 0.0f;
    mout[10] = 1.0f;
    mout[11] = 0.0f;    

    mout[12] = v[0];
    mout[13] = v[1];
    mout[14] = v[2];
    mout[15] = 1.0f;
}

void mat4f_LoadPerspective(float fov_radians, float aspect, float zNear, float zFar, float* mout)
{
    float f = 1.0f / tanf(fov_radians/2.0f);

    mout[0] = f / aspect;
    mout[1] = 0.0f;
    mout[2] = 0.0f;
    mout[3] = 0.0f;

    mout[4] = 0.0f;
    mout[5] = f;
    mout[6] = 0.0f;
    mout[7] = 0.0f;

    mout[8] = 0.0f;
    mout[9] = 0.0f;
    mout[10] = (zFar+zNear) / (zNear-zFar);
    mout[11] = -1.0f;

    mout[12] = 0.0f;
    mout[13] = 0.0f;
    mout[14] = 2 * zFar * zNear /  (zNear-zFar);
    mout[15] = 0.0f;
}

void mat4f_LoadOrtho(float left, float right, float bottom, float top, float near, float far, float* mout)
{
    float r_l = right - left;
    float t_b = top - bottom;
    float f_n = far - near;
    float tx = - (right + left) / (right - left);
    float ty = - (top + bottom) / (top - bottom);
    float tz = - (far + near) / (far - near);

    mout[0] = 2.0f / r_l;
    mout[1] = 0.0f;
    mout[2] = 0.0f;
    mout[3] = 0.0f;

    mout[4] = 0.0f;
    mout[5] = 2.0f / t_b;
    mout[6] = 0.0f;
    mout[7] = 0.0f;

    mout[8] = 0.0f;
    mout[9] = 0.0f;
    mout[10] = -2.0f / f_n;
    mout[11] = 0.0f;

    mout[12] = tx;
    mout[13] = ty;
    mout[14] = tz;
    mout[15] = 1.0f;
}

void mat4f_MultiplyMat4f(const float* a, const float* b, float* mout)
{
    mout[0]  = a[0] * b[0]  + a[4] * b[1]  + a[8] * b[2]   + a[12] * b[3];
    mout[1]  = a[1] * b[0]  + a[5] * b[1]  + a[9] * b[2]   + a[13] * b[3];
    mout[2]  = a[2] * b[0]  + a[6] * b[1]  + a[10] * b[2]  + a[14] * b[3];
    mout[3]  = a[3] * b[0]  + a[7] * b[1]  + a[11] * b[2]  + a[15] * b[3];

    mout[4]  = a[0] * b[4]  + a[4] * b[5]  + a[8] * b[6]   + a[12] * b[7];
    mout[5]  = a[1] * b[4]  + a[5] * b[5]  + a[9] * b[6]   + a[13] * b[7];
    mout[6]  = a[2] * b[4]  + a[6] * b[5]  + a[10] * b[6]  + a[14] * b[7];
    mout[7]  = a[3] * b[4]  + a[7] * b[5]  + a[11] * b[6]  + a[15] * b[7];

    mout[8]  = a[0] * b[8]  + a[4] * b[9]  + a[8] * b[10]  + a[12] * b[11];
    mout[9]  = a[1] * b[8]  + a[5] * b[9]  + a[9] * b[10]  + a[13] * b[11];
    mout[10] = a[2] * b[8]  + a[6] * b[9]  + a[10] * b[10] + a[14] * b[11];
    mout[11] = a[3] * b[8]  + a[7] * b[9]  + a[11] * b[10] + a[15] * b[11];

    mout[12] = a[0] * b[12] + a[4] * b[13] + a[8] * b[14]  + a[12] * b[15];
    mout[13] = a[1] * b[12] + a[5] * b[13] + a[9] * b[14]  + a[13] * b[15];
    mout[14] = a[2] * b[12] + a[6] * b[13] + a[10] * b[14] + a[14] * b[15];
    mout[15] = a[3] * b[12] + a[7] * b[13] + a[11] * b[14] + a[15] * b[15];
}
```

[Next](Resources-Shaders-videoSnake.vsh.md)[Previous](Classes-MovieRecorder.m.md)

