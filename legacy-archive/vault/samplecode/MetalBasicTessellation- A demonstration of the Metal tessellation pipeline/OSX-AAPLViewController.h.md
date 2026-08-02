---
title: 'MetalBasicTessellation: A demonstration of the Metal tessellation pipeline'
apple_id: TP40017289
resource_type: Sample Code
platform: macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalBasicTessellation/Listings/OSX_AAPLViewController_h.html
archived_at: '2026-07-18T03:14:47.842957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalBasicTessellation: A demonstration of the Metal tessellation pipeline](MetalBasicTessellation-%20A%20demonstration%20of%20the%20Metal%20tessellation%20pipeline.md)


[Next](OSX-AAPLViewController.m.md)[Previous](README.md.md)

# OSX/AAPLViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View Controller for the OS X version of MetalBasicTessellation.
            The UI elements that can modify a tessellation pass are: a segmented control to select a patch type, a button to enable/disable wireframe rendering, sliders to change the edge and inside tessellation factors.
            The MTKView's drawing loop is only executed when the view appears, when it receives a view notification (setNeedsDisplay methods), or when its draw method is explicitly called (IBAction receiver methods).
            The MTKView's delegate methods are contained in the TessellationPipeline class.
 */

#import <Cocoa/Cocoa.h>

@interface AAPLViewController : NSViewController

@end
```

[Next](OSX-AAPLViewController.m.md)[Previous](README.md.md)

