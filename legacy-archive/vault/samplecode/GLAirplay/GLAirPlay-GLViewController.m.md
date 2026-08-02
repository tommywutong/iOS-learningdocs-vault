---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_GLViewController_m.html
archived_at: '2026-07-18T03:09:50.032996Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-UserInterfaceViewController.h.md)[Previous](GLAirPlay-AppDelegate.m.md)

# GLAirPlay/GLViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This UIViewController configures the OpenGL ES view and its UI when an external display is connected/disconnected.
 */

#import "GLViewController.h"
#import "UserInterfaceViewController.h"
#import "GLView.h"

@implementation GLViewController

- (void)screenDidConnect:(UIViewController *)userInterface
{
    // Remove UI previously added atop the GL view
    for (UIView* v in [self.view subviews])
            [v removeFromSuperview];

    // One of these userInterface view controllers is visible at a time,
    // so release the other one to minimize memory usage
    self.userInterfaceOnTop = nil;
    self.userInterfaceFullscreen = userInterface;

    if (self.userInterfaceFullscreen)
    {
        // Setup UI (When an external display is connected, it will be added to mainViewController's view
        // in MainViewController/-screenDidChange:)
        [(UserInterfaceViewController *)self.userInterfaceFullscreen screenDidConnect];

        // Set the userControlDelegte, which is responsible for setting the cube's rotating radius
        [(GLView *)self.view setUserControlDelegate:(id)self.userInterfaceFullscreen];
    }
}

- (void)screenDidDisconnect:(UIViewController *)userInterface
{
    // One of these userInterface view controllers is visible at a time,
    // so release the other one to minimize memory usage
    self.userInterfaceFullscreen = nil;
    self.userInterfaceOnTop = userInterface;

    if (self.userInterfaceOnTop)
    {
        // Setup UI
        [(UserInterfaceViewController *)self.userInterfaceOnTop screenDidDisconnect];

        // Add UI on top
        [(GLView *)self.view addSubview:self.userInterfaceOnTop.view];

        // Set the userControlDelegte, which is responsible for setting the cube's rotating radius
        [(GLView *)self.view setUserControlDelegate:(id)self.userInterfaceOnTop];
    }
}

- (void)setTargetScreen:(UIScreen *)targetScreen
{
    // Delegate to the GL view to create a CADisplayLink for the target display (UIScreen/-displayLinkWithTarget:selector:)
    // This will result in the native fps for whatever display you create it from.
    [(GLView *)self.view setTargetScreen:targetScreen];
}

- (void)startAnimation
{
    [(GLView *)self.view startAnimation];
}

- (void)stopAnimation
{
    [(GLView *)self.view stopAnimation];
}

- (void)viewDidLoad
{
    [super viewDidLoad];

    self.view.autoresizingMask =
        UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin |
        UIViewAutoresizingFlexibleTopMargin | UIViewAutoresizingFlexibleBottomMargin |
        UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (BOOL)shouldAutorotate {
    return YES;
}

@end
```

[Next](GLAirPlay-UserInterfaceViewController.h.md)[Previous](GLAirPlay-AppDelegate.m.md)

