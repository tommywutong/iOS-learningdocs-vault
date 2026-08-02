---
title: Text Input Management
apple_id: 10000065i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-02'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputManager/Tasks/TextViewTask.html
archived_at: '2026-07-15T07:16:09.555101Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Input Management](Introduction%20to%20Text%20Input%20Management.md)


[Next](Document%20Revision%20History.md)[Previous](Deploying%20Input%20Servers.md)

# Creating Custom Views

This section explains how to use the text input
management system when implementing a custom view.
This information is relevant to anyone adding keyboard input capabilities to
their view that NSTextView does not
provide.

Custom Cocoa views can provide varying levels of support for
the text input management system. There are essentially three levels
of support to choose from:

1. Override the `keyDown:` method.
2. 

   Override `keyDown:` and
   use `interpretKeyEvents:` to
   support key bindings.
3. 

   Also implement the full NSTextInput protocol.

In the first level of support, the `keyDown:` method
recognizes a limited set of events and ignores others. This level
of support is typical of games. (When overriding [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown), you must also override [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder) to make your custom view respond to key events, as described in [Event Objects and Types](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventObjectsTypes/EventObjectsTypes.html#//apple_ref/doc/uid/10000060i-CH4).)

In the second level of support, you can override `keyDown:` and
use the `interpretKeyEvents:` method
to receive key-binding support without implementing the NSTextInput
protocol. You then implement the standard key-binding methods that
your view wants to support, such as `moveForward:` or `deleteForward:`.
(The full list of key-binding methods can be found in `NSResponder.h`.)

If you are writing your own text view from scratch, you should
use the third level of support and implement the NSTextInput protocol
in addition to overriding `keyDown:` and using `interpretKeyEvents:`.
NSTextView and its subclasses are the only classes provided in Cocoa
that implement NSTextInput, and if your application needs more complex behavior
than NSTextView can provide, as a word processor might, you may
need to implement a text view from the ground up. To do this, you
must subclass NSView and implement
the NSTextInput protocol. A class implementing this protocol—by
inheriting from NSTextView or another class, or by implementing
the protocol directly—is called a _text
view_.

If you are implementing NSTextInput, your view needs to manage
marked text and communicate with the input server to support the
text input management system. These tasks are described in the next
two sections.

One of the primary
things that a text view must do to cooperate with an input server
is to maintain a (possibly empty) range of _marked text_ within
its text storage. The text view should highlight text in this range
in a distinctive way, and it should allow selection within the marked
text. A text view must also maintain an _insertion point_,
which is usually at the end of the marked text, but the user can
place it within the marked text. The text view also maintains a
(possibly empty) _selection_ range within its text
storage, and if there is any marked text, the selection must
be entirely within the marked text.

A common example of marked text appears when a user enters
a character with multiple keystrokes, such as “é”, in an NSTextView
object. To enter this character, the user needs to type Option-E
followed by the E key. After pressing Option-E, the accent mark
appears in a highlighted box, indicating that the text is marked
(not final). After the final E is pressed, the “é” character
appears and the highlight disappears.

An input server and a text view must
cooperate so that the input server can implement its user interface.
The bulk of the NSTextInput protocol comprises methods called by
an input server to manipulate text within the text view for the
input server’s user interface purposes.

A text view must also inform the current input manager when
its marked text range changes or a mouse event happens. The text
view accomplishes this by calling the `markedTextSelectionChanged:client:`, `markedTextAbandoned:`,
and `handleMouseEvent:` methods
with the current input manager.

If the text view receives a mouse event within its
text area, and a marked text range exists, it must call the current
input manager’s `wantsToHandleMouseEvents`.
If `wantsToHandleMouseEvents` returns `YES`,
it must forward those mouse events to the input manager’s `handleMouseEvent:` method.
If it returns `NO`, it
is up to the text view to determine what to do with the event.

If the input server returns `NO` to
both `wantsToHandleMouseEvents` and `handleMouseEvent:`,
and the text view decides to change selection within the marked range,
it must notify the current input manager of the change with the `markedTextSelectionChanged:client:` method.
In general, however, the input server is responsible for managing
the selection within the marked text.

Also, the text view must call the current input manager’s `markedTextAbandoned:` method when
the insertion point leaves the marked text or whenever it decides
to clear the marked range.

The current input server generally uses all of the methods
in the NSTextInput protocol except for the `hasMarkedText` method.
The text view itself may call this method to determine whether there
is currently marked text. NSTextView, for example, disables Copy
in the Edit menu when `hasMarkedText` returns `YES`.

[Next](Document%20Revision%20History.md)[Previous](Deploying%20Input%20Servers.md)

