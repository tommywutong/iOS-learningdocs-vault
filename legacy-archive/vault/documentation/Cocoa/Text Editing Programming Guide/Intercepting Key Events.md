---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/InterceptKeys.html
archived_at: '2026-07-15T07:20:15.407399Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Delegate%20Messages%20and%20Notifications.md)[Previous](About%20Key%20Bindings.md)

# Intercepting Key Events

This article explains how to catch key events received by a text view so that you can modify the result. It also explains the message sequence that occurs when a text view receives a key event.

You need to intercept key events, for example, if you want users to be able to insert a line-break character in a text field. By default, text fields hold only one line of text. Pressing either Enter or Return causes the text field to end editing and send its action message to its target, so you would need to modify the behavior.

You may also wish to intercept key events in a text view to do something different from simply entering characters in the text being displayed by the view, such as changing the contents of an in-memory buffer.

In both circumstances you need to deal with the text view object, which is obvious for the text view case but less so for a text field. Editing in a text field is performed by an `NSTextView` object, called the field editor, shared by all the text fields belonging to a window.

When a text view receives a key event, it sends the character input to the input context for key binding and interpretation. In response, the input context sends either `insertText:replacementRange:` or `doCommandBySelector:` to the text view, depending on whether the key event represents text to be inserted or a command to perform. The input context can also send the [setMarkedText:selectedRange:replacementRange:](https://developer.apple.com/documentation/appkit/nstextinputclient/1438246-setmarkedtext) message to set the marked text in the text view’s associated text storage object. The message sequence invoked when a text view receives key events is described in more detail in [The Key-Input Message Sequence](Overview%20of%20Text%20Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdsljvga2dsni).

With the standard key bindings, an Enter or Return character causes the text view to receive `doCommandBySelector:` with a selector of `insertNewline:`, which can have one of two results. If the text view is not a field editor, the text view’s `insertText:replacementRange:` method inserts a line-break character. If the text view is a field editor, as when the user is editing a text field, the text view ends editing instead. You can cause a text view to behave in either way by calling `setFieldEditor:`.

Although you could alter the text view’s behavior by subclassing the text view and overriding `insertText:replacementRange:` and `doCommandBySelector:`, a better solution is to handle the event in the text view’s delegate. The delegate can take control over user changes to text by implementing the `textView:shouldChangeTextInRange:replacementString:` method.

To handle keystrokes that don’t insert text, the delegate can implement the `textView:doCommandBySelector:` method.

To distinguish between Enter and Return, for example, the delegate can test the selector passed with `doCommandBySelector:`. If it is `@selector(insertNewline:)`, you can send `currentEvent` to `NSApp` to make sure the event is a key event and, if so, which key was pressed.

[Next](Delegate%20Messages%20and%20Notifications.md)[Previous](About%20Key%20Bindings.md)

