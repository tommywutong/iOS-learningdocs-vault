---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_iOS_AAPLControlOverlay_h.html
archived_at: '2026-07-26T19:54:17.145772Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20tvOS-main.m.md)[Previous](Objective-C-fox2%20iOS-AAPLControlOverlay.m.md)

# Objective-C/fox2 iOS/AAPLControlOverlay.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Exposes game controller action button type functionality with screen-rendered buttons.
 */

#import <Foundation/Foundation.h>

#import "AAPLPadOverlay.h"
#import "AAPLButtonOverlay.h"

@interface AAPLControlOverlay : SKNode

- (instancetype)init NS_UNAVAILABLE;
- (instancetype)initWithCoder:(NSCoder *)aDecoder NS_UNAVAILABLE;

- (instancetype)initWithFrame:(CGRect)frame NS_DESIGNATED_INITIALIZER;

@property (nonatomic, retain) AAPLPadOverlay* leftPad;
@property (nonatomic, retain) AAPLPadOverlay* rightPad;
@property (nonatomic, retain) AAPLButtonOverlay* buttonA;
@property (nonatomic, retain) AAPLButtonOverlay* buttonB;

@end
```

[Next](Objective-C-fox2%20tvOS-main.m.md)[Previous](Objective-C-fox2%20iOS-AAPLControlOverlay.m.md)

