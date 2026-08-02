---
title: 'ButtonMadness: Creating and Customizing AppKit Controls'
apple_id: DTS10004430
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/ButtonMadness/Listings/ButtonMadness_DropDownButton_m.html
archived_at: '2026-07-18T03:02:21.091307Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ButtonMadness: Creating and Customizing AppKit Controls](ButtonMadness-%20Creating%20and%20Customizing%20AppKit%20Controls.md)


[Next](LICENSE.txt.md)[Previous](ButtonMadness-MyWindowController.m.md)

# ButtonMadness/DropDownButton.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSButton subclass for supporting drop down menus.
 */

#import "DropDownButton.h"

@implementation DropDownButton

// -------------------------------------------------------------------------------
//  awakeFromNib
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    [super awakeFromNib];
    if (self.menu != nil)
    {
        [self setUsesMenu:YES];
    }
}

// -------------------------------------------------------------------------------
//  setUsesMenu:flag
// -------------------------------------------------------------------------------
- (void)setUsesMenu:(BOOL)flag
{
    if (popUpCell == nil && flag)
    {
        popUpCell = [[NSPopUpButtonCell alloc] initTextCell:@""];
        [popUpCell setPullsDown:YES];
        popUpCell.preferredEdge = NSMaxYEdge;
    }
    else if (popUpCell != nil && !flag)
    {
        popUpCell = nil;
    }
}

// -------------------------------------------------------------------------------
//  usesMenu
// -------------------------------------------------------------------------------
- (BOOL)usesMenu
{
    return (popUpCell != nil);
}

// -------------------------------------------------------------------------------
//  runPopUp:theEvent
// -------------------------------------------------------------------------------
- (void)runPopUp:(NSEvent *)theEvent
{
    // create the menu the popup will use
    NSMenu *popUpMenu = [self.menu copy];
    [popUpMenu insertItemWithTitle:@"" action:NULL keyEquivalent:@"" atIndex:0];    // blank item at top
    popUpCell.menu = popUpMenu;

    // and show it
    [popUpCell performClickWithFrame:self.bounds inView:self];


    [self setNeedsDisplay: YES];
}

// -------------------------------------------------------------------------------
//  mouseDown:theEvent
// -------------------------------------------------------------------------------
- (void)mouseDown:(NSEvent *)theEvent
{
    if (self.usesMenu)
    {
        [self runPopUp:theEvent];
    }
    else
    {
        [super mouseDown:theEvent];
    }
}

@end
```

[Next](LICENSE.txt.md)[Previous](ButtonMadness-MyWindowController.m.md)

