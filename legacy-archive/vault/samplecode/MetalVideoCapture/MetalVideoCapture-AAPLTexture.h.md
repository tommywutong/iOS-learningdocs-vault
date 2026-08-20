---
title: MetalVideoCapture
apple_id: TP40015131
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/MetalVideoCapture/Listings/MetalVideoCapture_AAPLTexture_h.html
archived_at: '2026-07-18T03:14:55.226162Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalVideoCapture](MetalVideoCapture.md)


[Next](MetalVideoCapture-AAPLRenderer.mm.md)[Previous](MetalVideoCapture-AAPLPVRTexture.m.md)

# MetalVideoCapture/AAPLTexture.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Texture Loading classes for Metal. Includes examples of how to load a 2D, and Cubemap textures.
 */

#import <UIKit/UIKit.h>
#import <Metal/Metal.h>

@interface AAPLTexture : NSObject

@property (readonly) id <MTLTexture> texture;
@property (readonly) uint32_t width;
@property (readonly) uint32_t height;
@property (readonly) uint32_t depth;
@property (readonly) uint32_t target;
@property (readonly) uint32_t pixelFormat;
@property (readonly) BOOL hasAlpha;
@property (readonly) NSString *pathToTextureFile;

- (id)initWithResourceName:(NSString *)name extension:(NSString *)ext;
- (BOOL)loadIntoTextureWithDevice:(id<MTLDevice>)device;

@end

@interface AAPLTexture2D : AAPLTexture
@end

@interface AAPLTextureCubeMap : AAPLTexture
@end
```

[Next](MetalVideoCapture-AAPLRenderer.mm.md)[Previous](MetalVideoCapture-AAPLPVRTexture.m.md)

