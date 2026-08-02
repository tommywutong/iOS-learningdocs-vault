---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATApplicationController_h.html
archived_at: '2026-07-18T03:26:12.938594Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATMainWindowController.m.md)[Previous](TableViewPlayground-ATBasicTableViewWindowController.m.md)

# TableViewPlayground/ATApplicationController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The main demo application controller. This class is the delegate for the main NSApp instance. This class manages the windows that are open, and allows the user to create a new one with the 'Available Sample Windows' table view. Bindings are used in the 'Available Sample Windows' table for the content. The TableView is bound to the tableContents, which is an array of NSDictionary objects that contain the information to disply.
 */

@import Cocoa;

@interface ATApplicationController : NSObject

@end
```

[Next](TableViewPlayground-ATMainWindowController.m.md)[Previous](TableViewPlayground-ATBasicTableViewWindowController.m.md)

