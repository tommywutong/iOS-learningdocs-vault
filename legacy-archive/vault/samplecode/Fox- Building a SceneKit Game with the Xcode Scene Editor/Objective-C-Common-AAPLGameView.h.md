---
title: 'Fox: Building a SceneKit Game with the Xcode Scene Editor'
apple_id: TP40016154
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: General
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fox/Listings/Objective_C_Common_AAPLGameView_h.html
archived_at: '2026-07-18T03:08:52.938853Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox: Building a SceneKit Game with the Xcode Scene Editor](Fox-%20Building%20a%20SceneKit%20Game%20with%20the%20Xcode%20Scene%20Editor.md)


[Next](Objective-C-Common-AAPLGameViewControllerPrivate.h.md)[Previous](Objective-C-Common-AAPLCharacter.m.md)

# Objective-C/Common/AAPLGameView.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The view displaying the game scene, including the 2D overlay.
*/

@import simd;
@import SceneKit;

@protocol AAPLKeyboardAndMouseEventsDelegate <NSObject>
#if !(TARGET_OS_IOS || TARGET_OS_TV)
@required
- (BOOL)mouseDown:(NSView *)view event:(NSEvent *)event;
- (BOOL)mouseDragged:(NSView *)view event:(NSEvent *)event;
- (BOOL)mouseUp:(NSView *)view event:(NSEvent *)event;
- (BOOL)keyDown:(NSView *)view event:(NSEvent *)event;
- (BOOL)keyUp:(NSView *)view event:(NSEvent *)event;
#endif
@end

@interface AAPLGameView : SCNView

@property(nonatomic) NSUInteger collectedPearlsCount;
@property(nonatomic) NSUInteger collectedFlowersCount;

- (void)showEndScreen;

@property(nonatomic, weak) id <AAPLKeyboardAndMouseEventsDelegate> eventsDelegate;

#if TARGET_OS_IOS
- (CGRect)virtualDPadBounds;
#endif

@end
```

[Next](Objective-C-Common-AAPLGameViewControllerPrivate.h.md)[Previous](Objective-C-Common-AAPLCharacter.m.md)

