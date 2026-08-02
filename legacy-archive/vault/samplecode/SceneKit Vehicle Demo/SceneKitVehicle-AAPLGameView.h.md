---
title: SceneKit Vehicle Demo
apple_id: TP40014549
resource_type: Sample Code
platform: iOS
topic: null
technology: SceneKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitVehicle/Listings/SceneKitVehicle_AAPLGameView_h.html
archived_at: '2026-07-18T03:23:13.105201Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit Vehicle Demo](SceneKit%20Vehicle%20Demo.md)


[Next](SceneKitVehicle-AAPLOverlayScene.m.md)[Previous](SceneKitVehicle-AAPLGameViewController.h.md)

# SceneKitVehicle/AAPLGameView.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A SceneKit view that handles touch events.

 */

#import <UIKit/UIKit.h>
#import <SceneKit/SceneKit.h>

@interface AAPLGameView : SCNView

@property NSUInteger touchCount;
@property BOOL inCarView;

@end
```

[Next](SceneKitVehicle-AAPLOverlayScene.m.md)[Previous](SceneKitVehicle-AAPLGameViewController.h.md)

