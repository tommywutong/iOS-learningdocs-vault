---
title: MetalInstancedHelix
apple_id: TP40015091
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/MetalInstancedHelix/Listings/MetalInstancedHelix_AAPLSharedTypes_h.html
archived_at: '2026-07-18T03:14:50.829016Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalInstancedHelix](MetalInstancedHelix.md)


[Next](MetalInstancedHelix-AAPLTransforms.h.md)[Previous](MetalInstancedHelix-AAPLView.h.md)

# MetalInstancedHelix/AAPLSharedTypes.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
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
        simd::float4x4 modelview_projection_matrix;
        simd::float4x4 normal_matrix;
        simd::float4   ambient_color;
        simd::float4   diffuse_color;
        int            multiplier;
    } constants_t;
}

#endif

#endif
```

[Next](MetalInstancedHelix-AAPLTransforms.h.md)[Previous](MetalInstancedHelix-AAPLView.h.md)

