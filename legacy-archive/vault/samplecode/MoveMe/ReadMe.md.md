---
title: MoveMe
apple_id: DTS40007315
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-09-24'
source_url: https://developer.apple.com/library/archive/samplecode/MoveMe/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:16:03.518656Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoveMe](MoveMe.md)


[Next](MoveMe-APLAppDelegate.h.md)[Previous](MoveMe-main.m.md)

# ReadMe.md

```objc
# MoveMe


## Description
+ This application illustrates simple drawing, touch handling, and animation using UIKit and Core Animation.

+ The main class of interest is APLMoveMeView.  An instance of APLMoveMeView is created in the main storyboard.
+ If you touch inside the placard, the placard is animated in two ways: its transform is changed such that it appears to pulse, and it is moved such that its center is directly under the touch.
+ If you move your finger, APLMoveMeView moves the placard so that it remains centered under the touch. When the touch ends, the placard is animated back to the center of the screen, and its original (identity) transform restored.

+ The UIView methods implemented by APLMoveMeView that relate to touch handling are:

- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
- (void)touchesMoved:(NSSet *)touches withEvent:(UIEvent *)event
- (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
- (void)touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event

+ These in turn invoke other methods to perform the animation.  The sample illustrates two forms of animation:

- (void)animateFirstTouchAtPoint:(CGPoint)touchPoint shows you how to use UIView's built-in animation with a delegate.  Two slightly different implementations are provided to illustrate different animation behaviors.

- (void)animatePlacardViewToCenter shows how to implement explicit animation using CAKeyframeAnimation.

+ Further details are given in comments in the code.


## Build Requirements
+ iOS 8.0 SDK or later

## Runtime Requirements
+ iOS 8.0 or later

Copyright (C) 2008-2015 Apple Inc. All rights reserved.
```

[Next](MoveMe-APLAppDelegate.h.md)[Previous](MoveMe-main.m.md)

