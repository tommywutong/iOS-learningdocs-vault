---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Concepts/KeyBindings.html
archived_at: '2026-07-15T07:20:09.374787Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Intercepting%20Key%20Events.md)[Previous](Overview%20of%20Text%20Editing.md)

# About Key Bindings

The text input system uses a dictionary property list, called a _key-bindings
dictionary_, to interpret keyboard events before
passing them to the Input Method Kit framework for mapping to characters.

During the processing of a keyboard event, the event passes
through the `NSMenu` object, then to
the first responder via the `keyDown:` method.
The default implementation of the method provided by the `NSResponder`
class propagates
the message up the responder chain until an overridden `keyDown:` implementation
stops the propagation. Typically, an `NSResponder` subclass can choose
to process certain keys and ignore others (for example, in a game)
or to send the [handleEvent:](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528602-handleevent)  message to its input context.

The input context checks the event
to see if it matches any of the keystrokes in the user’s key-bindings
dictionary. A key-bindings dictionary maps a keystroke (including
its modifier keys) to a method name. For example, the default key-bindings
dictionary maps `^d` (Control-D)
to the method name `deleteForward:`.
If the keyboard event is in the dictionary, then the input context
calls the text view’s `doCommandBySelector:` method
with the selector associated with the dictionary entry.

If the input context cannot match the keyboard event to an
entry in the key-bindings dictionary, it passes the event to the Input Method Kit for mapping to characters.

The standard key-bindings dictionary is in the file `/System/Library/Frameworks/AppKit.framework/Resources/StandardKeyBinding.dict`.
You can override the standard dictionary entirely by providing a
dictionary file at the path `~/Library/KeyBindings/DefaultKeyBinding.dict`. However, defining custom key bindings dynamically (that is, while the application is running) is not supported.

[Next](Intercepting%20Key%20Events.md)[Previous](Overview%20of%20Text%20Editing.md)

