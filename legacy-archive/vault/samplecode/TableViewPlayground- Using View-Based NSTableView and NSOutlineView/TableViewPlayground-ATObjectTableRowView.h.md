---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATObjectTableRowView_h.html
archived_at: '2026-07-18T03:26:14.059876Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATBasicTableViewWindowController.h.md)[Previous](TableViewPlayground-ATColorTableController.h.md)

# TableViewPlayground/ATObjectTableRowView.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A simple subclass of NSTableRowView that introduces an objectValue property.
 */

@import Cocoa;

@interface ATObjectTableRowView : NSTableRowView {
@private
    id _objectValue;
}

@property(strong) id objectValue;

@end
```

[Next](TableViewPlayground-ATBasicTableViewWindowController.h.md)[Previous](TableViewPlayground-ATColorTableController.h.md)

