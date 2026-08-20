---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/OSX_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:00:54.143161Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLFleeScene.h.md)[Previous](OSX-main.m.md)

# OSX/AAPLAppDelegate.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    OS X application delegate. Handles switching demo scenes based on UI controls.
 */

@import SpriteKit;

@interface AAPLAppDelegate : NSObject <NSApplicationDelegate>

@property (weak) IBOutlet NSWindow *window;
@property (weak) IBOutlet SKView *skView;
@property (weak) IBOutlet NSSegmentedControl *sceneControl;

@end
```

[Next](Common-AAPLFleeScene.h.md)[Previous](OSX-main.m.md)

