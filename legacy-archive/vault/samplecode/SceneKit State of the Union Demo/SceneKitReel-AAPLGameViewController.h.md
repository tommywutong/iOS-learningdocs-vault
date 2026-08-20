---
title: SceneKit State of the Union Demo
apple_id: TP40014550
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: SceneKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitReel/Listings/SceneKitReel_AAPLGameViewController_h.html
archived_at: '2026-07-18T03:23:11.642701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit State of the Union Demo](SceneKit%20State%20of%20the%20Union%20Demo.md)


[Next](SceneKitReel-AAPLGameViewController.m.md)[Previous](SceneKitReel-OSX-AAPLAppDelegate.h.md)

# SceneKitReel/AAPLGameViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Game View Controller declaration.
 */

#if TARGET_OS_IPHONE
@import UIKit;
@interface AAPLGameViewController : UIViewController <SCNSceneRendererDelegate, SCNPhysicsContactDelegate>
#else
@interface AAPLGameViewController : NSViewController <SCNSceneRendererDelegate, SCNPhysicsContactDelegate>
#endif

- (void)handleTapAtPoint:(CGPoint)p;
- (void)handleDoubleTapAtPoint:(CGPoint)p;
- (void)handlePanAtPoint:(CGPoint)p;
- (void)gestureDidEnd;
- (void)gestureDidBegin;

- (void)tiltCameraWithOffset:(CGPoint)offset;

@end
```

[Next](SceneKitReel-AAPLGameViewController.m.md)[Previous](SceneKitReel-OSX-AAPLAppDelegate.h.md)

