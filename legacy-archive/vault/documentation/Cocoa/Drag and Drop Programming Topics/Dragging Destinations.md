---
title: Drag and Drop Programming Topics
apple_id: 10000069i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/Concepts/dragdestination.html
archived_at: '2026-07-15T07:15:05.142249Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drag and Drop Programming Topics](Introduction%20to%20Drag%20and%20Drop.md)


[Next](Receiving%20Drag%20Operations.md)[Previous](Dragging%20Sources.md)

# Dragging Destinations

To receive drag operations, you must register the pasteboard types that your window or view will accept by sending the object a [registerForDraggedTypes:](https://developer.apple.com/documentation/appkit/nsview/1483578-registerfordraggedtypes) message, defined in both NSWindow and NSView, and implement several methods from the NSDraggingDestination protocol. During a dragging session, a candidate destination receives NSDraggingDestination messages only if the destination is registered for a pasteboard type that matches the type of the pasteboard data being dragged. The destination receives these messages as an image enters, moves around inside, and then exits or is released within the destination’s boundaries.

Although NSDraggingDestination is declared as an informal protocol, the NSWindow and NSView subclasses you create to adopt the protocol need only implement those methods that are pertinent. (The NSWindow and NSView classes provide private implementations for all of the methods.) Either a window object or its delegate may implement these methods; however, the delegate’s implementation takes precedence if there are implementations in both places.

Each of the NSDraggingDestination methods sports a single argument: _sender_, the object that invoked the method. Within its implementations of the NSDraggingDestination methods, the destination can send NSDraggingInfo protocol messages to _sender_ to get more information on the current dragging session, such as querying for the dragging pasteboard or the source’s operations mask. In Java, _sender_ is an NSDragDestination object, which implements the NSDraggingInfo interface.

Although a standard dragging pasteboard (obtained using `[NSPasteboard pasteboardWithName:NSDragPboard]`) is provided as a convenience in getting the pasteboard for dragging data, there is NO guarantee that this will be the pasteboard used in a cross-process drag. Thus, to guarantee getting the correct pasteboard, your code should use `[sender draggingPasteboard]`.

The six NSDraggingDestination methods are invoked in a distinct order:

- As the image is dragged into the destination’s boundaries, the destination is sent a [draggingEntered:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416019-draggingentered) message. The method should return a value that indicates which dragging operation the destination will perform.
- While the image remains within the destination, a series of [draggingUpdated:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415998-draggingupdated) messages are sent. The method should return a value that indicates which dragging operation the destination will perform.
- If the image is dragged out of the destination, [draggingExited:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416056-draggingexited) is sent and the sequence of NSDraggingDestination messages stops. If it re-enters, the sequence begins again (with a new [draggingEntered:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416019-draggingentered) message).
- When the image is released, it either slides back to its source (and breaks the sequence) or a [prepareForDragOperation:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416066-preparefordragoperation) message is sent to the destination, depending on the value returned by the most recent invocation of [draggingEntered:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416019-draggingentered) or [draggingUpdated:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415998-draggingupdated).
- If the [prepareForDragOperation:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416066-preparefordragoperation) message returned `YES`, a [performDragOperation:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415970-performdragoperation) message is sent.
- Finally, if [performDragOperation:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415970-performdragoperation) returned `YES`, [concludeDragOperation:](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416010-concludedragoperation) is sent.

[Next](Receiving%20Drag%20Operations.md)[Previous](Dragging%20Sources.md)

