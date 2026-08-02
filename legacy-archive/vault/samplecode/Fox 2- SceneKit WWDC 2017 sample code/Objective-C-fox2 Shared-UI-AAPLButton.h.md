---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_UI_AAPLButton_h.html
archived_at: '2026-07-26T19:54:16.880591Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-UI-AAPLMenu.h.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLButton.m.md)

# Objective-C/fox2 Shared/UI/AAPLButton.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom `SKNode` based button.
 */

#import <SpriteKit/SpriteKit.h>

@interface AAPLButton : SKNode {
    void (*_action)(id, SEL);
}

+ (AAPLButton*)buttonWithText:(NSString*)txt;
+ (AAPLButton*)buttonWithSKNode:(SKNode*)node;

@property (readonly) CGFloat width;

- (void)setText:(NSString*)txt;
- (void)setBackgroundColor:(SKColor*)col;

- (void)setClickedTarget:(id)target action:(SEL)action;

@end
```

[Next](Objective-C-fox2%20Shared-UI-AAPLMenu.h.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLButton.m.md)

