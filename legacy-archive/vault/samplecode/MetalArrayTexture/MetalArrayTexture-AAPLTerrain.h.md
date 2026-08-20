---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLTerrain_h.html
archived_at: '2026-07-18T03:14:46.416842Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](README.md.md)[Previous](MetalArrayTexture-AAPLTerrain.mm.md)

# MetalArrayTexture/AAPLTerrain.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a terrain object.
 */

#import <Metal/Metal.h>

@interface AAPLTerrain : NSObject

// Indices
@property (nonatomic, readwrite) NSUInteger  vertexIndex;
@property (nonatomic, readwrite) NSUInteger  texCoordIndex;
@property (nonatomic, readwrite) NSUInteger  samplerIndex;

@property (nonatomic, readonly) uint32_t heightMapSize;
@property (nonatomic, readonly) uint32_t numOfSlices;

// Designated initializer
- (instancetype) initWithDevice:(id <MTLDevice>)device;

// Encoder
- (void)encode:(id <MTLRenderCommandEncoder>)renderEncoder;
- (void)draw:(id <MTLRenderCommandEncoder>)renderEncoder;

@end
```

[Next](README.md.md)[Previous](MetalArrayTexture-AAPLTerrain.mm.md)

