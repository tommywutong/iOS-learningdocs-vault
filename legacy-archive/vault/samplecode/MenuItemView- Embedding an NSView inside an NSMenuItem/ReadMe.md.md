---
title: 'MenuItemView: Embedding an NSView inside an NSMenuItem'
apple_id: DTS10004136
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MenuItemView/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:14:34.786425Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuItemView: Embedding an NSView inside an NSMenuItem](MenuItemView-%20Embedding%20an%20NSView%20inside%20an%20NSMenuItem.md)


[Next](MenuItemView-TrackView.h.md)[Previous](MenuItemView-main.m.md)

# ReadMe.md

```
# MenuItemView

## Description

MenuItemView is a Cocoa sample application that demonstrates how to embed an NSView inside an NSMenuItem in macOS.  This sample is intended to show how this is done with various user interface elements such as controls and the menu bar.

In the menu bar, "Custom" will contain the menu with embedded NSViews.  This same menu can also be found in the main window's controls as well as in the image view's contextual menu.  It is designed to show how this menu can be applied to different areas of the user interface.

Keep in mind should you choose to share this menu in different areas (like in this sample), that you cannot share the same menu instance among the various places.  You need to makes copies of the menu and its embedded views where ever you apply them.

## Requirements

### Build

macOS SDK 10.12.2 or later.

### Runtime

macOS 10.0 or later

Copyright (C) 2006-2017 Apple Inc. All rights reserved.
```

[Next](MenuItemView-TrackView.h.md)[Previous](MenuItemView-main.m.md)

