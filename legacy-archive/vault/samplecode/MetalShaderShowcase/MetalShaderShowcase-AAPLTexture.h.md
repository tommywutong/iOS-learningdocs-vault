---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLTexture_h.html
archived_at: '2026-07-18T03:14:53.854299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLParticleSystemRenderer.h.md)[Previous](MetalShaderShowcase-AAPLAppDelegate.h.md)

# MetalShaderShowcase/AAPLTexture.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Simple Utility class for creating a 2d texture
 */

#import <UIKit/UIKit.h>
#import <Metal/Metal.h>

@interface AAPLTexture : NSObject

@property (nonatomic, readonly)  id <MTLTexture>  texture;
@property (nonatomic, readonly)  MTLTextureType   target;
@property (nonatomic, readonly)  uint32_t         width;
@property (nonatomic, readonly)  uint32_t         height;
@property (nonatomic, readonly)  uint32_t         depth;
@property (nonatomic, readonly)  uint32_t         format;
@property (nonatomic, readonly)  NSString        *path;
@property (nonatomic, readonly)  BOOL             hasAlpha;
@property (nonatomic, readwrite) BOOL             flip;

- (id) initWithResourceName:(NSString *)name
                  extension:(NSString *)ext;

- (BOOL) finalize:(id<MTLDevice>)device;

@end
```

[Next](MetalShaderShowcase-AAPLParticleSystemRenderer.h.md)[Previous](MetalShaderShowcase-AAPLAppDelegate.h.md)

