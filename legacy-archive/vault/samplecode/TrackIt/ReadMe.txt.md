---
title: TrackIt
apple_id: DTS10004139
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-03-18'
source_url: https://developer.apple.com/library/archive/samplecode/TrackIt/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:27:07.422692Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TrackIt](TrackIt.md)


[Next](main.m.md)[Previous](TrackIt.md)

# ReadMe.txt

```
TrackIt
=======

"TrackIt" is a Cocoa application that demonstrates how to use the NSTrackingArea class.  An NSTrackingArea object defines a region of an NSView that generates mouse-tracking and cursor-update events when the mouse is over that region and when the mouse leaves that region.  Depending on the options specified for each tracking area created, the owner of the tracking area (usually the NSView) receives the following messages: mouseEntered, mouseExited, mouseMoved, cursorUpdate.

TrackIt illustrates two methods for hosting and managing tracking areas.  The first is managing tracking areas outside the NSView code in its NSWindowController class.  The second is managing the tracking area from within the custom NSView itself.  The middle grey tracking area that shows cursor updaties is hosted inside the CustomView class.

Build Requirements
==================
Mac OS X 10.6.x or later

Runtime Requirements
====================
Mac OS X 10.5.x or later


Changes from Previous Versions
==============================
1.2 - Updated for Mac OS X 10.6, now builds 3-way Universal (ppc, i386, x86_64)
1.0 - first released

Copyright (C) 2006-2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](TrackIt.md)

