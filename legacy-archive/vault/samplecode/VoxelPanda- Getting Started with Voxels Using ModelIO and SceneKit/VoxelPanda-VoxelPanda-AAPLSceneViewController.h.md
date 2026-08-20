---
title: 'VoxelPanda: Getting Started with Voxels Using ModelIO and SceneKit'
apple_id: TP40016473
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ModelIO
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/VoxelPanda/Listings/VoxelPanda_VoxelPanda_AAPLSceneViewController_h.html
archived_at: '2026-07-18T03:28:03.564848Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VoxelPanda: Getting Started with Voxels Using ModelIO and SceneKit](VoxelPanda-%20Getting%20Started%20with%20Voxels%20Using%20ModelIO%20and%20SceneKit.md)


[Next](VoxelPanda-VoxelPanda-AAPLAppDelegate.m.md)[Previous](VoxelPanda-VoxelPanda-main.m.md)

# VoxelPanda/VoxelPanda/AAPLSceneViewController.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view controller contains the Model IO code which is the focus of the sample, which is the loading of voxels. The voxels are displayed using SceneKit as an example graphics library.
 */

#if !TARGET_OS_IPHONE
@interface AAPLSceneViewController : NSViewController
#else
@interface AAPLSceneViewController : UIViewController
#endif


@property (weak) IBOutlet SCNView *sceneView;

- (IBAction)voxelize:(id)sender;
- (IBAction)dispalyVoxelsAsCubes:(id)sender;
- (IBAction)dispalyVoxelsAsSpheres:(id)sender;
- (IBAction)explode:(id)sender;
- (IBAction)reset:(id)sender;

@end
```

[Next](VoxelPanda-VoxelPanda-AAPLAppDelegate.m.md)[Previous](VoxelPanda-VoxelPanda-main.m.md)

