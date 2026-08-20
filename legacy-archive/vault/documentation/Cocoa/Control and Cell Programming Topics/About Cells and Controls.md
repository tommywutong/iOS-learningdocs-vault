---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Concepts/AboutControlsCells.html
archived_at: '2026-07-15T07:13:44.357614Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](How%20Controls%20and%20Cells%20Interact.md)[Previous](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)

# About Cells and Controls

This topic gives basic information on NSCell and NSControl.

The NSCell class provides a mechanism for displaying text or images in an NSView without the overhead of a full NSView subclass. In particular, it provides much of the functionality of the NSText class by providing access to a shared NSText object used by all instances of NSCell in an application. NSCells are also extremely useful for placing text or images at various locations in a custom subclass of NSView.

NSCell is used heavily by most of the NSControl classes to implement their internal workings. For example, NSSlider uses an NSSliderCell, NSTextField uses an NSTextFieldCell, and NSBrowser uses an NSBrowserCell. Sending a message to the NSControl is often simpler than dealing directly with the corresponding NSCell. For instance, NSControls typically invoke `updateCell:` (causing the cell to be displayed) after changing a cell attribute; whereas if you directly call the corresponding method of the NSCell, the NSCell might not automatically display itself again.

Some subclasses of NSControl (notably NSMatrix) group NSCells in an arrangement where they act together in some cooperative manner. Thus, with an NSMatrix, you can implement a uniformly sized group of radio buttons without needing an NSView for each button (and without needing an NSText object as the field editor for the text on each button).

The NSCell class provides primitives for displaying text or an image, editing text, setting and getting object values, maintaining state, highlighting, and tracking the mouse. NSCell’s method `trackMouse:inRect:ofView:untilMouseUp:` implements the mechanism that sends action messages to target objects. However, NSCell implements target/action features abstractly, deferring the details of implementation to NSActionCell and its subclasses.

NSControl is an abstract superclass that provides three fundamental features for implementing user-interface devices. First, as a subclass of NSView, NSControl draws, or coordinates the drawing of, the on-screen representation of the device. Second, it receives and responds to user-generated events within its bounds by overriding NSResponder’s `mouseDown:` method and providing a position in the responder chain. Third, it implements the `sendAction:to:` method to send an action message to the NSControl’s target object. Subclasses of NSControl defined in the Application Kit are NSBrowser, NSButton (and its subclass NSPopUpButton), NSColorWell, NSImageView, NSMatrix (and its subclass NSForm), NSScroller, NSSlider, NSTableView, and NSTextField. Instances of concrete NSControl subclasses are often referred to as, simply, controls.

[Next](How%20Controls%20and%20Cells%20Interact.md)[Previous](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)

