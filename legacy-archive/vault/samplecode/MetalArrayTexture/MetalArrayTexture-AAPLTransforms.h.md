---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLTransforms_h.html
archived_at: '2026-07-18T03:14:46.532098Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-AAPLMtkView.m.md)[Previous](MetalArrayTexture-iOS-AAPLAppDelegate.mm.md)

# MetalArrayTexture/AAPLTransforms.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility methods for linear transformations of projective
  geometry of the left-handed coordinate system.
 */

#ifndef _AAPL_MATH_TRANSFORMS_H_
#define _AAPL_MATH_TRANSFORMS_H_

#import <simd/simd.h>

#ifdef __cplusplus

namespace AAPL
{
    namespace Math
    {
        float radians(const float& degrees);

        simd::float4x4 scale(const float& x,
                             const float& y,
                             const float& z);

        simd::float4x4 scale(const simd::float3& s);

        simd::float4x4 translate(const float& x,
                                 const float& y,
                                 const float& z);

        simd::float4x4 translate(const simd::float3& t);

        simd::float4x4 rotate(const float& angle,
                              const float& x,
                              const float& y,
                              const float& z);

        simd::float4x4 rotate(const float& angle,
                              const simd::float3& u);

        simd::float4x4 frustum(const float& fovH,
                               const float& fovV,
                               const float& near,
                               const float& far);

        simd::float4x4 frustum(const float& left,
                               const float& right,
                               const float& bottom,
                               const float& top,
                               const float& near,
                               const float& far);

        simd::float4x4 frustum_oc(const float& left,
                                  const float& right,
                                  const float& bottom,
                                  const float& top,
                                  const float& near,
                                  const float& far);

        simd::float4x4 lookAt(const float * const pEye,
                              const float * const pCenter,
                              const float * const pUp);

        simd::float4x4 lookAt(const simd::float3& eye,
                              const simd::float3& center,
                              const simd::float3& up);

        simd::float4x4 perspective(const float& width,
                                   const float& height,
                                   const float& near,
                                   const float& far);

        simd::float4x4 perspective_fov(const float& fovy,
                                       const float& aspect,
                                       const float& near,
                                       const float& far);

        simd::float4x4 perspective_fov(const float& fovy,
                                       const float& width,
                                       const float& height,
                                       const float& near,
                                       const float& far);

        simd::float4x4 ortho2d_oc(const float& left,
                                  const float& right,
                                  const float& bottom,
                                  const float& top,
                                  const float& near,
                                  const float& far);

        simd::float4x4 ortho2d_oc(const simd::float3& origin,
                                  const simd::float3& size);

        simd::float4x4 ortho2d(const float& left,
                               const float& right,
                               const float& bottom,
                               const float& top,
                               const float& near,
                               const float& far);

        simd::float4x4 ortho2d(const simd::float3& origin,
                               const simd::float3& size);
    } // Math
} // AAPL

#endif

#endif
```

[Next](MetalArrayTexture-AAPLMtkView.m.md)[Previous](MetalArrayTexture-iOS-AAPLAppDelegate.mm.md)

