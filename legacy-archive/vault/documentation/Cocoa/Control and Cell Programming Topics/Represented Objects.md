---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Concepts/RepresentedObjects.html
archived_at: '2026-07-15T07:13:45.863030Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Cell%20States.md)[Previous](How%20Controls%20and%20Cells%20Interact.md)

# Represented Objects

Represented objects are objects an NSCell stands for. (They’re not to be confused with an NSCell’s object value, which is the value of the cell.) By setting a represented object for an NSCell (using `setRepresentedObject:`) you make an association between the NSCell and that object. For instance, you could have a pop-up list, each cell of which lists a color as its title; when the user selects a cell, the represented NSColor object is displayed in a color well. This feature is solely for the developer’s convenience. The cell itself does not use the represented object, except to archive and restore it.

[Next](Cell%20States.md)[Previous](How%20Controls%20and%20Cells%20Interact.md)

