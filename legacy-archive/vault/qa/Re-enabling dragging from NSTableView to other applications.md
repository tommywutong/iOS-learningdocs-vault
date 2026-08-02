---
title: Re-enabling dragging from NSTableView to other applications
apple_id: DTS10001743
resource_type: QA
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/qa/qa1220/_index.html
archived_at: '2026-07-18T02:30:12.644699Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1220

# Re-enabling dragging from NSTableView to other applications

## Q:  When I rebuild my application on Mac OS X version 10.2, my NSTableView loses the ability to drag-and-drop to other applications. How do I fix this?

A: When I rebuild my application on Mac OS X version 10.2, my NSTableView loses the ability to drag-and-drop to other applications. How do I fix this?

A bug in NSTableView in Mac OS X version 10.2 and later causes cross-application drags to not work without additional code from the application developer. Drag-and-drop within an application still works correctly. You can work around the bug by subclassing NSTableView and overriding -draggingSourceOperationMaskForLocal: to return the appropriate NSDragOperation (typically NSDragOperationCopy, depending upon what drag operation you want the drag-and-drop to perform). Only applications built on Mac OS X version 10.2.x are affected; applications built on 10.1.x are not affected.

This issue was resolved in Mac OS X version 10.4. For compatibility with that release and later, it is not necessary to subclass NSTableView in order for inter-application dragging that originates with the table view. It is, however, necessary to configure the table view by calling the setDraggingSourceOperationMask:forLocal: method. This is described in more detail in [Using Drag and Drop in Tables](https://developer.apple.com/documentation/Cocoa/Conceptual/TableView/Tasks/UsingDragAndDrop.html) at the end of the section "Beginning a Drag Operation".

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-02-08 | Updated for resolution of issue in Mac OS X 10.4. |
| 2002-12-02 | New document that explains how to re-enable drag-and-drop from NSTableViews to other applications |

