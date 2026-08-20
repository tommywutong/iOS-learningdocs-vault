---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_UserControlDelegate_h.html
archived_at: '2026-07-18T03:09:50.455114Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](GLAirPlay-GLViewController.h.md)[Previous](GLAirPlay-main.m.md)

# GLAirPlay/UserControlDelegate.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The object that conforms to this UserControlDelegate protocol is responsible for setting the GL cube's rotating radius.
 */

#import <Foundation/Foundation.h>

@protocol UserControlDelegate <NSObject>

-(float)rotatingRadius;

@end
```

[Next](GLAirPlay-GLViewController.h.md)[Previous](GLAirPlay-main.m.md)

