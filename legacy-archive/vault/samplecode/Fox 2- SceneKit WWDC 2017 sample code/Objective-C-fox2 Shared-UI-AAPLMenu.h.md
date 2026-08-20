---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_UI_AAPLMenu_h.html
archived_at: '2026-07-26T19:54:16.885482Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-UI-AAPLMenu.m.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLButton.h.md)

# Objective-C/fox2 Shared/UI/AAPLMenu.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom `SKNode` based menu.
 */

#import <Foundation/Foundation.h>
#import <SpriteKit/SpriteKit.h>

#import "AAPLButton.h"
#import "AAPLSlider.h"

@class AAPLMenu;

@protocol AAPLMenuDelegate <NSObject>

- (void)fStopChanged:(CGFloat)value;
- (void)focusDistanceChanged:(CGFloat)value;
- (void)debugMenuSelectCameraAtIndex:(NSUInteger)index;

@end

@interface AAPLMenu : SKNode

@property (nonatomic, weak) id<AAPLMenuDelegate> delegate;

- (id)initWithSize:(CGSize)size;
- (void)showMenu;

@end
```

[Next](Objective-C-fox2%20Shared-UI-AAPLMenu.m.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLButton.h.md)

