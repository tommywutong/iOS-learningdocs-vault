---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Tasks/SubclassingNSCell.html
archived_at: '2026-07-15T07:13:48.870159Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Subclassing%20NSControl.md)[Previous](Using%20a%20Continuous%20Control.md)

# Subclassing NSCell

The `initImageCell:` method is the designated initializer for NSCells that display images. The `initTextCell:` method is the designated initializer for NSCells that display text. Override one or both of these methods if you implement a subclass of NSCell that performs its own initialization. If you need to use target and action behavior, you may prefer to subclass NSActionCell or one of its subclasses, which provide the default implementation of this behavior.

If you want to implement your own mouse-tracking or mouse-up behavior, consider overriding `startTrackingAt:inView:`, `continueTracking:at:inView:`, and `stopTracking:at:inView:mouseIsUp:`. If you want to implement your own drawing, override `drawWithFrame:inView:` or `drawInteriorWithFrame:inView:`.

If the subclass contains instance variables that hold pointers to objects, consider overriding `copyWithZone:` to duplicate the objects. The default version copies only pointers to the objects.

[Next](Subclassing%20NSControl.md)[Previous](Using%20a%20Continuous%20Control.md)

