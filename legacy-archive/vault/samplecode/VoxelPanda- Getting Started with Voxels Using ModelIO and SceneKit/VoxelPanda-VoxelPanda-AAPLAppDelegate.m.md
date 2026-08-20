---
title: 'VoxelPanda: Getting Started with Voxels Using ModelIO and SceneKit'
apple_id: TP40016473
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ModelIO
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/VoxelPanda/Listings/VoxelPanda_VoxelPanda_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:28:03.525786Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VoxelPanda: Getting Started with Voxels Using ModelIO and SceneKit](VoxelPanda-%20Getting%20Started%20with%20Voxels%20Using%20ModelIO%20and%20SceneKit.md)


[Next](VoxelPanda-VoxelPanda-AAPLSceneViewController.m.md)[Previous](VoxelPanda-VoxelPanda-AAPLSceneViewController.h.md)

# VoxelPanda/VoxelPanda/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app delegate is a supporting class within the scope of this sample.
 */
#import "AAPLAppDelegate.h"

@interface AAPLAppDelegate ()

@property (weak) IBOutlet NSWindow *window;

@end

@implementation AAPLAppDelegate

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(nonnull NSApplication *)sender
{
    return YES;
}

@end
```

[Next](VoxelPanda-VoxelPanda-AAPLSceneViewController.m.md)[Previous](VoxelPanda-VoxelPanda-AAPLSceneViewController.h.md)

