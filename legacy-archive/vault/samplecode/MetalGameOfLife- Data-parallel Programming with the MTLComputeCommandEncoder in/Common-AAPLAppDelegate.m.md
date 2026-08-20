---
title: 'MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder
  in Metal'
apple_id: TP40017382
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalGameOfLife/Listings/Common_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:14:48.165749Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder in Metal](MetalGameOfLife-%20Data-parallel%20Programming%20with%20the%20MTLComputeCommandEncoder%20in.md)


[Next](Common-Shaders.metal.md)[Previous](OS%20X-main.m.md)

# Common/AAPLAppDelegate.m

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate for the Game of Life sample. Responds to application lifecycle messages.
*/

#import "AAPLAppDelegate.h"

@implementation AAPLAppDelegate

#if TARGET_OS_OSX

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender {
    return YES;
}

#endif

@end
```

[Next](Common-Shaders.metal.md)[Previous](OS%20X-main.m.md)

