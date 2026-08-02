---
title: Drag and Drop Programming Topics
apple_id: 10000069i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/Tasks/acceptingdrags.html
archived_at: '2026-07-15T07:15:07.167262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drag and Drop Programming Topics](Introduction%20to%20Drag%20and%20Drop.md)


[Next](Dragging%20Files.md)[Previous](Dragging%20Destinations.md)

# Receiving Drag Operations

This document shows sample code which allows a view (or window) to accept dragging sessions for several data types, performing different drag operations based on the dragged type. The sample implementation can accept either a color or a file. A dragged color will be copied while the file will be either linked or copied.

Before a view can receive a drag operation, you need to register the data types that it can accept by invoking its `registerForDraggedTypes:`, like this:

```
[self registerForDraggedTypes:[NSArray arrayWithObjects:
            NSColorPboardType, NSFilenamesPboardType, nil]];
```

Now, any time a dragging session that consists of either of these data types enters the view’s bounds, the view is sent a series of NSDraggingDestination messages. The code below is a simple example of the initial method that gets sent: `draggingEntered:`. The method obtains the dragging pasteboard and available drag operations from the _sender_ object. If the pasteboard contains color data and the source object permits dragging, the method returns `NSDragOperationGeneric`, indicating that the destination permits dragging of the color data on the pasteboard. If the pasteboard contains a file name and the source object permits linking, the method returns `NSDragOperationLink`, indicating that the destination permits the link. If the source does not allow linking, the destination also checks if a copy operation is allowed instead, returning `NSDragOperationCopy` if so. Failing all these tests, the method returns `NSDragOperationNone`.

```objc
- (NSDragOperation)draggingEntered:(id <NSDraggingInfo>)sender {
    NSPasteboard *pboard;
    NSDragOperation sourceDragMask;

    sourceDragMask = [sender draggingSourceOperationMask];
    pboard = [sender draggingPasteboard];

    if ( [[pboard types] containsObject:NSColorPboardType] ) {
        if (sourceDragMask & NSDragOperationGeneric) {
            return NSDragOperationGeneric;
        }
    }
    if ( [[pboard types] containsObject:NSFilenamesPboardType] ) {
        if (sourceDragMask & NSDragOperationLink) {
            return NSDragOperationLink;
        } else if (sourceDragMask & NSDragOperationCopy) {
            return NSDragOperationCopy;
        }
    }
    return NSDragOperationNone;
}
```

As the dragging session continues, the destination is sent `draggingUpdated:` messages. You only need to implement this if the destination needs to know the current position of the dragged image, either to change the dragging operation or to update any visual feedback, such as an insertion point, you are providing. If not implemented, NSView assumes the dragging operation is unchanged from the `draggingEntered:` invocation. If the dragging session leaves the view’s bounds, the `draggingExited:` method is invoked. Implement this if you need to clean up after one of the preceding messages, such as removing the visual feedback.

When the image is dropped with a drag operation other than `NSDragOperationNone`, the destination is sent a `prepareForDragOperation:` message followed by `performDragOperation:` and `concludeDragOperation:`. You can cancel the drag by returning `NO` from either of the first two methods.

You do the bulk of the data handling in the `performDragOperation:` method; the other two methods are implemented only if necessary. The following code sample shows a possible implementation of this method. The method again checks the pasteboard for the available data and, if necessary, it also checks the dragging source’s operation mask for the available operations.

```objc
- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender {
    NSPasteboard *pboard;
    NSDragOperation sourceDragMask;

    sourceDragMask = [sender draggingSourceOperationMask];
    pboard = [sender draggingPasteboard];

    if ( [[pboard types] containsObject:NSColorPboardType] ) {
        // Only a copy operation allowed so just copy the data
        NSColor *newColor = [NSColor colorFromPasteboard:pboard];
        [self setColor:newColor];
    } else if ( [[pboard types] containsObject:NSFilenamesPboardType] ) {
        NSArray *files = [pboard propertyListForType:NSFilenamesPboardType];

        // Depending on the dragging source and modifier keys,
        // the file data may be copied or linked
        if (sourceDragMask & NSDragOperationLink) {
            [self addLinkToFiles:files];
        } else {
            [self addDataFromFiles:files];
        }
    }
    return YES;
}
```

[Next](Dragging%20Files.md)[Previous](Dragging%20Destinations.md)

