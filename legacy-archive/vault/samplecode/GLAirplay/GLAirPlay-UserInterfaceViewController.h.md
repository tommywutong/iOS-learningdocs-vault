---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_UserInterfaceViewController_h.html
archived_at: '2026-07-18T03:09:50.492066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-AppDelegate.h.md)[Previous](GLAirPlay-GLViewController.m.md)

# GLAirPlay/UserInterfaceViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This UIViewController configures the appearances of the UI when an external display is connected/disconnected.
 */

#import <UIKit/UIKit.h>
#import <AVFoundation/AVFoundation.h>

#import "UserControlDelegate.h"

@interface UserInterfaceViewController : UIViewController <UserControlDelegate>

@property (nonatomic, weak) IBOutlet UISlider *slider;

- (void)screenDidConnect;
- (void)screenDidDisconnect;

@end
```

[Next](GLAirPlay-AppDelegate.h.md)[Previous](GLAirPlay-GLViewController.m.md)

