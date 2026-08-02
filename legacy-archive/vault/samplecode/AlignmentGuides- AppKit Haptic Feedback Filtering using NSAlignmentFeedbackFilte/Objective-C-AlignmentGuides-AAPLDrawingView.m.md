---
title: 'AlignmentGuides: AppKit Haptic Feedback Filtering using NSAlignmentFeedbackFilter'
apple_id: TP40016087
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/AlignmentGuides/Listings/Objective_C_AlignmentGuides_AAPLDrawingView_m.html
archived_at: '2026-07-18T03:00:57.317242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AlignmentGuides: AppKit Haptic Feedback Filtering using NSAlignmentFeedbackFilter](AlignmentGuides-%20AppKit%20Haptic%20Feedback%20Filtering%20using%20NSAlignmentFeedbackFilte.md)


[Next](Swift-AlignmentGuides-AlignmentGuidesView.swift.md)[Previous](Objective-C-AlignmentGuides-AAPLAlignmentGuidesView.h.md)

# Objective-C/AlignmentGuides/AAPLDrawingView.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    AAPLDrawingView is a helper for the sample code. Your app can draw however it wants since alignment is independent of the view hierarchy. Here, we're using bezier paths.
*/

#import "AAPLDrawingView.h"

@implementation AAPLDrawingView

- (void)drawRect:(NSRect)dirtyRect {
    [[NSColor colorWithDeviceRed:0.95 green:0.95 blue:0.9 alpha:1.0] set];
    NSRectFill(self.bounds);

    [[NSColor blackColor] set];
    NSFrameRect(self.bounds);
}

- (void)drawBox:(NSRect)frame drawCenterAlignmentGuides:(BOOL)drawCenterAlignmentGuides {
    [[NSColor colorWithDeviceRed:0.78 green:0.78 blue:0.78 alpha:1.0] set];
    NSRectFill(frame);

    [[NSColor blackColor] set];
    NSFrameRectWithWidth(frame, 1.0);

    if (drawCenterAlignmentGuides) {
        NSBezierPath *path = [NSBezierPath new];
        [path moveToPoint:NSMakePoint(NSMinX(frame), NSMidY(frame))];
        [path lineToPoint:NSMakePoint(NSMaxX(frame), NSMidY(frame))];
        [path moveToPoint:NSMakePoint(NSMidX(frame), NSMinY(frame))];
        [path lineToPoint:NSMakePoint(NSMidX(frame), NSMaxY(frame))];
        [path stroke];
    }
}

- (void)drawHorizontalGuide:(CGFloat)yCoordinate holdingItem:(BOOL)holdingItem {
    NSBezierPath *path = [NSBezierPath new];
    [[NSColor colorWithDeviceRed:0.0 green:0.0 blue:1.0 alpha:(holdingItem ? 0.8 : 0.2)] set];
    [path moveToPoint:NSMakePoint(0.0, yCoordinate)];
    [path lineToPoint:NSMakePoint(self.bounds.size.width, yCoordinate)];
    [path stroke];
}

- (void)drawVerticalGuide:(CGFloat)xCoordinate holdingItem:(BOOL)holdingItem {
    NSBezierPath *path = [NSBezierPath new];
    [[NSColor colorWithDeviceRed:0.0 green:0.0 blue:1.0 alpha:(holdingItem ? 0.8 : 0.2)] set];
    [path moveToPoint:NSMakePoint(xCoordinate, 0.0)];
    [path lineToPoint:NSMakePoint(xCoordinate, self.bounds.size.height)];
    [path stroke];
}

- (NSRect)constrainRectToBounds:(NSRect)rect {
    if (rect.origin.x < 0.0) {
        rect.origin.x = 0.0;
    }

    if (rect.origin.y < 0.0) {
        rect.origin.y = 0.0;
    }

    if (NSMaxX(rect) > self.bounds.size.width) {
        rect.origin.x = self.bounds.size.width-rect.size.width;
    }

    if (NSMaxY(rect) > self.bounds.size.height) {
        rect.origin.y = self.bounds.size.height-rect.size.height;
    }

    return rect;
}

@end
```

[Next](Swift-AlignmentGuides-AlignmentGuidesView.swift.md)[Previous](Objective-C-AlignmentGuides-AAPLAlignmentGuidesView.h.md)

