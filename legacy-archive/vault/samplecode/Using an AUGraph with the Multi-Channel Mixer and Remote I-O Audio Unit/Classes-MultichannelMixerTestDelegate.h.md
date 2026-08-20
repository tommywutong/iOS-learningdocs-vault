---
title: Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit
apple_id: TP40016060
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/iOSMultichannelMixerTest/Listings/Classes_MultichannelMixerTestDelegate_h.html
archived_at: '2026-07-18T03:29:36.058345Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit](Using%20an%20AUGraph%20with%20the%20Multi-Channel%20Mixer%20and%20Remote%20I-O%20Audio%20Unit.md)


[Next](Classes-MyViewController.m.md)[Previous](main.m.md)

# Classes/MultichannelMixerTestDelegate.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application Delegate
*/

#import <UIKit/UIKit.h>

#import "MyViewController.h"
#import "CAXException.h"

@interface MultichannelMixerTestDelegate : NSObject <UIApplicationDelegate> {
    IBOutlet UIWindow *window;

    IBOutlet UINavigationController *navigationController;
    IBOutlet MyViewController       *myViewController;
}

@property (nonatomic, strong) UIWindow *window;
@property (nonatomic, retain) IBOutlet UINavigationController *navigationController;
@property (nonatomic, retain) IBOutlet MyViewController *myViewController;

@end
```

[Next](Classes-MyViewController.m.md)[Previous](main.m.md)

