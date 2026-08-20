---
title: 'AlignmentGuides: AppKit Haptic Feedback Filtering using NSAlignmentFeedbackFilter'
apple_id: TP40016087
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/AlignmentGuides/Listings/Objective_C_AlignmentGuides_AAPLDrawingView_h.html
archived_at: '2026-07-18T03:00:57.269287Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AlignmentGuides: AppKit Haptic Feedback Filtering using NSAlignmentFeedbackFilter](AlignmentGuides-%20AppKit%20Haptic%20Feedback%20Filtering%20using%20NSAlignmentFeedbackFilte.md)


[Next](Objective-C-AlignmentGuides-AAPLAppDelegate.h.md)[Previous](Objective-C-AlignmentGuides-AAPLAlignmentGuidesView.m.md)

# Objective-C/AlignmentGuides/AAPLDrawingView.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    AAPLDrawingView is a helper for the sample code. Your app can draw however it wants since alignment is independent of the view hierarchy. Here, we're using bezier paths.
*/

@import Cocoa;

@interface AAPLDrawingView : NSView

- (void)drawBox:(NSRect)frame drawCenterAlignmentGuides:(BOOL)drawCenterAlignmentGuides;

- (void)drawHorizontalGuide:(CGFloat)yCoordinate holdingItem:(BOOL)holdingItem;

- (void)drawVerticalGuide:(CGFloat)xCoordinate holdingItem:(BOOL)holdingItem;

- (NSRect)constrainRectToBounds:(NSRect)rect;

@end
```

[Next](Objective-C-AlignmentGuides-AAPLAppDelegate.h.md)[Previous](Objective-C-AlignmentGuides-AAPLAlignmentGuidesView.m.md)

