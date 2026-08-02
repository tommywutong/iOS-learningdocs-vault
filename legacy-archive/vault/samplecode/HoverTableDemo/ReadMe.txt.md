---
title: HoverTableDemo
apple_id: DTS40011082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/HoverTableDemo/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:11:56.888671Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HoverTableDemo](HoverTableDemo.md)


[Next](HoverTableDemo-HoverTableDemoAppDelegate.h.md)[Previous](HoverTableDemo.md)

# ReadMe.txt

```
### HoverTableDemo ###

===========================================================================
DESCRIPTION:

Demonstrates how to use view-based NSTableViews in your application, complete with custom drawing and mouse tracking.

It subclasses NSTableView's drawGridInClipRect for custom grid drawing as well as "setFrameSize:size" to invalidate more elements when live-resizing occurs.

The sample implements a custom NSTableRowView class that tracks the mouse to achieve an elegant selection appearance.  The overrides for this include:

Override point to draw a custom background:
    drawBackgroundInRect:dirtyRect

Override point for drawing the (horizontal) separator:
    drawSeparatorInRect:dirtyRect

Override point for drawing the selection:
    drawSelectionInRect:dirtyRect

===========================================================================
BUILD REQUIREMENTS:

Xcode 4.4, OS X 10.8

===========================================================================
RUNTIME REQUIREMENTS:

OS X 10.7 or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.1
- Upgraded to OS X 10.8 to eliminate build warnings, now uses NSDictionary to back each table row, App Sandboxing enabled.

Version 1.0
- First version.

===========================================================================
Copyright (C) 2011-2012 Apple Inc. All rights reserved.
```

[Next](HoverTableDemo-HoverTableDemoAppDelegate.h.md)[Previous](HoverTableDemo.md)

