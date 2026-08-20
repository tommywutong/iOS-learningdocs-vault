---
title: Text Input Management
apple_id: 10000065i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-02'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputManager/Tasks/InputServerCreation.html
archived_at: '2026-07-15T07:16:08.527927Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Input Management](Introduction%20to%20Text%20Input%20Management.md)


[Next](Deploying%20Input%20Servers.md)[Previous](About%20Key%20Bindings.md)

# Creating Input Servers

This article explains how to implement an input
server for
the Cocoa text input system. If you want to create an input method
that can be accessed from both Cocoa and Carbon applications, use
the Text Services Manager in the Carbon framework.

For an example of a custom Cocoa input server, see HexInputServer,
located at
`/Developer/Examples/AppKit/HexInputServer`.

To create an input server, you can either subclass NSInputServer or instantiate
an NSInputServer object with a delegate. The second choice normally
suffices. If you choose to subclass NSInputServer, you usually override
most or all of the methods required by the NSInputServiceProvider
protocol.
If you assign a delegate object, the delegate must implement the
NSInputServiceProvider protocol.

The input management
classes identify each text-modification message with a _client_ and
a _conversation identifier_. Clients are instances
of the NSInputManager class associated with applications, and conversation
identifiers specify
the text views within applications.
The input server talks to multiple clients (applications), and each
client controls multiple conversations (text views).

Unless your input server processes only single characters,
it needs a way to keep track of multiple clients and conversations.
A straightforward way to do this is to define a context object class
to handle individual input clients, and map clients to context objects
with a dictionary. You can convert the addresses of client objects
(pointers) to NSNumber objects, and
use the resulting NSNumber as a key for the context object. The
following C macro converts client addresses to NSNumber keys:

```
#define KEY_FROM_CLIENTID(theClient) ([NSNumber numberWithUnsignedInt:
                                            (unsigned int)theClient])
```

Additionally, within each context object, you need to map
conversation numbers (type `long`)
to check that input server messages correspond to the current conversation.
You can again use a dictionary or other data structure to perform
the mapping.

Input servers can manage an active portion of a text view,
called the _marked text_, which is visually marked
so the user knows it is not final. To set the marked text range, use the input client’s `setMarkedText:selectedRange:` method.
To retrieve the current marked range, use the `markedRange` method.
This code fragment replaces the current marked range with the string `outputBuffer` in
the text input client `client` and
sets the selected range to the new string:

```
id client;              // Assume this exists and implements NSTextInput.
NSString *outputBuffer; // Assume this exists.

[client setMarkedText:outputBuffer
        selectedRange:NSMakeRange(0,[outputBuffer length]);
```

To unmark the text in a client view, use the NSTextInput `unmarkText` method.

To retrieve the text formatting attributes supported by a
client view, use the `validAttributesForMarkedText` method.
See the additions to NSAttributedString in the Application
Kit for the set of string constants supported by the view.

To make an input server receive mouse events—for example,
to handle selection—as well as keyboard events, you should implement
its `wantsToHandleMouseEvents` to
return `YES`. Additionally,
to handle mouse events the input server must implement the NSInputServerMouseTracker
protocol, which consists
of three methods: `mouseDownOnCharacterIndex:atCoordinate:withModifier:client:`, `mouseDraggedOnCharacterIndex:atCoordinate:withModifier:client:`,
and `mouseUpOnCharacterIndex:atCoordinate:withModifier:client:`,
for mouse-down, mouse-dragged, and mouse-up events, respectively.

[Next](Deploying%20Input%20Servers.md)[Previous](About%20Key%20Bindings.md)

