---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTViewController_m.html
archived_at: '2026-07-18T03:13:31.313835Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTWindowController.m.md)[Previous](LightTable-LTMaskLayer.h.md)

# LightTable/LTViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is the view controller for the main view in the window. It sets up the bindings between the document's array controller and the light table view that we could not set up in IB, defines the tools view animation, and provides utility functions to open and close the tools view.
 */

@import QuartzCore;
#import "LTViewController.h"

@interface LTViewController ()

@property (weak) IBOutlet NSLayoutConstraint *toolsViewPosition;

@end

@implementation LTViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do view setup here.

    // The managed object context and entity name of the array controller are set in Interface Builder,
    // but this is how it's done in code.
    // [self.slidesArrayController setManagedObjectContext:self.representedObject];
    // [self.slidesArrayController setEntityName:@"slide"];
    // [self.slidesArrayController prepareContent];


    // Set up the bindings between the LTView and the NSArrayController that points to Core Data data model.
    [self.lightTableView bind:@"slides" toObject:self.slidesArrayController withKeyPath:@"arrangedObjects" options:nil];

    [self.slidesArrayController bind:@"selectionIndexes" toObject:self.lightTableView withKeyPath:@"selectionIndexes" options:nil];

    // Set the state of tools view showing property.
    if (self.toolsViewPosition.constant > 0) {
        // The tools view is showing.
        self.toolsViewShowing = YES;
    } else {
        self.toolsViewShowing = NO;
    }

    // Define the animation that will show and hide the tools view.
    CABasicAnimation *animation = [CABasicAnimation animation];
    animation.timingFunction = [CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseOut];
    animation.duration = 0.5;
    // And add the animation to the constraint.
    self.toolsViewPosition.animations = @{@"constant": animation};

}

#pragma mark API

- (void)toggleToolsView {
    if (self.isToolsViewShowing) {
        // The toolsView is showing, so let's hide it.
        [self hideToolsView];
    } else {
        // The tooldView is hidden, so let's show it.
        [self showToolsView];
    }
}

- (void)hideToolsView {

    self.toolsViewPosition.animator.constant = 0;
    self.toolsViewShowing = NO;

}

- (void)showToolsView {

    self.toolsViewPosition.animator.constant = 200;
    self.toolsViewShowing = YES;
}


@end
```

[Next](LightTable-LTWindowController.m.md)[Previous](LightTable-LTMaskLayer.h.md)

