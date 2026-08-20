---
title: Text Input Management
apple_id: 10000065i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-02'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputManager/Concepts/InputManagerArchitecture.html
archived_at: '2026-07-15T07:16:06.521871Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Input Management](Introduction%20to%20Text%20Input%20Management.md)


[Next](About%20Key%20Bindings.md)[Previous](Introduction%20to%20Text%20Input%20Management.md)

# Text Input Management Architecture

The Cocoa text input management system centers around
three classes that interact with each other to transmit input from
the user’s keyboard or mouse to a text view. An _input server_ (NSInputServer or other NSInputServiceProvider object)
receives keyboard characters and transmits characters to be inserted
into a text view object. An _input manager_ (NSInputManager object) serves
as a proxy for a particular input server and passes messages to
the active input server. Finally, a _text view_ (NSTextView or
other NSTextInput object)
displays, stores, and manages onscreen text.

In the simplest case, the text view passes keyboard events to
the input manager through the standard message-passing hierarchy.
The input manager checks the events against the _key-bindings dictionary_,
which maps certain Control-key events to selectors. If a key-bindings
entry is found in the dictionary, the selector is sent to the input
server. Most events, however, are passed directly to the active
input server as strings of text. The input server processes the
received text and sends a message asking the originating text view
to insert the text, possibly in a modified form.

In more complex scenarios, the input server can do much more
than simply send back the text it receives. Every text view tracks
a region of _marked
text_, a region of text (distinct from the selection, and
usually indicated with a yellow-orange highlight color) that is incomplete—the
input server can retrieve and modify the marked text depending on subsequent
characters. Additionally, input servers can manage palette windows, including
one that appears immediately below the insertion point, for complex
character sets. These facilities allow the input server to output
more characters than it inputs, or vice versa.

Each localization of Mac OS X has a _platform
input server_, which serves as the default input server
on that system. For example, the U.S. English platform input server transforms
Option-E followed by E (two keystrokes) to a single character, an
e with an acute accent. (The Option-E appears as marked text until
the second keystroke completes the input process.) The Japanese
platform input server demonstrates more complex processing, allowing
the user to enter hiragana (phonetic) characters, to pick from a
list of possible kanji (pictogram) characters that could match the
hiragana input in a palette window, and to insert the kanji character
into the text view.

Note that all Application Kit event handling, including text
input, is not thread-safe. If you are writing a multithreaded application,
make sure all event handling takes place in the main thread.

Input servers are
objects that implement the NSInputServiceProvider protocol. Input server
objects are typically instances of NSInputServer or a subclass,
and instances of NSInputServer are typically assigned a delegate to provide
custom input management. For information on creating an input server,
see [Creating Input Servers](Creating%20Input%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaztqlkciffeqssbizea).

Input managers are instances of the NSInputManager
class. You never have to instantiate or subclass NSInputManager,
and in general you never have to directly access its methods either.
The only place that its methods need to be accessed are within the
implementation of a text view that does not inherit from NSTextView.

Text views are instances
of classes that implement the NSTextInput protocol. The most common
example of a text view is an NSTextView object or instance of a
subclass of NSTextView.

If you need more sophisticated text handling than NSTextView
provides, for example in a word processing application, you may
need to create a text view that does not inherit from NSTextView.
In this case, you will need to implement the NSTextInput protocol
and access NSInputManager methods from within the implementation.
For information on creating custom text views, see [Creating Custom Views](Creating%20Custom%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dsmbrfvbegskdivdeori).

[Next](About%20Key%20Bindings.md)[Previous](Introduction%20to%20Text%20Input%20Management.md)

