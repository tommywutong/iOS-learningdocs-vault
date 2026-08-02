---
title: Fireworks
apple_id: DTS40009114
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2016-03-10'
source_url: https://developer.apple.com/library/archive/samplecode/Fireworks/Listings/Fireworks_AppController_h.html
archived_at: '2026-07-18T03:08:44.770103Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fireworks](Fireworks.md)


[Next](ReadMe.md.md)[Previous](Fireworks-AppController.m.md)

# Fireworks/AppController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Create a fireworks simulation using particles, respond to user actions
 */

@import Cocoa;
@import QuartzCore;

@interface AppController : NSObject {
    IBOutlet NSView *theView;
    CALayer *rootLayer;
    CAEmitterLayer *mortor;
    IBOutlet NSSlider *rocketRange;
    IBOutlet NSSlider *fireworkRange;
    IBOutlet NSSlider *fireworkVelocity;
    IBOutlet NSSlider *fireworkVelocityRange;
    IBOutlet NSSlider *rocketVelocity;
    IBOutlet NSSlider *rocketVelocityRange;
    IBOutlet NSSlider *fireworkGravity;
    IBOutlet NSSlider *rocketGravity;
    IBOutlet NSSlider *animationSpeed;
}

@end
```

[Next](ReadMe.md.md)[Previous](Fireworks-AppController.m.md)

