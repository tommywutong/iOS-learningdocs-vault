---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/TextViewTask.html
archived_at: '2026-07-15T07:20:17.080667Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Synchronizing%20Editing.md)[Previous](Subclassing%20NSTextView.md)

# Creating Custom Views

This article explains how to use the text input system when implementing a custom view. This information is relevant to anyone adding to their view keyboard input capabilities that `NSTextView` does not provide.

Custom Cocoa views can provide varying levels of support for the text input system. There are essentially three levels of support to choose from:

1. Override the [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown) method.
2. 

   Override `keyDown:` and use [handleEvent:](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528602-handleevent) to support key bindings.
3. 

   Also implement the full `NSTextInputClient` protocol.

In the first level of support, the `keyDown:` method recognizes a limited set of events and ignores others. This level of support is typical of games. (When overriding [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown), you must also override [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder) to make your custom view respond to key events, as described in “[Event Handling Basics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventHandlingBasics/EventHandlingBasics.html#//apple_ref/doc/uid/10000060i-CH5)” in _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.)

In the second level of support, you can override `keyDown:` and use the [handleEvent:](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528602-handleevent) method to receive key-binding support without implementing the `NSTextInputClient` protocol. Because the `NSView` method `inputContext` does not instantiate `NSTextInputContext` automatically if the view does not conform to `NSTextInputClient`, the custom view must instantiate it manually. You then implement the standard key-binding methods that your view wants to support, such as `moveForward:` or `deleteForward:`. (The full list of key-binding methods can be found in `NSResponder.h`.)

If you are writing your own text view from scratch, you should use the third level of support and implement the `NSTextInputClient` protocol in addition to overriding `keyDown:` and using [handleEvent:](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528602-handleevent). `NSTextView` and its subclasses are the only classes provided in Cocoa that implement `NSTextInputClient`, and if your application needs more complex behavior than `NSTextView` can provide, as a word processor might, you may need to implement a text view from the ground up. To do this, you must subclass `NSView` and implement the `NSTextInputClient` protocol. (A class implementing this protocol—by inheriting from `NSTextView` or by implementing the protocol directly—is called a text view.)

If you are implementing the `NSTextInputClient` protocol, your view needs to manage marked text and communicate with the text input context to support the text input system. These tasks are described in the next two sections.

One of the primary things that a text view must do to cooperate with an input context is to maintain a (possibly empty) range of _marked text_ within its text storage. The text view should highlight text in this range in a distinctive way, and it should allow selection within the marked text. A text view must also maintain an _insertion point_, which is usually at the end of the marked text, but the user can place it within the marked text. The text view also maintains a (possibly empty) _selection_ range within its text storage, and if there is any marked text, the selection must be entirely within the marked text.

A common example of marked text appears when a user enters a character with multiple keystrokes, such as “é”, in an `NSTextView` object. To enter this character, the user needs to type Option-E followed by the E key. After pressing Option-E, the accent mark appears in a highlighted box, indicating that the text is marked (not final). After the final E is pressed, the “é” character appears and the highlight disappears.

A text view and a text input context must cooperate so that the input context can implement its user interface. The `NSTextInputContext` class represents the interface to the text input system, that is, a state or context unique to its client object such as the key binding state, input method communication session, and so on. Most of the `NSTextInputClient` protocol methods are called by an input context to manipulate text within the text view for the input context’s user-interface purposes.

Each `NSTextInputClient`-compliant object (typically an `NSView` subclass) has its own `NSTextInputContext` instance. The default implementation of the `NSView` method `inputContext` manages an `NSTextInputContext` instance automatically if the view subclass conforms to the `NSTextInputClient` protocol.

A text view must inform the current input manager when a mouse or keyboard event happens by sending the [handleEvent:](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528602-handleevent) message to the current input context. When its marked text range is no longer needed, the text view sends a [discardMarkedText](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528752-discardmarkedtext) message to the current input context.

In addition, a text view must tell the input context when position information for a character range changes, such as when the text view scrolls, by sending the [invalidateCharacterCoordinates](https://developer.apple.com/documentation/appkit/nstextinputcontext/1535165-invalidatecharactercoordinates) message to the input context. The input context can then update information previously queried via methods like [firstRectForCharacterRange:actualRange:](https://developer.apple.com/documentation/appkit/nstextinputclient/1438240-firstrect) when, for example, it wants to show a selection pop-up menu for marked text (as with a Japanese input method). There is an optional method, `drawsVerticallyForCharacterAtIndex:`, that can inform the text input system whether the protocol-conforming client renders the character at the given index vertically.

The input context generally uses all of the methods in the `NSTextInputClient` protocol. You can also register to receive a notification from the input context when the keyboard layout changes.

[Next](Synchronizing%20Editing.md)[Previous](Subclassing%20NSTextView.md)

