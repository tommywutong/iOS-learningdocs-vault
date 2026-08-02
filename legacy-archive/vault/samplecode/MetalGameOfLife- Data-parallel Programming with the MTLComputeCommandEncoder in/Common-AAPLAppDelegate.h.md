---
title: 'MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder
  in Metal'
apple_id: TP40017382
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalGameOfLife/Listings/Common_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:14:48.125481Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder in Metal](MetalGameOfLife-%20Data-parallel%20Programming%20with%20the%20MTLComputeCommandEncoder%20in.md)


[Next](Common-AAPLRenderer.h.md)[Previous](Common-AAPLViewController.h.md)

# Common/AAPLAppDelegate.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate for the Game of Life sample. Responds to application lifecycle messages.
*/

#include <TargetConditionals.h>

#if TARGET_OS_IOS || TARGET_OS_TV

@import UIKit;

@interface AAPLAppDelegate : UIResponder <UIApplicationDelegate>

@property (nullable, nonatomic, strong) UIWindow *window;

@end

#elif TARGET_OS_MAC

@import Cocoa;

@interface AAPLAppDelegate : NSObject <NSApplicationDelegate>

@end

#endif
```

[Next](Common-AAPLRenderer.h.md)[Previous](Common-AAPLViewController.h.md)

