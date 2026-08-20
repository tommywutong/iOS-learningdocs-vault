---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Concepts/ControlsAndCells.html
archived_at: '2026-07-15T07:13:45.358319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Represented%20Objects.md)[Previous](About%20Cells%20and%20Controls.md)

# How Controls and Cells Interact

Controls are usually associated with one or more cells—instances of a subclass of the abstract class NSCell. A control’s cell (or cells) usually fit just inside the bounds of the control. Cells are objects that can draw themselves and respond to events, but they can do so only indirectly, upon instruction from their control, which acts as a kind of coordinating backdrop.

Controls manage the behavior of their cells. By inheritance from NSView, controls derive the ability for responding to user actions and rendering their on-screen representation. When users click on a control, it responds in part by sending `trackMouse:inRect:ofView:untilMouseUp:` to the cell that was clicked. Upon receiving this message, the cell tracks the mouse and may have the control send the cell’s action message to its target (either upon mouse-up or continuously, depending on the cell’s attributes). When controls receive a display request, they, in turn, send their cell (or cells) a `drawWithFrame:inView:` message to have the cells draw themselves.

This relationship of control and cell makes two things possible: A control can manage cells of different types and with different targets and actions (see below), and a single control can manage multiple cells. Most Application Kit controls, like NSButtons and NSTextFields, manage only a single cell. But some controls, notably NSMatrix and NSForm, manage multiple cells (usually of the same size and attributes, and arranged in a regular pattern). Because cells are lighter-weight than controls, in terms of inherited data and behavior, it is more efficient to use a multi-cell control rather than multiple controls.

Many methods of NSControl—particularly methods that set or obtain values and attributes—have corresponding methods in NSCell. Sending a message to the control causes it to be forwarded to the control’s cell or (if a multi-cell control) its selected cell. However, many NSControl methods are effective only in controls with single cells (these are noted in the method descriptions).

An NSControl subclass doesn’t have to use an NSCell subclass to implement itself—NSScroller and NSColorWell are examples of NSControls that don’t. However, such subclasses have to take care of details NSCell would otherwise handle. Specifically, they have to override methods designed to work with a cell. What’s more, the lack of a cell means you can’t make use of NSMatrix capability for managing multi-cell arrays such as radio buttons.

[Next](Represented%20Objects.md)[Previous](About%20Cells%20and%20Controls.md)

