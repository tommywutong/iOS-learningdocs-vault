---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLMtkView_h.html
archived_at: '2026-07-18T03:14:46.141663Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-AAPLRenderer.h.md)[Previous](MetalArrayTexture-AAPLRenderer.mm.md)

# MetalArrayTexture/AAPLMtkView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A MTKView subclass. Handles camera movement. Delegates to the AAPLRenderer object for actual rendering and resizing.
 */

#import <MetalKit/MetalKit.h>

#import "AAPLRenderer.h"

@interface AAPLMtkView : MTKView

@property (strong, nonatomic) AAPLRenderer *renderer;

@end
```

[Next](MetalArrayTexture-AAPLRenderer.h.md)[Previous](MetalArrayTexture-AAPLRenderer.mm.md)

