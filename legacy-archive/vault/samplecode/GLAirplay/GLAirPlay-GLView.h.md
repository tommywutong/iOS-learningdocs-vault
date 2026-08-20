---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_GLView_h.html
archived_at: '2026-07-18T03:09:50.081575Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-AppDelegate.m.md)[Previous](GLAirPlay-UserInterfaceViewController.m.md)

# GLAirPlay/GLView.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The OpenGL ES view which renders a rotating cube. Responsible for creating a CADisplayLink for the new target display when a connection/disconnection occurs.
 */

#import <UIKit/UIKit.h>
#import <GLKit/GLKit.h>

#import "UserControlDelegate.h"

@interface GLView : UIView

@property (readonly, nonatomic, getter=isAnimating) BOOL animating;
@property (nonatomic) NSInteger animationFrameInterval;
@property (nonatomic, strong) id <UserControlDelegate> userControlDelegate;
@property (nonatomic, weak) UIScreen *targetScreen;

- (void)startAnimation;
- (void)stopAnimation;
- (void)drawView:(id)sender;

@end
```

[Next](GLAirPlay-AppDelegate.m.md)[Previous](GLAirPlay-UserInterfaceViewController.m.md)

