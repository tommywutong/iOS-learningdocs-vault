---
title: Text Input Management
apple_id: 10000065i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-02'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputManager/Concepts/KeyBindings.html
archived_at: '2026-07-15T07:16:07.027234Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Input Management](Introduction%20to%20Text%20Input%20Management.md)


[Next](Creating%20Input%20Servers.md)[Previous](Text%20Input%20Management%20Architecture.md)

# About Key Bindings

Input managers use a dictionary property list, called a _key-bindings
dictionary_, to interpret keyboard events before
passing them to an input server.

During the processing of a keyboard event, the event passes
through the NSMenu object, then to
the first responder via the `keyDown:` method.
The default implementation of the method provided by the NSResponder
class propagates
the message up the responder chain until an overridden `keyDown:` implementation
stops the propagation. Typically, an NSResponder subclass can choose
to process certain keys and ignore others (for example, in a game)
or to call the `interpretKeyEvents:` method,
which passes the event to the current input manager.

The input manager checks the event
to see if it matches any of the keystrokes in the user’s key-bindings
dictionary. A key-bindings dictionary maps a keystroke (including
its modifier keys) to a method name. For example, the default key-bindings
dictionary maps `^d` (Control-D)
to the method name `deleteForward:`.
If the keyboard event is in the dictionary, then the input manager
calls the input server’s `doCommandBySelector:client:` method
with the selector associated with the dictionary entry. If the input
server’s `doCommandBySelector:client:` method
doesn’t find a matching method, then it passes the command selector onto the text view’s `doCommandBySelector:` method,
which may or may not find a matching method to call.

If the input manager cannot match the keyboard event to an
entry in the key-bindings dictionary, it extracts the string from
the event by using its `characters` method
and passes the returned characters to the input server’s `insertText:client:` method.

The standard key-bindings dictionary is in the file `/System/Library/Frameworks/AppKit.framework/Resources/StandardKeyBinding.dict`.
You can override the standard dictionary entirely by providing a
dictionary file at the path `~/Library/KeyBindings/DefaultKeyBinding.dict`. However, defining custom key bindings dynamically (that is, while the application is running) is not supported.

[Next](Creating%20Input%20Servers.md)[Previous](Text%20Input%20Management%20Architecture.md)

