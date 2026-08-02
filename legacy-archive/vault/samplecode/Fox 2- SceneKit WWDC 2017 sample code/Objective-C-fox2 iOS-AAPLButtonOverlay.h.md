---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_iOS_AAPLButtonOverlay_h.html
archived_at: '2026-07-26T19:54:17.112003Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20iOS-AAPLPadOverlay.m.md)[Previous](Objective-C-fox2%20iOS-AAPLGameViewController.m.md)

# Objective-C/fox2 iOS/AAPLButtonOverlay.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Support class for action buttons.
 */

#import <SpriteKit/SpriteKit.h>

NS_ASSUME_NONNULL_BEGIN

@class AAPLButtonOverlay;

@protocol AAPLButtonOverlayDelegate <NSObject>

- (void)willPressButtonOverlay:(AAPLButtonOverlay*)button;
- (void)didPressButtonOverlay:(AAPLButtonOverlay*)button;

@end

@interface AAPLButtonOverlay : SKNode

// Default 25, 25
@property (nonatomic, assign) CGSize size;

@property (nonatomic, weak, nullable) id<AAPLButtonOverlayDelegate> delegate;

- (instancetype)init NS_UNAVAILABLE;
- (instancetype)initWithCoder:(NSCoder *)aDecoder NS_UNAVAILABLE;

- (instancetype)initWithText:(NSString *)text NS_DESIGNATED_INITIALIZER;

NS_ASSUME_NONNULL_END

@end
```

[Next](Objective-C-fox2%20iOS-AAPLPadOverlay.m.md)[Previous](Objective-C-fox2%20iOS-AAPLGameViewController.m.md)

