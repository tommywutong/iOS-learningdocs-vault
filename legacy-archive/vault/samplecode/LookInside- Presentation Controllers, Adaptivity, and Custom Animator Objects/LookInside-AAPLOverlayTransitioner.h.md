---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLOverlayTransitioner_h.html
archived_at: '2026-07-18T03:13:49.306680Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LICENSE.txt.md)[Previous](LookInside-AAPLOverlayPresentationController.h.md)

# LookInside/AAPLOverlayTransitioner.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  AAPLOverlayAnimatedTransitioning and AAPLOverlayTransitioningDelegate interfaces.

 */

@import UIKit;

@interface AAPLOverlayAnimatedTransitioning : NSObject <UIViewControllerAnimatedTransitioning>
@property (nonatomic) BOOL isPresentation;
@end

@interface AAPLOverlayTransitioningDelegate : NSObject <UIViewControllerTransitioningDelegate>
@end
```

[Next](LICENSE.txt.md)[Previous](LookInside-AAPLOverlayPresentationController.h.md)

