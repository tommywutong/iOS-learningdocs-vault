---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/SetFocus.html
archived_at: '2026-07-15T07:20:15.909983Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Working%20With%20the%20Field%20Editor.md)[Previous](Synchronizing%20Editing.md)

# Setting Focus and Selection Programmatically

Usually the user clicks a view object in a window to set the focus, or first responder status, so that subsequent keyboard events go to that object initially. Likewise, the user usually creates a selection by dragging the mouse in a view. However, you can set both the focus and the selection programmatically.

For example, if you have a window that contains a text view, and you want that text view to become the first responder with the insertion point located at the beginning of any text currently in the text view, you need a reference to the window and the text view. If those references are `theWindow` and `theTextView`, respectively, you can use the following code to set the focus and the insertion point, which is simply a zero-length selection range:

```
[theWindow makeFirstResponder: theTextView];
[theTextView setSelectedRange: NSMakeRange(0,0)];
```

When an object conforming to the `NSTextInputClient` protocol becomes the first responder in the key window, its `NSTextInputContext` object becomes active and bound to the active text input sources, such as character palette, keyboards, and input methods.

Whether the selection was set programmatically or by the user, you can get the range of characters currently selected using the `selectedRange` method. `NSTextView` indicates its selection by applying a special set of attributes to it. The `selectedTextAttributes` method returns these attributes, and `setSelectedTextAttributes:` sets them.

While changing the selection in response to user input, an `NSTextView` object invokes its `setSelectedRange:affinity:stillSelecting:` method. The first argument is the range to select. The second, called the selection affinity, determines which glyph the insertion point displays near when the two glyphs defining the selected range are not adjacent. It’s typically used where the selected lines wrap to place the insertion point at the end of one line or the beginning of the following line. You can get the selection affinity currently in effect using the `selectionAffinity` method. The last argument indicates whether the selection is still in the process of changing; the delegate and any observers aren’t notified of the change in the selection until the method is invoked with `NO` for this argument.

Another factor affecting selection behavior is the selection granularity: whether characters, words, or whole paragraphs are being selected. This is usually determined by number of initial mouse clicks; for example, a double click initiates word-level selection. `NSTextView` decides how much to change the selection during input tracking using its `selectionRangeForProposedRange:granularity:` method.

An additional aspect of selection, related to input management, is the range of marked text. As the input context interprets keyboard input, it can mark incomplete input in a special way. The text view displays this marked text differently from the selection, using temporary attributes that affect only display, not layout or storage. For example, `NSTextView` uses marked text to display a combination key, such as Option-E, which places an acute accent character above the character entered next. When the user types Option-E, the text view displays an acute accent in a yellow highlight box, indicating that it is marked text, rather than final input. When the user types the next character, the text view displays it as a single accented character, and the marked text highlight disappears. The `markedRange` method returns the range of any marked text, and `markedTextAttributes` returns the attributes used to highlight the marked text. You can change these attributes using `setMarkedTextAttributes:`.

[Next](Working%20With%20the%20Field%20Editor.md)[Previous](Synchronizing%20Editing.md)

