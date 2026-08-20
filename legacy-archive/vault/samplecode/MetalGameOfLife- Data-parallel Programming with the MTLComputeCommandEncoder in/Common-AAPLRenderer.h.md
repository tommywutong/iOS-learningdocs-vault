---
title: 'MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder
  in Metal'
apple_id: TP40017382
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalGameOfLife/Listings/Common_AAPLRenderer_h.html
archived_at: '2026-07-18T03:14:48.268712Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder in Metal](MetalGameOfLife-%20Data-parallel%20Programming%20with%20the%20MTLComputeCommandEncoder%20in.md)


[Next](Common-AAPLRenderer.m.md)[Previous](Common-AAPLAppDelegate.h.md)

# Common/AAPLRenderer.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The renderer class for the Game of Life sample. Responsible for enqueuing compute and render work on the GPU.
*/

@import Foundation;
@import MetalKit;

@interface AAPLRenderer : NSObject <MTKViewDelegate>

@property (nonatomic, readonly) MTLSize gridSize;

/// Creates a new renderer and makes it the delegate of the view.
/// The grid size of the simulation is derived from the current
/// drawableSize of the view
- (instancetype)initWithView:(MTKView *)view;

/// Brings random cells in the neighborhood of the provided cell
/// coordinates to life. Can be used with touch or mouse inputs
/// to add interactivity to the simulation.
- (void)activateRandomCellsInNeighborhoodOfCell:(CGPoint)cell;

@end
```

[Next](Common-AAPLRenderer.m.md)[Previous](Common-AAPLAppDelegate.h.md)

