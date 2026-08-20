---
title: LayoutManagerDemo
apple_id: DTS10000394
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/LayoutManagerDemo/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:13:29.617729Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LayoutManagerDemo](LayoutManagerDemo.md)


[Next](LayoutManagerDemo-ApplicationDelegate.h.md)[Previous](LayoutManagerDemo.md)

# ReadMe.txt

```
LayoutManagerDemo
=================

ABOUT:

 This application demonstrates interrogating the layout manager for information about   text layout, and the use of temporary attributes to color text.  Specifically, we provide rollover coloring of text--one color for the line, another for the word,    and a third for the character under the mouse.  A subclass of NSTextView is used,   but solely for the purpose of obtaining mouse events.  The interesting portion of    the code involves the conversion of mouse coordinates to a particular glyph and   character index, then determining the corresponding line and word, and finally    using temporary attributes for coloring. 

===========================================================================
BUILD REQUIREMENTS:

Xcode 4.3, Mac OS X 10.7.x or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X 10.6.x Snow Leopard or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

1.2 - Upgraded to Xcode 4.3 and Mac OS X 10.7
1.1 - Project updated for Xcode 4.
1.0 - First version.

===========================================================================
Copyright (C) 2001-2012 Apple Inc. All rights reserved.
```

[Next](LayoutManagerDemo-ApplicationDelegate.h.md)[Previous](LayoutManagerDemo.md)

