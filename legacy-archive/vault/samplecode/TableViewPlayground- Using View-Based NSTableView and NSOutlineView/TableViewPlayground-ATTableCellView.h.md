---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATTableCellView_h.html
archived_at: '2026-07-18T03:26:14.224445Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATColorView.m.md)[Previous](TableViewPlayground-ATComplexTableViewController.m.md)

# TableViewPlayground/ATTableCellView.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic subclass of NSTableCellView that adds some properties strictly for allowing access to the items in code.
 */

@import Cocoa;

@class ATColorView;

@interface ATTableCellView : NSTableCellView

@property (weak) IBOutlet NSTextField *subTitleTextField;
@property (weak) IBOutlet ATColorView *colorView;
@property (weak) IBOutlet NSProgressIndicator *progessIndicator;

- (void)layoutViewsForSmallSize:(BOOL)smallSize animated:(BOOL)animated;

@end
```

[Next](TableViewPlayground-ATColorView.m.md)[Previous](TableViewPlayground-ATComplexTableViewController.m.md)

