---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Utility_vectorUtil_c.html
archived_at: '2026-07-18T03:10:04.464643Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Utility-modelUtil.c.md)[Previous](GLEssentials-Source-Utility-imageUtil.h.md)

# GLEssentials/Source/Utility/vectorUtil.c

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.

 See LICENSE.txt for this sample’s licensing information



 Abstract:

 Functions for performing vector math.
 */

#include "vectorUtil.h"

#include <math.h>
#include <memory.h>

void vec4Add(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] + rhs[0];
    vec[1] = lhs[1] + rhs[1];
    vec[2] = lhs[2] + rhs[2];
    vec[3] = lhs[3] + rhs[3];
}

void vec4Subtract(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] - rhs[0];
    vec[1] = lhs[1] - rhs[1];
    vec[2] = lhs[2] - rhs[2];
    vec[3] = lhs[3] - rhs[3];
}


void vec4Multiply(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] * rhs[0];
    vec[1] = lhs[1] * rhs[1];
    vec[2] = lhs[2] * rhs[2];
    vec[3] = lhs[3] * rhs[3];
}

void vec4Divide(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] / rhs[0];
    vec[1] = lhs[1] / rhs[1];
    vec[2] = lhs[2] / rhs[2];
    vec[3] = lhs[3] / rhs[3];
}


void vec3Add(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] + rhs[0];
    vec[1] = lhs[1] + rhs[1];
    vec[2] = lhs[2] + rhs[2];
}

void vec3Subtract(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] - rhs[0];
    vec[1] = lhs[1] - rhs[1];
    vec[2] = lhs[2] - rhs[2];
}


void vec3Multiply(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] * rhs[0];
    vec[1] = lhs[1] * rhs[1];
    vec[2] = lhs[2] * rhs[2];
}

void vec3Divide(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[0] / rhs[0];
    vec[1] = lhs[1] / rhs[1];
    vec[2] = lhs[2] / rhs[2];
}

float vec3DotProduct(const float* lhs, const float* rhs)
{
    return lhs[0]*rhs[0] + lhs[1]*rhs[1] + lhs[2]*rhs[2];   
}

float vec4DotProduct(const float* lhs, const float* rhs)
{
    return lhs[0]*rhs[0] + lhs[1]*rhs[1] + lhs[2]*rhs[2] + lhs[3]*rhs[3];   
}

void vec3CrossProduct(float* vec, const float* lhs, const float* rhs)
{
    vec[0] = lhs[1] * rhs[2] - lhs[2] * rhs[1];
    vec[1] = lhs[2] * rhs[0] - lhs[0] * rhs[2];
    vec[2] = lhs[0] * rhs[1] - lhs[1] * rhs[0];
}

float vec3Length(const float* vec)
{
    return sqrtf(vec[0]*vec[0] + vec[1]*vec[1] + vec[2]*vec[2]);
}

float vec3Distance(const float* pointA, const float* pointB)
{
    float diffx = pointA[0]-pointB[0];
    float diffy = pointA[1]-pointB[1];
    float diffz = pointA[2]-pointB[2];
    return sqrtf(diffx*diffx + diffy*diffy + diffz*diffz);
}

void vec3Normalize(float* vec, const float* src)
{
    float length = vec3Length(src);

    vec[0] = src[0]/length;
    vec[1] = src[1]/length;
    vec[2] = src[2]/length;
}
```

[Next](GLEssentials-Source-Utility-modelUtil.c.md)[Previous](GLEssentials-Source-Utility-imageUtil.h.md)

