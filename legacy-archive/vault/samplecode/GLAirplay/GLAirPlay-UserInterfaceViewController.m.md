---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_UserInterfaceViewController_m.html
archived_at: '2026-07-18T03:09:50.533054Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-GLView.h.md)[Previous](GLAirPlay-MyOpenALSupport.h.md)

# GLAirPlay/UserInterfaceViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This UIViewController configures the appearances of the UI when an external display is connected/disconnected.
 */

#import "UserInterfaceViewController.h"

@interface UserInterfaceViewController () {
    CGRect _fsFrame;
}
@end

@implementation UserInterfaceViewController

- (float)rotatingRadius
{
    return self.slider.value * 2.0f;
}

- (void)screenDidConnect
{
    self.view.backgroundColor = [UIColor whiteColor];
    self.view.frame = _fsFrame; //fullscreen
    self.view.autoresizingMask =
        UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin |
        UIViewAutoresizingFlexibleTopMargin | UIViewAutoresizingFlexibleBottomMargin |
        UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
}

- (void)screenDidDisconnect
{
    self.view.backgroundColor = [UIColor clearColor];
    self.view.frame = CGRectMake(0, _fsFrame.size.height - 80, _fsFrame.size.width, 50);
    self.view.autoresizingMask =
        UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin |
        UIViewAutoresizingFlexibleTopMargin | /*fixed bottom*/
        UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
}

- (void)viewDidLoad
{
    [super viewDidLoad];

    _fsFrame = self.view.frame;
}

- (BOOL)shouldAutorotate {
    return YES;
}

@end
```

[Next](GLAirPlay-GLView.h.md)[Previous](GLAirPlay-MyOpenALSupport.h.md)

