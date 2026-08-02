---
title: 'SplitViews: Using NSSplitView in a variety of different ways'
apple_id: DTS40011336
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/SplitViews/Listings/SplitViews_CollapseWindowController_m.html
archived_at: '2026-07-18T03:25:20.419853Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SplitViews: Using NSSplitView in a variety of different ways](SplitViews-%20Using%20NSSplitView%20in%20a%20variety%20of%20different%20ways.md)


[Next](SplitViews-ActivityView.m.md)[Previous](SplitViews-AppDelegate.h.md)

# SplitViews/CollapseWindowController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The NSWindowController subclass managing the collapsible split views. 
 */

#import "CollapseWindowController.h"

#define kMinContrainValue 100.0f


@implementation CollapseWindowController

#pragma mark - NSSplitViewDelegate methods

// -------------------------------------------------------------------------------
//  canCollapseSubview:
//
//  This delegate allows the collapsing of the first and last subview.
// -------------------------------------------------------------------------------
- (BOOL)splitView:(NSSplitView *)splitView canCollapseSubview:(NSView *)subview
{
    BOOL canCollapseSubview = NO;

    NSArray *splitViewSubviews = splitView.subviews;
    NSUInteger splitViewSubviewCount = splitViewSubviews.count;
    if (subview == splitViewSubviews[0] || subview == splitViewSubviews[(splitViewSubviewCount - 1)])
    {
        canCollapseSubview = YES;
    }
    return canCollapseSubview;
}

// -------------------------------------------------------------------------------
//  shouldCollapseSubview:subView:dividerIndex
//
//  This delegate allows the collapsing of the first and last subview.
// -------------------------------------------------------------------------------
- (BOOL)splitView:(NSSplitView *)splitView shouldCollapseSubview:(NSView *)subview forDoubleClickOnDividerAtIndex:(NSInteger)dividerIndex
{
    // yes, if you can collapse you should collapse it
    return YES;
}

// -------------------------------------------------------------------------------
//  constrainMinCoordinate:proposedCoordinate:index
// -------------------------------------------------------------------------------
- (CGFloat)splitView:(NSSplitView *)splitView constrainMinCoordinate:(CGFloat)proposedCoordinate ofSubviewAt:(NSInteger)index
{
    CGFloat constrainedCoordinate = proposedCoordinate;
    if (index == 0)
    {
        constrainedCoordinate = proposedCoordinate + kMinContrainValue;
    }
    return constrainedCoordinate;
}

// -------------------------------------------------------------------------------
//  constrainMaxCoordinate:proposedCoordinate:proposedCoordinate:index
// -------------------------------------------------------------------------------
- (CGFloat)splitView:(NSSplitView *)splitView constrainMaxCoordinate:(CGFloat)proposedCoordinate ofSubviewAt:(NSInteger)index
{
    CGFloat constrainedCoordinate = proposedCoordinate;
    if (index == (splitView.subviews.count - 2))
    {
        constrainedCoordinate = proposedCoordinate - kMinContrainValue;
    }

    return constrainedCoordinate;   
}

@end
```

[Next](SplitViews-ActivityView.m.md)[Previous](SplitViews-AppDelegate.h.md)

