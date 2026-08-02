---
title: MetalInstancedHelix
apple_id: TP40015091
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/MetalInstancedHelix/Listings/MetalInstancedHelix_AAPLRenderer_h.html
archived_at: '2026-07-18T03:14:50.639260Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalInstancedHelix](MetalInstancedHelix.md)


[Next](MetalInstancedHelix-AAPLAppDelegate.mm.md)[Previous](MetalInstancedHelix-AAPLAppDelegate.h.md)

# MetalInstancedHelix/AAPLRenderer.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal Renderer for MetalInstancedHelix. Acts as the update and render delegate for the view controller and performs rendering. In MetalInstancedHelix, the renderer draws N cubes, whos color values change every update.
 */

#import "AAPLView.h"
#import "AAPLViewController.h"

#import <Metal/Metal.h>

@interface AAPLRenderer : NSObject <AAPLViewControllerDelegate, AAPLViewDelegate>

// load all assets before triggering rendering
- (void)configure:(AAPLView *)view;

@end
```

[Next](MetalInstancedHelix-AAPLAppDelegate.mm.md)[Previous](MetalInstancedHelix-AAPLAppDelegate.h.md)

