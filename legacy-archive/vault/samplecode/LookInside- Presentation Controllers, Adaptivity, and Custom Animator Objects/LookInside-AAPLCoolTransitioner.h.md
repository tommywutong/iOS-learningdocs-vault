---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLCoolTransitioner_h.html
archived_at: '2026-07-18T03:13:49.156851Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LookInside-AAPLOverlayPresentationController.m.md)[Previous](LookInside-AAPLAppDelegate.h.md)

# LookInside/AAPLCoolTransitioner.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  AAPLCoolAnimatedTransitioning and AAPLCoolTransitioningDelegate interfaces.

 */

@import UIKit;

@interface AAPLCoolAnimatedTransitioning : NSObject <UIViewControllerAnimatedTransitioning>
@property (nonatomic) BOOL isPresentation;
@end

@interface AAPLCoolTransitioningDelegate : NSObject <UIViewControllerTransitioningDelegate>
@end
```

[Next](LookInside-AAPLOverlayPresentationController.m.md)[Previous](LookInside-AAPLAppDelegate.h.md)

