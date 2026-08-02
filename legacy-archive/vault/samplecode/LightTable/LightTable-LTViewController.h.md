---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTViewController_h.html
archived_at: '2026-07-18T03:13:31.256596Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-DragTracker.h.md)[Previous](LightTable-LTSlide.m.md)

# LightTable/LTViewController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is the view controller for the main view in the window. It sets up the bindings between the document's array controller and the light table view that we could not set up in IB, defines the tools view animation, and provides utility functions to open and close the tools view.
 */

@import Cocoa;
#import "LTView.h"

@interface LTViewController : NSViewController
@property (weak) IBOutlet NSBox *toolsView;
@property (weak) IBOutlet LTView *lightTableView;

@property (weak) IBOutlet NSSlider *frameThicknessSlider;
@property (weak) IBOutlet NSSlider *cornerRadiusSlider;
@property (weak) IBOutlet NSArrayController *slidesArrayController;

@property (assign, nonatomic, getter=isToolsViewShowing) BOOL toolsViewShowing;

- (void)toggleToolsView;

@end
```

[Next](LightTable-DragTracker.h.md)[Previous](LightTable-LTSlide.m.md)

