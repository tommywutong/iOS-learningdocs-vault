---
title: 'SplitViews: Using NSSplitView in a variety of different ways'
apple_id: DTS40011336
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/SplitViews/Listings/SplitViews_MailWindowController_m.html
archived_at: '2026-07-18T03:25:20.497173Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SplitViews: Using NSSplitView in a variety of different ways](SplitViews-%20Using%20NSSplitView%20in%20a%20variety%20of%20different%20ways.md)


[Next](SplitViews-MailWindowController.h.md)[Previous](SplitViews-ActivityView.h.md)

# SplitViews/MailWindowController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  Custom NSWindowController subclass used for managing the mail-style window. 
 */

#import "MailWindowController.h"

@interface MailWindowController ()

@property (weak) IBOutlet NSSplitView *verticalSplitView;
@property (weak) IBOutlet NSSplitView *horizontalSplitView;
@property (weak) IBOutlet NSView *dividerHandleView;

@end


#pragma mark -

@implementation MailWindowController

// -------------------------------------------------------------------------------
//  windowDidLoad
// -------------------------------------------------------------------------------
- (void)windowDidLoad
{
    (self.verticalSplitView).delegate = self;   // we want a chance to affect the vertical split view coverage
}

// -------------------------------------------------------------------------------
//  splitView:effectiveRect:effectiveRect:forDrawnRect:ofDividerAtIndex
// -------------------------------------------------------------------------------
- (NSRect)splitView:(NSSplitView *)splitView effectiveRect:(NSRect)proposedEffectiveRect forDrawnRect:(NSRect)drawnRect ofDividerAtIndex:(NSInteger)dividerIndex
{
    NSRect effectiveRect = drawnRect;

    if (splitView == self.verticalSplitView)
    {
        // don't steal as much from the scroll bar as NSSplitView normally would
        effectiveRect.origin.x -= 2.0;
        effectiveRect.size.width += 6.0;

    }

    return effectiveRect;
}

// -------------------------------------------------------------------------------
//  splitView:additionalEffectiveRectOfDividerAtIndex:dividerIndex:
// -------------------------------------------------------------------------------
- (NSRect)splitView:(NSSplitView *)splitView additionalEffectiveRectOfDividerAtIndex:(NSInteger)dividerIndex
{
    // we have a divider handle next to one of the split views in the window
    if (splitView == self.verticalSplitView)
    {
        return [self.dividerHandleView convertRect:(self.dividerHandleView).bounds toView:splitView];
    }
    else
    {
        return NSZeroRect;
    }
}

// -------------------------------------------------------------------------------
//  constrainMinCoordinate:proposedCoordinate:index
// -------------------------------------------------------------------------------
- (CGFloat)splitView:(NSSplitView *)splitView constrainMinCoordinate:(CGFloat)proposedCoordinate ofSubviewAt:(NSInteger)index
{
    CGFloat constrainedCoordinate = proposedCoordinate;

    if (splitView == self.verticalSplitView)
    {
        // the primary vertical split view is asking for a constrained size,
        // keep the right view no smaller than 120 points
        constrainedCoordinate = proposedCoordinate + 120.0;
    }
    else if (splitView == self.horizontalSplitView)
    {
        // the horizontal split view between mailboxes and activity view,
        // keep the top view at no smaller than 40 points
        constrainedCoordinate = proposedCoordinate + 40.0;
    }

    return constrainedCoordinate;
}

- (CGFloat)splitView:(NSSplitView *)splitView constrainMaxCoordinate:(CGFloat)proposedMaximumPosition ofSubviewAt:(NSInteger)dividerIndex
{
    CGFloat constrainedCoordinate = proposedMaximumPosition;

    if (splitView == self.horizontalSplitView)
    {
        // the horizontal split view between mailboxes and activity view,
        // keep the max size relative to the window size
        constrainedCoordinate = splitView.frame.size.height - 90;
    }

    return constrainedCoordinate;
}

@end
```

[Next](SplitViews-MailWindowController.h.md)[Previous](SplitViews-ActivityView.h.md)

