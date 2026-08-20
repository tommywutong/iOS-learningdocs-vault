---
title: 'AlignmentGuides: AppKit Haptic Feedback Filtering using NSAlignmentFeedbackFilter'
apple_id: TP40016087
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/AlignmentGuides/Listings/Objective_C_AlignmentGuides_AAPLAlignmentGuidesView_h.html
archived_at: '2026-07-18T03:00:57.036511Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AlignmentGuides: AppKit Haptic Feedback Filtering using NSAlignmentFeedbackFilter](AlignmentGuides-%20AppKit%20Haptic%20Feedback%20Filtering%20using%20NSAlignmentFeedbackFilte.md)


[Next](Objective-C-AlignmentGuides-AAPLDrawingView.m.md)[Previous](Objective-C-AlignmentGuides-AAPLAppDelegate.h.md)

# Objective-C/AlignmentGuides/AAPLAlignmentGuidesView.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    AlignmentGuidesView shows how to use NSAlignmentFeedbackFilter to align a box to the edges of its container and the container's center.

                The sample shows how to feed the filter using both a tracking loop (see mouseDown) and a gesture recognizer (see panGestureUpdated). These two methods feed the filter the latest event information, and then call into the appropriate handler for mouse down/dragged/up.
*/

@import Cocoa;

#import "AAPLDrawingView.h"

@interface AAPLAlignmentGuidesView : AAPLDrawingView

@property (weak) IBOutlet NSPopUpButton *eventHandlingButton;
@property (weak) IBOutlet NSButton *useGridButton;

@property (strong) NSAlignmentFeedbackFilter *feedbackFilter;

@property NSRect boxFrame;
@property NSPoint dragOriginOffset;

@property BOOL drawCenterXAsHoldingItem;
@property BOOL drawCenterYAsHoldingItem;

@end
```

[Next](Objective-C-AlignmentGuides-AAPLDrawingView.m.md)[Previous](Objective-C-AlignmentGuides-AAPLAppDelegate.h.md)

