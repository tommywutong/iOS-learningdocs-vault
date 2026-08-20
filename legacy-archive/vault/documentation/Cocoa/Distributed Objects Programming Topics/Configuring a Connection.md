---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/configuring.html
archived_at: '2026-07-15T07:15:02.258486Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Handling%20Connection%20Errors.md)[Previous](Getting%20a%20Vended%20Object.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Configuring a Connection

You can control some factors of distributed objects communication by configuring `NSConnection` objects. You can set timeouts to limit the amount of time an `NSConnection` object waits on a remote message, set the mode it awaits requests and responses on, and control how an `NSConnection` object manages multiple remote messages. In addition to these parameter settings, you can change an `NSConnection` object’s registered name or root object for dynamic alteration of your distributed application.

An `NSConnection` object uses two kinds of timeouts, one for outgoing messages and one for replies. An outgoing network message may take some time to send. Once it goes out, there is usually a delay before any return value arrives. If either of these operations exceeds its timeout, the `NSConnection` object raises an `NSPortTimeoutException`. You can set the values for these timeouts with the `setRequestTimeout:` and `setReplyTimeout:` messages, respectively. By default these timeouts are set to the maximum possible value.

`NSConnection` objects that vend objects await new connection requests in `NSDefaultRunLoopMode` (as defined by the `NSRunLoop` class). When an `NSConnection` object sends a remote message out, it awaits the return value in `NSConnectionReplyMode`. You cannot change this mode, but you can use it to set up `NSTimer` objects or other input mechanisms that need to be processed while awaiting replies to remote messages. Use `addRequestMode:` to add input mechanisms for this mode.

Normally an `NSConnection` object forwards remote messages to their intended recipients as it receives them. If your application returns to the run loop or uses distributed objects either directly or indirectly, it can receive a remote message while it is already busy processing another. Suppose a server is processing a remote message and sends a message to another application through distributed objects. If another application sends a message to the server, its `NSConnection` object immediately forwards it to the intended recipient, even though the server is also awaiting a reply on the outgoing message. This behavior can cause problems if a remote message causes a lengthy change in the server application’s state that renders it inconsistent for a time: Other remote messages may interfere with this state, either getting incorrect results or corrupting the state of the server application. You can turn this behavior off with the `setIndependentConversationQueueing:` method, so that only one remote message is allowed to be in effect at any time within the `NSConnection` object’s thread. When independent conversation queueing is turned on, the `NSConnection` object forwards incoming remote messages only when no other remote messages are being handled in its thread. This only affects messages between objects, not requests for new connections; new connections can be formed at any time.

One other way to configure a named `NSConnection` object is to change its name or root object. This effectively changes the object that applications get using the techniques described in [Getting a Vended Object](Getting%20a%20Vended%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43dklkciffeoqsbijdq), but does not change the proxies that other applications have already received. You might use this technique to field-upgrade a distributed application with an improved server object class. For example, to install a new server process have the old one change its name, perhaps from “Analysis Server” to “Old Analysis Server”. This hides it from clients attempting to establish new connections, but allows its root object to serve existing connections (when those connections close, the old server process exits). In the meantime, launch the new server which claims the name “Analysis Server” so that new requests for analyses contact the updated object.

Note that for inter-host communication, you cannot use the default connection, default `NSPort` subclass, or default port name server. You must use an `NSPort` subclass that supports inter-machine communication, such as `NSSocketPort`. You might configure the server as shown in the following code fragment.

```
NSSocketPort *port = [[NSSocketPort alloc] init];
NSConnection *connection = [NSConnection connectionWithReceivePort:port sendPort:nil];
[[NSSocketPortNameServer sharedInstance] registerPort:port name:@"doug"];
```

You would then configure the client as follows.

```
NSSocketPort *port = [[NSSocketPortNameServer sharedInstance] portForName:@"doug" host:@"*"];
NSConnection *connection = [NSConnection connectionWithReceivePort:nil sendPort:port];
```

[Next](Handling%20Connection%20Errors.md)[Previous](Getting%20a%20Vended%20Object.md)

