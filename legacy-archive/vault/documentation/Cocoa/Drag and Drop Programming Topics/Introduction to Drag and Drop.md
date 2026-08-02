---
title: Drag and Drop Programming Topics
apple_id: 10000069i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html
archived_at: '2026-07-15T07:15:05.825893Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Dragging%20Sources.md)

# Introduction to Drag and Drop

Cocoa gives you the ability to implement sophisticated drag-and-drop capabilities both within your application and between applications. This programming topic describes how you can implement drag-and-drop with just a few methods.

In the text here and in the dragging protocol descriptions, the term dragging session is the entire process during which an image is selected, dragged, released, and absorbed or rejected by the destination. A dragging operation is the action that the destination takes in absorbing the image when it is released. The dragging source is the object that “owns” the image that is being dragged; it is specified as an argument to the method that instigates the dragging session.

Dragging is a visual phenomenon. To be the source or destination of a dragging operation, an object must represent a portion of screen real estate; thus, only window and view objects can be the sources and destinations of drags. (Note that the source view is not necessarily the same objects as the dragging source defined above.) NSWindow and NSView provide methods that handle the user interface for dragging an object. You only need to implement a few methods from either the NSDraggingSource or NSDraggingDestination protocol, depending on whether your window or view subclass is the source or destination.

The dragging protocols are described in these articles:

- [Dragging Sources](Dragging%20Sources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe3tmlkdjjbemqsbirda)
- [Dragging Destinations](Dragging%20Destinations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe3tolkciffeessgijdq)

How to receive a drag is described in these articles:

- [Receiving Drag Operations](Receiving%20Drag%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe4tglkcifbeqscjjbbq)
- [Dragging Files](Dragging%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dqlkdivduurseizdq)

Commonly-asked questions about drag-and-drop are addressed in this article:

- [Frequently Asked Questions](Frequently%20Asked%20Questions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dqlkcijbuor2cjbcq)

[Next](Dragging%20Sources.md)

