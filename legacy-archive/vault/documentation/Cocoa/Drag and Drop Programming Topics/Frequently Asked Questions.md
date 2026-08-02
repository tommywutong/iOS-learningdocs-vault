---
title: Drag and Drop Programming Topics
apple_id: 10000069i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/Tasks/faq.html
archived_at: '2026-07-15T07:15:07.799448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drag and Drop Programming Topics](Introduction%20to%20Drag%20and%20Drop.md)


[Next](Document%20Revision%20History.md)[Previous](Dragging%20Files.md)

# Frequently Asked Questions

This document answers commonly asked questions about the drag and drop capabilities of the Application Kit. This includes information on HFS promise drags and special information regarding cross-application dragging from NSTableView objects.

This document covers the following subjects:

- [HFS Promise Drag](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dqljzgy4teoi)
- [Cross-Application Drag and Drop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dqljzg4ytgoi)

The questions addressed in this section include:

- [How Do I Set a Custom Drag Image When Doing an HFS Promise Drag in Cocoa?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dqljzg42dmma)
- [How Do I Add Other Pasteboard Types to an HFS Promise Drag in Cocoa?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dqljzg42tcmy)

NSView’s [dragPromisedFilesOfTypes:fromRect:source:slideBack:event:](https://developer.apple.com/documentation/appkit/nsview/1483598-dragpromisedfilesoftypes) method doesn't provide a way to set the drag image to be used when dragging an HFS promise file. However, this method calls another NSView method, [dragImage:at:offset:event:pasteboard:source:slideBack:](https://developer.apple.com/documentation/appkit/nsview/1483279-dragimage) in its implementation, which does provide a parameter for an NSImage to be used as the drag image. So, to set a custom drag image, simply override `dragImage:at:offset:event:pasteboard:source:slideBack:`, setup your custom image, invoke super's `dragImage:at:offset:event:pasteboard:source:slideBack:` and pass in your custom drag image.

NSView's [dragPromisedFilesOfTypes:fromRect:source:slideBack:event:](https://developer.apple.com/documentation/appkit/nsview/1483598-dragpromisedfilesoftypes) method doesn't provide a means to add other pasteboard types to the HFS Promise data, because it doesn't expose the pasteboard that it uses. However, there is a workaround to add other pasteboard type data. `dragPromisedFilesOfTypes:fromRect:source:slideBack:event:` calls NSView's [dragImage:at:offset:event:pasteboard:source:slideBack:](https://developer.apple.com/documentation/appkit/nsview/1483279-dragimage) method in its implementation. So, you can override `dragImage:at:offset:event:pasteboard:source:slideBack:`, add any additional pasteboard types you need, and then invoke super's `dragImage:at:offset:event:pasteboard:source:slideBack:` to allow everything to continue as before.

The questions addressed in this section include:

- [When I Rebuild My application on OS X version 10.2, My NSTableView Loses the Ability to Drag-And-Drop to Other Applications. How Do I Fix This?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dqljzg4ytkoi)

A bug in NSTableView in OS X version 10.2 and later causes cross-application drags to not work without additional code from the application developer. Drag-and-Drop within an application still works correctly.

You can work around the bug by subclassing NSTableView and overriding `draggingSourceOperationMaskForLocal:` to return the appropriate `NSDragOperation` (typically `NSDragOperationCopy`, depending upon what drag operation you want the drag-and-drop to perform). Only applications built on OS X version 10.2 and later are affected; applications built on OS X version 10.1.x are not affected.

In OS X v10.4 you can work around this bug without subclassing. By default the NSTableView implementation of `draggingSourceOperationMaskForLocal:` disallows dragging to destinations outside of the application while allowing any type of drag within the same application. You can change this behavior by sending the table view a `setDraggingSourceOperationMask:forLocal:` message. Passing a value of `YES` as the second parameter indicates that specified mask applies when the destination object is in the same application. Passing a value of `NO` indicates that the specified mask applies when the destination object in an application outside the receiver's application. The masks are archived with the table view.

[Next](Document%20Revision%20History.md)[Previous](Dragging%20Files.md)

