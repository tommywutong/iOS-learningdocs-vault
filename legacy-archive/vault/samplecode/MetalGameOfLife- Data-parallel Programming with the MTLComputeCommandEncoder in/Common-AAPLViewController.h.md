---
title: 'MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder
  in Metal'
apple_id: TP40017382
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalGameOfLife/Listings/Common_AAPLViewController_h.html
archived_at: '2026-07-18T03:14:48.421425Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder in Metal](MetalGameOfLife-%20Data-parallel%20Programming%20with%20the%20MTLComputeCommandEncoder%20in.md)


[Next](Common-AAPLAppDelegate.h.md)[Previous](Common-Shaders.metal.md)

# Common/AAPLViewController.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The view controller class for the Game of Life sample. Manages an MTKView for displaying graphics rendered by Metal
    and mediates touch and mouse interactions.
*/

@import Foundation;

#if TARGET_OS_IPHONE
@import UIKit;
@interface AAPLViewController : UIViewController
#else
@import Cocoa;
@interface AAPLViewController : NSViewController
#endif
@end
```

[Next](Common-AAPLAppDelegate.h.md)[Previous](Common-Shaders.metal.md)

