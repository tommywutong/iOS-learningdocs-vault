---
title: 'MenuItemView: Embedding an NSView inside an NSMenuItem'
apple_id: DTS10004136
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MenuItemView/Listings/MenuItemView_TrackView_m.html
archived_at: '2026-07-18T03:14:34.616085Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuItemView: Embedding an NSView inside an NSMenuItem](MenuItemView-%20Embedding%20an%20NSView%20inside%20an%20NSMenuItem.md)


[Next](MenuItemView-ImageMenuItemView.m.md)[Previous](MenuItemView-ViewController.m.md)

# MenuItemView/TrackView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The NSView that handles the label color tracking.
 */

#import "TrackView.h"

@interface TrackView ()

@property (strong) NSMutableArray *viewTrackingAreas;

@property NSInteger whichTrackedID;   // indicates the currently tracked label
@property BOOL trackEntered;          // indicates we are currently inside a label tracking area

@end


#pragma mark -

@implementation TrackView

// key for dictionary in NSTrackingAreas's userInfo
NSString *kTrackerKey = @"whichTracker";

// key values for dictionary in NSTrackingAreas's userInfo,
// which tracking area is being tracked
typedef NS_ENUM(NSInteger, trackingAreaIDs) {
    kTrackingArea1 = 1,
    kTrackingArea2,
    kTrackingArea3,
    kTrackingArea4,
    kTrackingArea5,
    kTrackingArea6,
    kTrackingArea7,
    kTrackingArea8
};

// -------------------------------------------------------------------------------
//  awakeFromNib:
//
//  Setup the tracking areas for each colored dot.  Each colored dot is a separate
//  NSView for easy management/tracking purposes.
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    [super awakeFromNib];
    [self setupTrackingAreas];
}

// -------------------------------------------------------------------------------
//  setupTrackingAreas:
// -------------------------------------------------------------------------------
- (void)setupTrackingAreas
{
    if (self.viewTrackingAreas == nil)
    {
        // load all the suviews and add tracking areas to them
        NSArray *viewsToFrame = self.subviews;

        _viewTrackingAreas = [NSMutableArray array];    // keep all tracking areas in an array

        // determine the tracking options
        NSTrackingAreaOptions trackingOptions = NSTrackingEnabledDuringMouseDrag |
                                                NSTrackingMouseEnteredAndExited |
                                                NSTrackingActiveInActiveApp |
                                                NSTrackingActiveAlways;

        for (NSUInteger index = 1; index < self.subviews.count; index++)
        {
            // make tracking data (to be stored in NSTrackingArea's userInfo)
            // so we can later determine which tracking area is focused on
            //
            NSDictionary *trackerData = @{kTrackerKey: @(index)};

            NSTrackingArea *trackingArea = [[NSTrackingArea alloc]
                                                initWithRect:[viewsToFrame[index-1] frame]
                                                // note: since we are working with this view's coordinate system,
                                                // we need to  use the 'frame' for each subview instead of its bounds
                                                options:trackingOptions
                                                owner:self
                                                userInfo:trackerData];

            [self.viewTrackingAreas addObject:trackingArea];    // keep track of this tracking area for later disposal
            [self addTrackingArea:trackingArea];    // add the tracking area to the view/window
        }
    }
}

// -------------------------------------------------------------------------------
//  drawRect:rect
//
//  Returns the NSColor corresponding to the sub-view index.
// -------------------------------------------------------------------------------
- (NSColor *)colorForViewIndex:(NSInteger)viewIndex
{
    NSColor *returnColor = nil;
    switch (viewIndex)
    {
        case kTrackingArea1:    // grey
            returnColor = [NSColor grayColor];
            break;

        case kTrackingArea2:    // purple
            returnColor = [NSColor purpleColor];
            break;

        case kTrackingArea3:    // blue
            returnColor = [NSColor blueColor];
            break;

        case kTrackingArea4:    // green
            returnColor = [NSColor greenColor];
            break;

        case kTrackingArea5:    // yellow
            returnColor = [NSColor yellowColor];
            break;

        case kTrackingArea6:    // orange
            returnColor = [NSColor orangeColor];
            break;

        case kTrackingArea7:    // red
            returnColor = [NSColor redColor];
            break;

        case kTrackingArea8:    // none (black)
            returnColor = [NSColor blackColor];
            break;
    }
    return returnColor;
}

// -------------------------------------------------------------------------------
//  drawRect:rect
//
//  Examine all the sub-view colored dots and color them with their appropriate colors.
// -------------------------------------------------------------------------------
- (void)drawRect:(NSRect)rect
{
    NSArray *viewsToFrame = self.subviews;

    NSInteger viewCount = viewsToFrame.count - 1;
    for (NSInteger index = 1; index <= viewCount; index++)
    {
        if (self.whichTrackedID == index)
        {
            // obtain the bezier path (a filled circle) to draw in
            NSBezierPath *theFill = [NSBezierPath bezierPathWithOvalInRect:[viewsToFrame[self.whichTrackedID - 1] frame]];

            NSColor *theColor = [self colorForViewIndex:self.whichTrackedID];

            if (self.trackEntered)
            {
                // if we are tracking inside any label, we want to brighten the color to show selection feedback

                // take the current label color and brighten it
                CGFloat hue, saturation, brightness, alpha;
                [[theColor
                    colorUsingColorSpaceName:NSDeviceRGBColorSpace] getHue:&hue
                    saturation:&saturation brightness:&brightness alpha:&alpha];

                theColor = [NSColor colorWithDeviceHue:hue saturation:saturation-.60 brightness:brightness + 40.0 alpha:alpha];
            }

            // finally, render the color change (light or dark)
            [self lockFocus];
            [theColor set];
            [theFill fill];
            [self unlockFocus];
        }
        else
        {
            // obtain the bezier path (a filled circle) to draw in
            NSBezierPath *theFill = [NSBezierPath bezierPathWithOvalInRect:[viewsToFrame[index-1] frame]];

            // fill the area with the appropriate color
            [[self colorForViewIndex:index] set];
            [theFill fill];
        }
    }
}

// -------------------------------------------------------------------------------
//  getTrackerIDFromDict:dict
//
//  Used in obtaining dictionary entry info from the 'userData', used by each
//  mouse event method.  It helps determine which tracking area is being tracked.
// -------------------------------------------------------------------------------
- (int)getTrackerIDFromDict:(NSDictionary *)dict
{
    id whichTracker = dict[kTrackerKey];
    return [whichTracker intValue];
}

// -------------------------------------------------------------------------------
//  mouseEntered:event
//
//  Because we installed NSTrackingArea to our NSImageView, this method will be called.
// -------------------------------------------------------------------------------
- (void)mouseEntered:(NSEvent *)event
{
    // which tracking area is being tracked?
    _whichTrackedID = [self getTrackerIDFromDict:event.userData];
    _trackEntered = YES;

    [self setNeedsDisplay:YES]; // force update the currently tracked label back to its original color
}

// -------------------------------------------------------------------------------
//  mouseExited:event
//
//  Because we installed NSTrackingArea to our NSImageView, this method will be called.
// -------------------------------------------------------------------------------
- (void)mouseExited:(NSEvent *)event
{
    // which tracking area is being tracked?
    _whichTrackedID = [self getTrackerIDFromDict:event.userData];
    _trackEntered = NO;

    [self setNeedsDisplay:YES]; // force update the currently tracked label to a lighter color
}

// -------------------------------------------------------------------------------
//  mouseDown:event
// -------------------------------------------------------------------------------
- (void)mouseUp:(NSEvent*)event
{
    NSPoint mousePoint = [self convertPoint:event.locationInWindow fromView:nil];

    // figure out which label color was clicked on at mouseUp time
    NSArray *labelViews = self.subviews;
    for (NSUInteger index = 1; index < labelViews.count; index++)
    {
        NSRect labelRect = [labelViews[index-1] frame];
        if (NSPointInRect(mousePoint, labelRect))
        {
            // here you would respond to the particular label selection...
            NSLog(@"label %ld was selected", index);
        }
    }

    // on mouse up, we want to dismiss the menu being tracked
    NSMenu *menu = self.enclosingMenuItem.menu;
    [menu cancelTracking];

    // we are no longer tracking, reset the tracked label color (if any)
    _whichTrackedID = NSNotFound;
    [self setNeedsDisplay:YES];
}

@end
```

[Next](MenuItemView-ImageMenuItemView.m.md)[Previous](MenuItemView-ViewController.m.md)

