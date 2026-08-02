---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Utility_vectorUtil_h.html
archived_at: '2026-07-18T03:10:04.555289Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Utility-sourceUtil.h.md)[Previous](GLEssentials-Source-Utility-sourceUtil.c.md)

# GLEssentials/Source/Utility/vectorUtil.h

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.

 See LICENSE.txt for this sample’s licensing information



 Abstract:

 Functions for performing vector math.
 */

#ifndef __VECTOR_UTIL_H__
#define __VECTOR_UTIL_H__

// A Vector is floating point array with either 3 or 4 components
// functions with the vec4 prefix require 4 elements in the array
// functions with vec3 prefix require only 3 elements in the array

// Subtracts one 4D vector to another
void vec4Add(float* vec, const float* lhs, const float* rhs);

// Subtracts one 4D vector from another
void vec4Subtract(float* vec, const float* lhs, const float* rhs);

// Multiplys one 4D vector by another
void vec4Multiply(float* vec, const float* lhs, const float* rhs);

// Divides one 4D vector by another
void vec4Divide(float* vec, const float* lhs, const float* rhs);

// Subtracts one 4D vector to another
void vec3Add(float* vec, const float* lhs, const float* rhs);

// Subtracts one 4D vector from another
void vec3Subtract(float* vec, const float* lhs, const float* rhs);

// Multiplys one 4D vector by another
void vec3Multiply(float* vec, const float* lhs, const float* rhs);

// Divides one 4D vector by another
void vec3Divide(float* vec, const float* lhs, const float* rhs);

// Calculates the Cross Product of a 3D vector
void vec3CrossProduct(float* vec, const float* lhs, const float* rhs);

// Normalizes a 3D vector
void vec3Normalize(float* vec, const float* src);

// Returns the Dot Product of 2 3D vectors
float vec3DotProduct(const float* lhs, const float* rhs);

// Returns the Dot Product of 2 4D vectors
float vec4DotProduct(const float* lhs, const float* rhs);

// Returns the length of a 3D vector 
// (i.e the distance of a point from the origin)
float vec3Length(const float* vec);

// Returns the distance between two 3D points
float vec3Distance(const float* pointA, const float* pointB);

#endif //__VECTOR_UTIL_H__
```

[Next](GLEssentials-Source-Utility-sourceUtil.h.md)[Previous](GLEssentials-Source-Utility-sourceUtil.c.md)

