---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLArrayTexture_h.html
archived_at: '2026-07-18T03:14:46.030721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-GeoUtils.c.md)[Previous](MetalArrayTexture-GeoUtils.h.md)

# MetalArrayTexture/AAPLArrayTexture.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple Utility class for creating a 2d array texture
 */

#import <Metal/Metal.h>

@interface AAPLArrayTexture : NSObject

@property (nonatomic, readonly) id <MTLTexture> texture;
@property (nonatomic, readonly) uint32_t width;
@property (nonatomic, readonly) uint32_t height;

- (instancetype)initWithTextureWidth:(NSUInteger)width textureHeight:(NSUInteger)height arrayLength:(NSUInteger)length device:(id <MTLDevice>)device;
- (BOOL)setSlice:(NSUInteger)slice withContentsOfFile:(NSString *)path;

@end
```

[Next](MetalArrayTexture-GeoUtils.c.md)[Previous](MetalArrayTexture-GeoUtils.h.md)

