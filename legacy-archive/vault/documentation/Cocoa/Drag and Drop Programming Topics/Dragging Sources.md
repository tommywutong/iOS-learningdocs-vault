---
title: Drag and Drop Programming Topics
apple_id: 10000069i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/Concepts/dragsource.html
archived_at: '2026-07-15T07:15:05.814837Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drag and Drop Programming Topics](Introduction%20to%20Drag%20and%20Drop.md)


[Next](Dragging%20Destinations.md)[Previous](Introduction%20to%20Drag%20and%20Drop.md)

# Dragging Sources

A dragging session is initiated by the user clicking the mouse inside a window or view and moving the mouse. NSView and NSWindow implement the method `dragImage:at:offset:event:pasteboard:source:slideBack:` to handle the dragging session. You invoke this method in the `mouseDown:` or `mouseDragged`: method of your subclass of NSView or NSWindow. You provide an image to display during the drag, a pasteboard holding the data, and an object that acts as the “owner”, or dragging source, of the data. During the dragging session, the dragging source is sent messages defined by the NSDraggingSource protocol to perform any necessary actions, described below.

Only one of the NSDraggingSource methods needs to be implemented: `draggingSourceOperationMaskForLocal:`. This method declares what types of operations the source allows to be performed. [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe3tmljrga2tqnjufvbuuqsgi5feksi) lists the available drag operations. (In Java, the constants are defined in the NSDraggingInfo namespace and lack the `NS` prefix.) The method should return a bitwise-OR combination of the allowed types or `NSDragOperationNone` if no operations are allowed.

__Table 1__  Available drag operations

| Dragging Operation | Meaning |
| `NSDragOperationCopy` | The data represented by the image can be copied. |
| `NSDragOperationLink` | The data can be shared. |
| `NSDragOperationGeneric` | The operation can be defined by the destination. |
| `NSDragOperationPrivate` | The operation is negotiated privately between the source and the destination. |
| `NSDragOperationMove` | The data can be moved. |
| `NSDragOperationDelete` | The data can be deleted. |
| `NSDragOperationEvery` | All of the above |
| `NSDragOperationAll` | Deprecated. Use `NSDragOperationEvery` instead. |
| `NSDragOperationNone` | No drag operations are allowed. |

The allowed operations may differ if the drag is occurring entirely within your application or between your application and another. The flag passed to `draggingSourceOperationMaskForLocal:` indicates whether it is a local, or internal, drag.

The user can press modifier keys to further select which operation to perform. If the control, option, or command key is pressed, the source’s operation mask is filtered to only contain the operations given in [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe3tmljrga2timzvfvbuuqsfi5feesq). To prevent modifiers from altering the mask, your dragging source should implement `ignoreModifierKeysWhileDragging` and return `YES`.

__Table 2__  Drag operations selected with modifier keys

| Modifier Key | Dragging Operation |
| Control | `NSDragOperationLink` |
| Option | `NSDragOperationCopy` |
| Command | `NSDragOperationGeneric` |

During the course of the drag, the source object is sent a series of messages to notify it of the status of the drag operation. At the very beginning of the drag, the source is sent the message `draggedImage:beganAt:`. Each time the dragged image moves, the source is sent a `draggedImage:movedTo:` message. Finally, when the user has released the mouse button and the destination has either performed the drop operation or rejected it, the source is sent a `draggedImage:endedAt:operation:` message. The _operation_ argument is the drag operation the destination performed or `NSDragOperationNone` if the drag failed. (In Java, these method names are `startedDraggingImage`, `movedDraggingImage`, and `finishedDraggingImage`.)

The dragging source generally does not need to implement any of these methods. If you are going to support the `NSDragOperationMove` or `NSDragOperationDelete` operations, however, you do need to implement `draggedImage:endedAt:operation:` to remove the dragged data from the source. (Note that an `NSDragOperationDelete` operation is requested when dragging any object to the Trash icon in the dock.)

The image that is dragged in a dragging session is simply an image that represents the data on the pasteboard. Although a dragging destination can access the image, its primary concern is with the pasteboard data that the image represents—the dragging operation that a destination ultimately performs is on the pasteboard data, not on the image itself.

When the dragging session is started by using the NSView method `dragFile:fromRect:slideBack:event:`, NSView uses the file’s Finder icon for the image. For your own custom drags, you need to construct a suitable image. Possibilities include a semi-transparent snapshot of the displayed data, such as the selected section of text, or a symbolic representation of the data, such as a table icon when dragging spreadsheet data.

[Next](Dragging%20Destinations.md)[Previous](Introduction%20to%20Drag%20and%20Drop.md)

