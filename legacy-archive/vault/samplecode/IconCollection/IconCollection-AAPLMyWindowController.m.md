---
title: IconCollection
apple_id: DTS10004477
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/IconCollection/Listings/IconCollection_AAPLMyWindowController_m.html
archived_at: '2026-07-18T03:12:14.959849Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IconCollection](IconCollection.md)


[Next](IconCollection-AAPLMyViewController.m.md)[Previous](IconCollection-AAPLMyViewController.h.md)

# IconCollection/AAPLMyWindowController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This sample's main window controller object.
 */

#import "AAPLMyWindowController.h"

@interface AAPLMyWindowController ()

@property (weak) IBOutlet NSButton *alternateColors;
@property (weak) IBOutlet NSSegmentedControl *iconOrdering;

@end


#pragma mark -

@implementation AAPLMyWindowController

// -------------------------------------------------------------------------------
//  awakeFromNib
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    self.alternateColors.state = 0;
    self.iconOrdering.selectedSegment = 0;
}

@end
```

[Next](IconCollection-AAPLMyViewController.m.md)[Previous](IconCollection-AAPLMyViewController.h.md)

