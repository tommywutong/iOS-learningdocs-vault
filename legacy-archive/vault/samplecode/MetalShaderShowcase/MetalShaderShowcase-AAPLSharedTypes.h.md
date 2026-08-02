---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLSharedTypes_h.html
archived_at: '2026-07-18T03:14:52.846450Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLTransforms.h.md)[Previous](MetalShaderShowcase-AAPLParticleSystem.mm.md)

# MetalShaderShowcase/AAPLSharedTypes.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shared data types between CPU code and metal shader code
 */

#ifndef _AAPL_SHARED_TYPES_H_
#define _AAPL_SHARED_TYPES_H_

#import <simd/simd.h>

#ifdef __cplusplus

namespace AAPL
{
    typedef struct
    {
        simd::float4x4 model_matrix;
        simd::float4x4 view_matrix;
        simd::float4x4 projection_matrix;
        float t;
        float lifespan;
    } uniforms_t;
}

#endif

#endif
```

[Next](MetalShaderShowcase-AAPLTransforms.h.md)[Previous](MetalShaderShowcase-AAPLParticleSystem.mm.md)

