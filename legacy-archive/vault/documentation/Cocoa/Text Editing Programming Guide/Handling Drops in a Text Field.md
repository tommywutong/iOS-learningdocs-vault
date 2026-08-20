---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/HandlingDrops.html
archived_at: '2026-07-15T07:20:14.894653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Working%20With%20the%20Field%20Editor.md)

# Handling Drops in a Text Field

To handle drag and drop in a text field, you need to subclass `NSTextField` and add support for the operation. This works well as long as the text field is not currently being edited. To handle drag and drop while the text field is being edited, you must implement support in the field editor.

To provide a custom field editor for your text field (or any other control) you need to implement a method to respond to the `NSWindow` delegate message `windowWillReturnFieldEditor:toObject:` in the delegate of the window containing the text field you want to respond to drags. The client specified in the `toObject:` argument is the text field that is about to be edited, for which it uses the `NSTextView` object you return instead of the standard field editor.

`NSTextView` has support for drag and drop through the `NSDragging` category. However, an `NSTextView` object registers for draggable pasteboard types only if it is set up to handle rich text (see the `setRichText:` method) and allows attached files (see the `setImportsGraphics:` method). By default, `NSTextView` does not accept dragged files.

To support new data types for dragging operations, you should override the `acceptableDragTypes` method. Your implementation of these methods should invoke the superclass implementation, add the new data types to the array returned from the superclass, and return the modified array. You must also override the appropriate methods of the `NSDraggingDestination` protocol to support importing those types. See that protocol reference for more information. Also see _[Drag and Drop Programming Topics](../Drag%20and%20Drop%20Programming%20Topics/Introduction%20to%20Drag%20and%20Drop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ds2i)_.

[Next](Document%20Revision%20History.md)[Previous](Working%20With%20the%20Field%20Editor.md)

