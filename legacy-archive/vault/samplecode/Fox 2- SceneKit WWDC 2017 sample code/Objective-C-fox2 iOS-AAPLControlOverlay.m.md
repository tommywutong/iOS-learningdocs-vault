---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_iOS_AAPLControlOverlay_m.html
archived_at: '2026-07-26T19:54:17.141128Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20iOS-AAPLControlOverlay.h.md)[Previous](Objective-C-fox2%20iOS-AAPLGameViewController.h.md)

# Objective-C/fox2 iOS/AAPLControlOverlay.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Exposes game controller action button type functionality with screen-rendered buttons.
 */

#import "AAPLControlOverlay.h"

#define PadBottomMargin 40.0
#define PadLeftMargin 20.0
#define PadRightMargin 20.0

#define ButtonMarginFromPad 0.0
#define ButtonAPositionAngleDegree 155.0f
#define ButtonBPositionAngleDegree 110.0f

#define ToRadian(x) (x) * M_PI / 180.f

@implementation AAPLControlOverlay

- (instancetype)initWithFrame:(CGRect)frame {
    if (self = [super init]) {
        _leftPad = [[AAPLPadOverlay alloc] init];
        _leftPad.position = CGPointMake(PadLeftMargin, PadBottomMargin);
        [self addChild:_leftPad];

        _rightPad = [[AAPLPadOverlay alloc] init];
        _rightPad.position = CGPointMake(
            frame.size.width - PadRightMargin - _rightPad.size.width, PadBottomMargin);
        [self addChild:_rightPad];

        _buttonA = [[AAPLButtonOverlay alloc] initWithText:@"A"];
        _buttonB = [[AAPLButtonOverlay alloc] initWithText:@"B"];

        const float buttonDistance =
            _rightPad.size.height / 2.0f + _rightPad.stickSize.width / 2.0f + _buttonA.size.height / 2.0f + ButtonMarginFromPad;
        vector_float2 center = (vector_float2){
            _rightPad.position.x + _rightPad.size.width  / 2.0f,
            _rightPad.position.y + _rightPad.size.height / 2.0f };

        CGPoint buttonCenterOffset =  CGPointMake(_buttonA.size.width / 2.0f, _buttonA.size.height / 2.0f);
        _buttonA.position = CGPointMake(
            center.x + buttonDistance * cosf(ToRadian(ButtonAPositionAngleDegree)) - buttonCenterOffset.x,
            center.y + buttonDistance * sinf(ToRadian(ButtonAPositionAngleDegree)) - buttonCenterOffset.y);
        [self addChild:_buttonA];

        _buttonB.position = CGPointMake(
            center.x + buttonDistance * cosf(ToRadian(ButtonBPositionAngleDegree)) - buttonCenterOffset.x,
            center.y + buttonDistance * sinf(ToRadian(ButtonBPositionAngleDegree)) - buttonCenterOffset.y);
        [self addChild:_buttonB];
    }
    return self;
}

@end
```

[Next](Objective-C-fox2%20iOS-AAPLControlOverlay.h.md)[Previous](Objective-C-fox2%20iOS-AAPLGameViewController.h.md)

