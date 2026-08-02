---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATColorView_h.html
archived_at: '2026-07-18T03:26:13.283086Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATColorTableController.m.md)[Previous](TableViewPlayground-ATObjectTableRowView.m.md)

# TableViewPlayground/ATColorView.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic NSView subclass that supports having an animatable background color (NOTE: the animation only works when the view is layer backed).
 */

@import Cocoa;

@interface ATColorView : NSControl

@property (strong, nonatomic) NSColor *backgroundColor;
@property BOOL drawBorder;

@end
```

[Next](TableViewPlayground-ATColorTableController.m.md)[Previous](TableViewPlayground-ATObjectTableRowView.m.md)

