---
title: Fireworks
apple_id: DTS40009114
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2016-03-10'
source_url: https://developer.apple.com/library/archive/samplecode/Fireworks/Listings/Fireworks_FireworksAppDelegate_m.html
archived_at: '2026-07-18T03:08:44.996775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fireworks](Fireworks.md)


[Next](Fireworks-FireworksAppDelegate.h.md)[Previous](Fireworks-main.m.md)

# Fireworks/FireworksAppDelegate.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Standard app delegate
 */

#import "FireworksAppDelegate.h"

@implementation FireworksAppDelegate

// Quit app when the window is closed
- (BOOL) applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)theApplication {
    return YES;
}

- (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)sender {
    return NSTerminateNow;
}

@end
```

[Next](Fireworks-FireworksAppDelegate.h.md)[Previous](Fireworks-main.m.md)

