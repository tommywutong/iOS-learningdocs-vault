---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTWindowController_m.html
archived_at: '2026-07-18T03:13:31.644164Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTView.h.md)[Previous](LightTable-LTViewController.m.md)

# LightTable/LTWindowController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is the window controller for our document window. It enables the menu item to toggle the tools view.
 */

#import "LTWindowController.h"
#import "LTViewController.h"

@implementation LTWindowController

#pragma mark Window cascading
- (void)windowDidLoad {
    [super windowDidLoad];
    self.shouldCascadeWindows = YES;
}

#pragma mark NSMenuValidation
- (BOOL)validateMenuItem:(NSMenuItem *)menuItem {

    LTViewController *ltViewController = (LTViewController *)self.contentViewController;

    if (menuItem.action == @selector(toggleToolsViewShown:)) {
        if (ltViewController.isToolsViewShowing) {
            menuItem.state = NSOnState;
        } else {
            menuItem.state = NSOffState;
        }
    }

    return YES;
}


#pragma mark API

// Tell the view controller to toggle the tools view.
- (IBAction)toggleToolsViewShown:(id)sender {
    LTViewController *ltViewController = (LTViewController *)self.contentViewController;
    [ltViewController toggleToolsView];
}


@end
```

[Next](LightTable-LTView.h.md)[Previous](LightTable-LTViewController.m.md)

