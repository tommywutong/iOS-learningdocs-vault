---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLRenderer_h.html
archived_at: '2026-07-18T03:14:46.258916Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-texturedTerrain.metal.md)[Previous](MetalArrayTexture-AAPLMtkView.h.md)

# MetalArrayTexture/AAPLRenderer.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal Renderer. Acts as the update and render delegate for the MTKView object.
 */

#import <MetalKit/MTKView.h>
#import "AAPLViewController.h"

#import <Metal/Metal.h>

@interface AAPLRenderer : NSObject

@property (nonatomic, readonly) float zoomFactor;

// load all assets before triggering rendering
- (void)configure:(MTKView *)view;

- (void)rotateCameraWithDx:(float)dx dy:(float)dy scale:(float)scale;
- (void)zoomCameraWithScale:(float)scale;

- (void)reshapeView:(MTKView *)view;
- (void)drawView:(MTKView *)view;

@end
```

[Next](MetalArrayTexture-texturedTerrain.metal.md)[Previous](MetalArrayTexture-AAPLMtkView.h.md)

