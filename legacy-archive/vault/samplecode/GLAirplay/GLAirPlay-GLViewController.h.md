---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_GLViewController_h.html
archived_at: '2026-07-18T03:09:49.960578Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-GLView.m.md)[Previous](GLAirPlay-UserControlDelegate.h.md)

# GLAirPlay/GLViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This UIViewController configures the OpenGL ES view and its UI when an external display is connected/disconnected.
 */

#import <UIKit/UIKit.h>
#import "UserControlDelegate.h"

@interface GLViewController : UIViewController

@property (nonatomic, strong) UIViewController *userInterfaceOnTop;
@property (nonatomic, strong) UIViewController *userInterfaceFullscreen;

- (void)startAnimation;
- (void)stopAnimation;
- (void)screenDidConnect:(UIViewController *)userInterface;
- (void)screenDidDisconnect:(UIViewController *)userInterface;
- (void)setTargetScreen:(UIScreen *)targetScreen;

@end
```

[Next](GLAirPlay-GLView.m.md)[Previous](GLAirPlay-UserControlDelegate.h.md)

