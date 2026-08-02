---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/OSX_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:00:54.173649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](OSX-main.m.md)[Previous](iOS-AAPLGameViewController.h.md)

# OSX/AAPLAppDelegate.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    OS X application delegate. Handles switching demo scenes based on UI controls.
 */

#import "AAPLAppDelegate.h"

#import "AAPLGameScene.h"

@implementation AAPLAppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {

    self.window.titleVisibility = NSWindowTitleHidden;

    // Configure the view.
    self.skView.ignoresSiblingOrder = YES;
    self.skView.showsFPS = YES;
    self.skView.showsNodeCount = YES;

    // Present the scene.
    [self selectScene:self.sceneControl];
}

- (IBAction)selectScene:(NSSegmentedControl *)sender {
    AAPLGameScene *scene = [AAPLGameScene sceneWithType:sender.selectedSegment size:CGSizeMake(800, 600)];

    scene.scaleMode = SKSceneScaleModeAspectFit;

    [self.skView presentScene:scene];
}

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender {
    return YES;
}

@end
```

[Next](OSX-main.m.md)[Previous](iOS-AAPLGameViewController.h.md)

