---
title: 'MetalBasicTessellation: A demonstration of the Metal tessellation pipeline'
apple_id: TP40017289
resource_type: Sample Code
platform: macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalBasicTessellation/Listings/Common_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:14:47.359781Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalBasicTessellation: A demonstration of the Metal tessellation pipeline](MetalBasicTessellation-%20A%20demonstration%20of%20the%20Metal%20tessellation%20pipeline.md)


[Next](iOS-AAPLViewController.h.md)[Previous](Common-AAPLTessellationPipeline.m.md)

# Common/AAPLAppDelegate.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application delegate for MetalBasicTessellation.
 */

#include <TargetConditionals.h>

#if TARGET_OS_IOS

#import <UIKit/UIKit.h>

@interface AAPLAppDelegate : UIResponder <UIApplicationDelegate>

@property (nullable, nonatomic, strong) UIWindow *window;

@end

#elif TARGET_OS_OSX

#import <Cocoa/Cocoa.h>

@interface AAPLAppDelegate : NSObject <NSApplicationDelegate>

@end

#endif
```

[Next](iOS-AAPLViewController.h.md)[Previous](Common-AAPLTessellationPipeline.m.md)

