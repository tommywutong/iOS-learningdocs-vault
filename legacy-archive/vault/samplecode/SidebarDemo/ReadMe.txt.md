---
title: SidebarDemo
apple_id: DTS40010893
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-05-02'
source_url: https://developer.apple.com/library/archive/samplecode/SidebarDemo/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:46.134495Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SidebarDemo](SidebarDemo.md)


[Next](main.m.md)[Previous](SidebarDemo.md)

# ReadMe.txt

```
### SidebarDemo ###

===========================================================================
DESCRIPTION:

This example demonstrates a basic View Based OutlineView implementation that implements a source list sidebar.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X 10.7 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X 10.7 or later

===========================================================================
PACKAGING LIST:

SidebarDemoAppDelegate.h/.m: The basic app delegate implementation that is also the main controller for the window. It implements the NSOutlineView dataSource and delegate methods to provide a source list. 

SidebarTableCellView.h/.m: An NSTableCellView subclass that adds an NSButton outlet. It also performs layout in -viewWillDraw.

ContentView[1-3].xib: Sample content view used to the right of the sidebar.

SidebarCell.xib: SidebarTableCellView instance in the XIB file. A basic NSTextField and NSImage are used, along with a button to use as an unread indicator or "action" button. The identifier for the cell is set to @"MainCell". This string is used in the SidebarDemoAppDelegate.m by calling [outlineView makeViewWithIdentifier:@"MainCell" owner:self] to load the XIB, if needed.

HeaderTextFieldCell.xib: A custom header cell. The identifier for the cell is set to @"HeaderTextField". This string is used in the SidebarDemoAppDelegate.m by calling [outlineView makeViewWithIdentifier:@"HeaderTextField" owner:self] to load the XIB, if needed.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](SidebarDemo.md)

