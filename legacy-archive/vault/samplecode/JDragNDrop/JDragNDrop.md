---
title: JDragNDrop
apple_id: DTS10000392
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JDragNDrop/Introduction/Intro.html
archived_at: '2026-07-18T03:13:09.403512Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# JDragNDrop

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates building a simple view to implement Drag-and-Drop functionality in Cocoa-Java. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X |

This project demonstrates building a simple view to implement drag and drop functionality in Cocoa-Java. CLASSES: < MyView.java > sublcassed from NSView. MyView creates a simple view and overrides the necessary init methods. The most important parts of MyView are registering for specific drag types and the concludeDragOperation method. All of the methods must be there for the drag and drop to work correctly, due to messaging of Cocoa. POSSIBLE ENHANCEMENTS: Modify constructor to allow different drag types and modify concludeDragOperation to operate on the different types.

[Next](main.m.md)

