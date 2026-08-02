---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATSampleWindowRowView_h.html
archived_at: '2026-07-18T03:26:14.128015Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATComplexOutlineController.m.md)[Previous](TableViewPlayground-ATApplicationController.m.md)

# TableViewPlayground/ATSampleWindowRowView.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 ATSampleWindowRowView implementation. This class is used because the NIB has an ATSampleWindowRowView placed in it with a special key of NSTableViewRowViewKey. NSTableView first looks for a view with that key for the row view, if the delegate method tableView:rowViewForRow: is not used.
 */

@import Cocoa;

@interface ATSampleWindowRowView : NSTableRowView

@end
```

[Next](TableViewPlayground-ATComplexOutlineController.m.md)[Previous](TableViewPlayground-ATApplicationController.m.md)

